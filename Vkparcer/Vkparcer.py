# TARGET = Мы возьмем две группы, возьмем несколько постов из неё и соберем всех лайкнувших эти посты. У каждого лайкнувшего мы узнаем имя, id страницы, номер телефона, сайт, ну и соберем общее количество лайков (почему нет)

import requests
import time
import sqlite3

token = '8f68c42072557646091a1b5d80005abddcfc51e7890a39c00b821c444674431cfdb65f267ca2eddf604e6'
group_id = 'iqdevops'

conn = sqlite3.connect('Pages.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS tabl(
    id_page TEXT,
    name TEXT,
    phone TEXT,
    site TEXT,
    likes TEXT);
""")

# Для того чтобы хранить информацию до передачи ее в базу данных, создадим словарь. В качестве ключа мы будем использовать id, так как они все уникальны. Тогда мы будем обращаться к словарю по ключу, если он есть мы поменяем даннные внутри, если его нет - создадим новые.
dict_for_bd = {}


# Функция для скачивания из ВК
def vk_download(method, parameters, token=token):
    url = 'https://api.vk.com/method/' + method + '?' + parameters + '&access_token=' + token + "&v=5.131"
    response = requests.get(url)
    # return (response.json())
    try:
        return (response.json())['response']
    except:
        print('Пожалуйста, обновите токен, для этого воспользуйтесь ссылкой из файла main.py')
        exit()


# Функция для получения информации со страницы человека
def page_download(page_id):
    page_id = str(page_id)
    #Также нам понадобятся параметры скачивания, потому что без них получаемая нами информация только основная, а интересующие нас номер телефона и сайт лежат в расширенной.
    parameters_for_download = '&fields=photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, ' \
                              'photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, ' \
                              'online, domain, has_mobile, contacts, site, education, universities, schools, status, ' \
                              'last_seen, followers_count, common_count, occupation, nickname, relatives, relation, ' \
                              'personal, connections, exports, activities, interests, music, movies, tv, books, ' \
                              'games, about, quotes, can_post, can_see_all_posts, can_see_audio, ' \
                              'can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, ' \
                              'timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, ' \
                              'military, blacklisted, blacklisted_by_me, can_be_invited_group '
    page_info = vk_download('users.get', 'users_ids=' + page_id + parameters_for_download)
    page_info = page_info[0]  # Для начала мы получим словарь
    page_name = page_info['first_name'] + ' ' + page_info['last_name']  # Сохраним имя и фамилию в переменной page_name

    try:  # получить номер телефона и сайт, но если мы его просто будем искать по ключу, то в отсутствие номера мы получим ошибку
        mobile_phone = page_info['mobile_phone']
        if mobile_phone == '':
            mobile_phone = 'None'
    except:
        mobile_phone = 'None'
    try: # с сайтом также
        site = page_info['site']
        if site == '':
            site = 'None'
    except:
        site = 'None'

    # Теперь нам нужно вернуть полученные значения в виде списка
    information_from_page = inform = [page_name, page_id, mobile_phone, site]
    time.sleep(0.5) # проставим небольшую задержку для того, что бы вк пропустил следующий запрос
    return information_from_page

# The Main code
for group_id in group_ids: # чтобы пройти по всем группам лежащим в списке с группами, воспользуемся циклом for
    group_info = vk_download('groups.getById', 'group_id=' + group_id)
    group_name = group_info[0]['name']
    print('Группа:', '"' + group_name + '"')

    # теперь нам нужна стена этой группы. Скачаем записи и сохраним количество постов, которое эта группа уже выложила:
    group_info = vk_download('wall.get', 'domain=' + group_id)
    count_post = group_info['count']

    if count_post >= 50: # Для анализа нам понадобятся последние 50 выложенных постов. Но их там может не быть. Поэтому мы пропустим количество постов через условный оператор. Если их больше 50, то скачаем 50, а если меньше, то те, что есть:
        n = 50
    else:
        n = count_post

    # В новом цикле мы будем проходить по каждой записи и обрабатывать полученную из неё информацию. Так как мы будем обрабатывать только те записи, в которых есть лайки, а проходить все, то мы будем пользоваться циклом while, потому что в цикле for нельзя менять границы цикла
    i, k = 0, 0 # Переменная i понадобится для цикла, а переменная k для счета скачанных записей
    while i < n:
        print('# Запись №', i + 1)
        # Скачивать мы будем по одному посту, поэтому нам понадобится параметр для смещения
        parameter_offset = '&count=1&offset=' + str(i) # count - количество, offset - смещение
        download_note = vk_download('wall.get', 'domain=' + group_id + parameter_offset)

        download_note = download_note['items'][0] # перейдем к полученному словарю
        # мы будем проверять автора. Если id автора такой же как id  группы, то продолжаем обработку (пока поставим pass), а если нет, то увеличииваем n
        if int(download_note['from_id']) == int(download_note['owner_id']):
            id_post = download_note['id']
            id_group = download_note['from_id']
            count_likes = download_note['likes']['count']
            if count_likes != 0: # если количество лайков отлично от нуля, то с помощью цикла for будем по ним проходить и выводить номер лайка
                for j in range(0, count_likes):
                    print('Лайк', j, 'из', count_likes)
                    param_post = '&type=post&owner_id=' + str(id_group) + '&'
                    param_post += 'item_id=' + str(id_post) + '&filter=likes&'
                    param_post += 'extended=1&offset=' + str(j) + '&count=1&v=5.131'
                    post = vk_download('likes.getList', param_post)
                    # сразу перейдем к внутреннему списку записью о лайке и получим оттуда словарь:
                    post = post['items']
                    post = post[0]
                    # получим id страницы пользователя, поставившего лайк и создадим список для хранения в нем информации:
                    id_page = str(post['id'])
                    spis = []
                    if not (dict_for_bd.get(id_page)): # специальная команда, с помощью которой можно узнать есть ли данный ключ в словаре
                        # Так как у нас нет информации по данному ключу, то нам нужно получить информацию и добавить в словарь с заданным ключем
                        page = page_download(id_page)
                        like = 1
                        spis = [page, like]
                        dict_for_bd[id_page] = spis
                    else: # в этом случае у нас есть информация по ключу. Получим её:
                        spis = dict_for_bd[id_page]
                        spis[1] += 1
                        dict_for_bd[id_page] = spis
                    time.sleep(0.5)
                k += 1 # Увеличим счетчик записей на 1
                print('Записей скачано:', k)
            else:
                n += 1
        else:
            n += 1
        i += 1 # у цикла while счетчик сам не увиличивается, то мы будем его менять сами
        time.sleep(0.5) # что бы Вконтакте не ругался на нас проставим задержку

    # Закончили скачивать посты
    print('Группа:', '"' + group_name + '"')
    print('Посты скачаны. Из этой группы скачано: ' + str(k))5
dkeys = dict_for_bd.keys()
for dkey in dkeys:
    spis = dict_for_bd[dkey]
    id_page = spis[0][1]
    name = spis[0][0]
    phone = spis[0][2]
    site = spis[0][3]
    likes = spis[1]
    # Сложим их в отдельный список, добавим его в базу данных и сохраним изменения:
    record = (id_page, name, phone, site, likes)
    cur.execute("INSERT INTO tabl VALUES(?, ?, ?, ?, ?);", record)
    conn.commit()
print('База данных готова.')



