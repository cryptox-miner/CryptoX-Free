import subprocess
import time
import colorama
from colorama import Fore, Style
text = """ 
 ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ██╗  ██╗    ███████╗████████╗██╗  ██╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗╚██╗██╔╝    ██╔════╝╚══██╔══╝██║  ██║
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║ ╚███╔╝     █████╗     ██║   ███████║
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║ ██╔██╗     ██╔══╝     ██║   ██╔══██║
╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██╔╝ ██╗    ███████╗   ██║   ██║  ██║
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝
                                                                                        """
print(text)
print(f"{Fore.RED}FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE")
print(" ")
print(f"Made by the Crypto X team")
print(f"{Fore.BLUE}Discord: discord.gg/jPJgrkVADW")
print(" ")
print(" ")

while True:
    print(f"{Fore.GREEN}Press 1 for ETH")
    print(f"{Fore.RED}Press 2 for BTC")
    print(f"{Fore.RED}Press 3 for LTC")
    print(f"{Fore.RED}Press 4 for BNB")
    print(f"{Fore.RED}Press q to quit")
    
    user_input = input()
    
    if user_input == "1":
        print(f"{Fore.GREEN}Starting...")
        subprocess.call(["python", "eth.py"])
    elif user_input == "2":
        print(f"{Fore.RED}To do this action you need to buy Ghostminer Ultra. Join the Discord server to buy: discord.gg/jPJgrkVADW")
        time.sleep(5)
    elif user_input == "3":
        print(f"{Fore.RED}To do this action you need to buy Ghostminer Ultra. Join the Discord server to buy: discord.gg/jPJgrkVADW")
        time.sleep(5)
    elif user_input == "4":
        print(f"{Fore.RED}To do this action you need to buy Ghostminer Ultra. Join the Discord server to buy: discord.gg/jPJgrkVADW")
        time.sleep(5)
    elif user_input == "q":
        break
    else:
        print("Invalid input")
