#!/usr/bin/python

import subprocess
import datetime 
from pexpect import *
import sys
import random
import json
import requests
import time

#ARCHWAY_VALOPER = sys.argv[1]
NUMBER_ACCOUNT = sys.argv[1]
MAIN_ACCOUNT = "archway1fg93ekk3mzrq7qcuq2grfps9j72ju39kfcqa02"
#MAIN_ACCOUNT = "archway1mdlzc9wg5806guru66xm8x3kvtfqhawkmu47q7"
#NEW_ADDRESS = "archway1fg93ekk3mzrq7qcuq2grfps9j72ju39kfcqa02"
#ARCHWAY_WALLET = sys.argv[2]
#PASSWORD = sys.argv[3]
PASSWORD = "D@n987654321"



"""
def get_balance():
    #data = subprocess.check_output(f"archwayd q bank balances {ARCHWAY_WALLET} --output json", shell=True, encoding='cp437')
    #data1 =  json.loads(data)
    data = json.loads(subprocess.check_output(f"archwayd q bank balances {ARCHWAY_WALLET} --output json", shell=True, encoding='cp437'))
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
cmd = f"archwayd tx staking delegate archwayvaloper1fg93ekk3mzrq7qcuq2grfps9j72ju39kfuflzr 1utorii --from archway1fg93ekk3mzrq7qcuq2grfps9j72ju39kfcqa02 --fees 1utorii -y --chain-id torii-1 --output json"
child = spawn(cmd, timeout=5, encoding='utf-8')
child.expect('Enter keyring passphrase:')
child.sendline(PASSWORD)
ca1 = json.loads(child.read())
print(ca1['height'])
"""
"""
# Create account. WORK!!!
cmd = f"archwayd keys add deniskaponchiktest"+NUMBER_ACCOUNT+" --output json"
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
"""


"""
def claim_faucet():
while True:
   creating_account()
   add_csv()
   response = requests.get(https://faucet.torii-1.archway.tech/ui/)
   time.sleep(300)
   send_tokens()
#  delegate()
"""



"""
# Send tokens. WORK !!!
#archwayd tx bank send archway1mdlzc9wg5806guru66xm8x3kvtfqhawkmu47q7 archway1fg93ekk3mzrq7qcuq2grfps9j72ju39kfcqa02 5999989utorii --fees 0utorii --chain-id torii-1 -y
#archwayd tx bank send archway1fg93ekk3mzrq7qcuq2grfps9j72ju39kfcqa02 archway1mdlzc9wg5806guru66xm8x3kvtfqhawkmu47q7 1utorii --fees 0utorii --chain-id torii-1 -y --output json
cmd = f"archwayd tx bank send "+NEW_ADDRESS+" "+MAIN_ACCOUNT+" 1utorii --fees 0utorii --chain-id torii-1 -y --output json"
child = spawn(cmd, timeout=5, encoding='utf-8')
child.expect('Enter keyring passphrase:')
child.sendline(PASSWORD)
ca = json.loads(child.read())
TX_HASH = ca['txhash']
#ADDRESS = ca['address']
#MNEMONIC = ca['mnemonic']
print(TX_HASH)
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
