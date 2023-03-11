import subprocess
import time
text = """ $$$$$$\  $$\                             $$\                   $$\                               
$$  __$$\ $$ |                            $$ |                  \__|                              
$$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$\   $$$$$$\$$$$\  $$\ $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |$$$$\ $$  __$$\ $$  __$$\ $$  _____|\_$$  _|  $$  _$$  _$$\ $$ |$$  __$$\ $$  __$$\ $$  __$$\ 
$$ |\_$$ |$$ |  $$ |$$ /  $$ |\$$$$$$\    $$ |    $$ / $$ / $$ |$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$ |  $$ | \____$$\   $$ |$$\ $$ | $$ | $$ |$$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |$$ |  $$ |\$$$$$$  |$$$$$$$  |  \$$$$  |$$ | $$ | $$ |$$ |$$ |  $$ |\$$$$$$$\ $$ |      
 \______/ \__|  \__| \______/ \_______/    \____/ \__| \__| \__|\__|\__|  \__| \_______|\__|"""
print(text)
print("FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE FREE")
print(" ")
print("Made by the team Ghostminer")
print("Discord: https://discord.gg/Rh5R9Dbt7p")
print(" ")
print(" ")

while True:
    print("Press 1 for ETH")
    print("Press 2 for BTC")
    print("Press 3 for LTC")
    print("Press 4 for BNB")
    print("Press q to quit")
    
    user_input = input()
    
    if user_input == "1":
        print("starting...")
        subprocess.call(["python", "eth.py"])
    elif user_input == "2":
        print("To do this action you need to buy Ghostminer Ultra. Join the Discord server to buy: https://discord.gg/Rh5R9Dbt7p")
        time.sleep(5)
    elif user_input == "3":
        print("To do this action you need to buy Ghostminer Ultra. Join the Discord server to buy: https://discord.gg/Rh5R9Dbt7p")
        time.sleep(5)
    elif user_input == "4":
        print("To do this action you need to buy Ghostminer Ultra. Join the Discord server to buy: https://discord.gg/Rh5R9Dbt7p")
        time.sleep(5)
    elif user_input == "q":
        break
    else:
        print("Invalid input")
