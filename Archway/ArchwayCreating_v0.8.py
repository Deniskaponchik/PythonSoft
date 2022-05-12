#!/usr/bin/python

import subprocess
import datetime 
from pexpect import *
import sys
import random
import json
import requests
import time
from time import sleep
from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
import csv


#ARCHWAY_VALOPER = sys.argv[1]
NUMBER_ACCOUNT = sys.argv[1]
MAIN_ACCOUNT = "archway1fg93ekk3mzrq7qcuq2grfps9j72ju39kfcqa02"
#MAIN_ACCOUNT = "archway1mdlzc9wg5806guru66xm8x3kvtfqhawkmu47q7"
#NEW_ADDRESS = "archway1fg93ekk3mzrq7qcuq2grfps9j72ju39kfcqa02"
#ARCHWAY_WALLET = sys.argv[2]
#PASSWORD = sys.argv[3]
PASSWORD = "D@n987654321"
#start = 17
START_COUNT = int(sys.argv[1])
END_COUNT = int(sys.argv[2])
#end = 18


HEADER = ['keys add', 'Name', 'deniskaponchik2', 'archwayd tx', 'NEW_ADDRESS', 'MAIN_ACCOUNT', 'Send torii', 'Coins', 'valoper', 'mnemonic']

def processing_loop(csvfile):
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(HEADER)

    START_COUNT = int(sys.argv[1])
    END_COUNT = int(sys.argv[2])

    while START_COUNT <= END_COUNT:
#      print(START_COUNT)
       START_COUNT += 1
       print()
       NEW_NAME = "deniska"+NUMBER_ACCOUNT

#      csv_writer.writerow([light, voltage])
       csv_writer.writerow(['archwayd keys add', NEW_NAME, '', 'archwayd tx bank send', '', '', '', 0, '', '' ])
       csvfile.flush()
       time.sleep(1)


START_COUNT = int(sys.argv[1])
END_COUNT = int(sys.argv[2])
CSV_NAME = f"results_{START_COUNT}_{END_COUNT}.csv"
#with open('results.csv', 'w') as csvfile:
with open(CSV_NAME, 'w') as csvfile:
   processing_loop(csvfile)


"""
# Create Account
   cmd = f"archwayd keys add deniska"+NUMBER_ACCOUNT+" --output json"
   child = spawn(cmd, timeout=5, encoding='utf-8')
   child.expect('Enter keyring passphrase:')
   child.sendline(PASSWORD)
   ca = json.loads(child.read())
   NEW_NAME = ca['name']
   NEW_ADDRESS = ca['address']
   NEW_MNEMONIC = ca['mnemonic']
   print(NEW_NAME)
   print(NEW_ADDRESS)
   print(NEW_MNEMONIC)


# FAUCET
#  username = 'archway1fg93ekk3mzrq7qcuq2grfps9j72ju39kfcqa02'
   VK_ROOT_URL = "https://faucet.torii-1.archway.tech/ui/"
   opts = FirefoxOptions()
   opts.add_argument("--headless")
   driver = webdriver.Firefox(options=opts)
   driver.get(VK_ROOT_URL)
   account_field = driver.find_element(By.ID, "address")
#  account_field.send_keys(username)
   account_field.send_keys(NEW_NAME)
   sleep(5)
   login_button = driver.find_element(By.ID, "submit-btn")
   login_button.click()
   print('Tokens has been claimed')
   sleep(600)


# Send tokens. WORK !!!
#archwayd tx bank send archway1mdlzc9wg5806guru66xm8x3kvtfqhawkmu47q7 archway1fg93ekk3mzrq7qcuq2grfps9j72ju39kfcqa02 5999989utorii --fees 0utorii --chain-id torii-1 -y
#archwayd tx bank send archway1fg93ekk3mzrq7qcuq2grfps9j72ju39kfcqa02 archway1mdlzc9wg5806guru66xm8x3kvtfqhawkmu47q7 1utorii --fees 0utorii --chain-id torii-1 -y --output json
   cmd = f"archwayd tx bank send "+NEW_ADDRESS+" "+MAIN_ACCOUNT+" 1utorii --fees 0utorii --chain-id torii-1 -y --output json"
   print(cmd)
   child = spawn(cmd, timeout=5, encoding='utf-8')
   child.expect('Enter keyring passphrase:')
   child.sendline(PASSWORD)
   ca = json.loads(child.read())
   TX_HASH = ca['txhash']
   print(TX_HASH)
   print()


else:
   print('THE END')
"""

"""
def get_balance():
    #data = subprocess.check_output(f"archwayd q bank balances {ARCHWAY_WALLET} --output json", shell=True, encodin>
    #data1 =  json.loads(data)
    data = json.loads(subprocess.check_output(f"archwayd q bank balances {ARCHWAY_WALLET} --output json", shell=Tru>
    balance1 = data['balances']
    balance2 = data['pagination']
    return [balance1, balance2]
def get_balance():
    data = json.loads(subprocess.check_output(f"archwayd q bank balances {ARCHWAY_WALLET} --output json", shell=Tru>
    balance1 = data[0]["amount"]
    balance2 = data[1]["total"]
    return [balance1, balance2]
values = get_balance()
print(values[0])
print(values[1])
"""
"""
# delegate. WORK !!!
cmd = f"archwayd tx staking delegate archwayvaloper1fg93ekk3mzrq7qcuq2grfps9j72ju39kfuflzr 1utorii --from archway1f>
child = spawn(cmd, timeout=5, encoding='utf-8')
child.expect('Enter keyring passphrase:')
child.sendline(PASSWORD)
ca1 = json.loads(child.read())
print(ca1['height'])
"""











"""
def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def delegate():
    cmd = f"archwayd tx staking delegate {ARCHWAY_VALOPER} 2000000utorii --from {ARCHWAY_WALLET} --fees 500utorii"
    child = spawn(cmd, timeout=5, encoding='utf-8')
    child.expect('(?i)pass')
    child.sendline(PASSWORD)
    print(child.after)
    time.sleep(1)
    child.sendline('y')
    child.interact()

def claim_commision():
    cmd = f"archwayd tx distribution withdraw-rewards {ARCHWAY_VALOPER} --from {ARCHWAY_WALLET} --commission --fees 100utorii -y"
    child = spawn(cmd, timeout=5, encoding='utf-8')
    child.expect('(?i)pass')
    child.sendline(PASSWORD)
    print(child.after)
    child.interact()

def claim_reward():
    cmd = f"archwayd tx distribution withdraw-all-rewards --from {ARCHWAY_WALLET} --fees 100utorii -y"
    child = spawn(cmd, timeout=5, encoding='utf-8')
    child.expect('(?i)pass')
    child.sendline(PASSWORD)
    print(child.after)
    child.interact()

print("🐲  Script auto-delegate."
      " Telegram channel: https://t.me/icodragondev\n"
      "Please subscribe to our telegram channel.\n"
      "Coder: https://t.me/icodragon")
"""


"""
while True:
    print(datetime.datetime.now(), '🔴 --> Send request get commision.')
    claim_commision()
    time.sleep(random.randint(60, 70))
    print(datetime.datetime.now(), '🔴 --> Send request get reward.')
    claim_reward()
    time.sleep(random.randint(60, 70))
    balance = get_balance()
    if check_int(balance)        if int(balance) >= 2000000:
            print(datetime.datetime.now(), '🟢 --> Send request delegate.')
            delegate()
            time.sleep(random.randint(60, 70))
        else:
            print(2000000 - int(balance), 'tokens left till delegate.')
"""
