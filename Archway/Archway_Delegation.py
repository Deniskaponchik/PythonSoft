#!/usr/bin/python

import subprocess
import time
import datetime
from pexpect import *
import sys
import random

ARCHWAY_VALOPER = sys.argv[1]
ARCHWAY_WALLET = sys.argv[2]
PASSWORD = sys.argv[3]

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def get_balance():
    data = subprocess.check_output(f"archwayd q bank balances {ARCHWAY_WALLET}", shell=True, encoding='cp437')
    return data.split('\n')[1]\
        .replace('"', '')\
        .replace('-', '')\
        .replace(':', '')\
        .replace('amount', '').strip()


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
while True:
    print(datetime.datetime.now(), '🔴 --> Send request get commision.')
    claim_commision()
    time.sleep(random.randint(60, 70))
    print(datetime.datetime.now(), '🔴 --> Send request get reward.')
    claim_reward()
    time.sleep(random.randint(60, 70))
    balance = get_balance()
    if check_int(balance):
        if int(balance) >= 2000000:
            print(datetime.datetime.now(), '🟢 --> Send request delegate.')
            delegate()
            time.sleep(random.randint(60, 70))
        else:
            print(2000000 - int(balance), 'tokens left till delegate.')
