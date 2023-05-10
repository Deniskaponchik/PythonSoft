import requests
import time
import sqlite3
# при вызове методов нужно указывать параметры,например id страницы, которую парсим, и нам жизненно необходим для парсинга token, поэтому на вход мы будем подавать три аргумента: метод, параметр и token
# !!! Не забудем обновить токен (каждые сутки), чтобы продолжить парсить Вконтакте !!!
token = '8f68c42072557646091a1b5d80005abddcfc51e7890a39c00b821c444674431cfdb65f267ca2eddf604e6'
# page_id = '179828038'
page_id = 'dm'
# создадим переменную для того, чтобы хранить количество постов, которые мы будем качать
#n = 1


""" БЕЗ функции
# Для начала попробуем "вытащить" имя со страницы
# Для этого воспользуемся методом users.get. метод возвращает расширенную информацию о пользователе
# Нам понадобится параметр user_ids, который отвечает за пользователей, информацию о которых нам хотелось бы вытащить
url = 'https://api.vk.com/method/users.get?user_ids=' + page_id + '&access_token=' + token + "&v=5.131"
# Теперь у нас есть ссылка по которой можно скачать информацию со страницы
# Для самого скачивания воспользуемся функцией get() из библиотеки requests, в скобках передадим url. Для хранения информации создадим переменную response
response = requests.get(url)
user_name = response.json()
#print(user_name)
title_page = user_name['response'][0]
print(title_page)
"""
def vk_download(method, parameters, token=token):
    url = 'https://api.vk.com/method/' + method + '?' + parameters + '&access_token=' + token + "&v=5.131"
    response = requests.get(url)
    #return (response.json())
    try:
        return (response.json())['response']
    except:
        print('Пожалуйста, обновите токен, для этого воспользуйтесь ссылкой из файла main.py')
        exit()

#Мы уже знаем, что title_page и wall являются словарями в словарях (как мы помним из курса теории в словаре есть ключи и значения, а значениями может быть все что угодно, но стоит указать, что значения, как в нашем случае, лежат в списке. Т.е  мы имеем словарь, который обернут в список и доступен по значению из другого словаря), избавимся от внешнего словаря:
#print(vk_download('users.get','user_ids='+page_id))
title_page = vk_download('users.get','user_ids='+page_id)
#title_page = title_page['response']
#Как мы помним - после функции у нас получается словарь, который мы раскрываем в 18ой строчке. Если вывести то что получилось до этой строчки, мы увидим еще один словарь, но на самом деле этот словарь лежит в списке и является его единственным членом
#Для того чтобы получить словарь, мы раскрываем список [0], затем мы в словаре ищем нужное нам значение ['id'], которое мы получаем в целочисленном формате, а для совмещения его со строкой нужно преобразовать его к строковому типу с помощью str()
new_id = str(title_page[0]['id'])
#print(vk_download('wall.get','owner_id=' + '53083705'))
#wall = vk_download('wall.get','owner_id=' + '53083705')
wall = vk_download('wall.get','owner_id=' + new_id)
#wall = wall['response']
count_notes = wall['count']
name_page = title_page[0]['first_name'] + ' ' + title_page[0]['last_name']
n = int(input('На странице '+str(count_notes)+' записей. Сколько скачаем записей? '))
#Теперь сравним сколько постов всего и сколько скачалось.
#print(wall['count'])        # смотрим значение из словаря по ключу
#print(len(wall['items']))   # считаем словарь, к которому обратились по ключу

conn = sqlite3.connect(name_page+'.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS wall(
   number TEXT,
   author TEXT,
   comments TEXT,
   likes TEXT,
   reposts TEXT);
""")


#Мы будем скачивать по одному посту, рассортировывать данные и качать следующий. При этом каждый раз нам необходимо смещать строчку, чтобы не качать один и тот же пост снова, за количество уже скачанных постов у нас отвечает i, поэтому именно эта переменная лежит в offset
for i in range(0,n):  # создать цикл, в котором мы будем скачивать посты
    #для того чтобы скачивать определенное количество записей со стены, нам нужно ввести дополнительный параметр
    #count отвечает за количество скачиваемых постов, а offset за смещение
    param = '&count=1&offset=' + str(i)
    note = vk_download('wall.get', 'owner_id=' + new_id + param)
    #после скачивания у нас будет словарь в словаре и для того, чтобы получить доступ к внутреннему словарю необходимо "раскрыть внешний":
    #note = note['response']
    #Сейчас в note лежит словарь с двумя ключами: count и items. В первом ключе находится общее количество постов, а во втором - список с записями (в нашем случае одной записью). Поэтому давайте сразу перейдем к словарю скачанной записи
    note = note['items'][0]
    author_note, coments_count = 'Гость', str(note['comments']['count'])
    likes_count, reposts_count = str(note['likes']['count']), str(note['reposts']['count'])
    #в переменной author_note лежит всегда одно и то же значение.Нам необходимо создать условный оператор, который будет определять автора
    if int(note['from_id']) == int(note['owner_id']):
        author_note = 'Владелец'

    #print(author_note, coments_count, likes_count, reposts_count)
    #база данных готова, а вот для заполнения нам нужно создать список. Мы просто отправим в базу данных список, и она сама все распределит
    information_recording = (i, author_note, coments_count, likes_count, reposts_count)
    cur.execute("INSERT INTO wall VALUES(?, ?, ?, ?, ?);", information_recording)
    conn.commit() # Save changes
    time.sleep(0.5) # Вконтакте ограничивает количество запросов в секунду, нам нужно установить задержку
    print('Записей скачано:', i + 1)
print('Посты скачаны. Всего скачано: ' + str(n))
