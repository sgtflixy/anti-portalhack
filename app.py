import random
import time
import os
import subprocess

def generate():
    key = ''
    portion = ''
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for _ in range(16):  # Generate 16 characters for a complete key
        character = random.choice(characters)
        key += character
        portion += character
        if len(portion) == 4 and len(key) < 16:
            key += '-'
            portion = ''
    return key

delay = float(input("[ 1 ] ~ Enter the time between requests (0 for fastest) -> "))
times = int(input("[ 2 ] ~ How many times to repeat requests (0 for inf) -> "))
save = "0"
possible = ["y", "Y", "N", "n", ""]

while save not in possible:
    os.system("cls")
    print(f"[ 1 ] ~ Enter the time between requests -> {delay}")
    print(f"[ 2 ] ~ How many times to repeat requests (0 for inf) -> {times}")
    save = input("[ 3 ] ~ Save to txt y/n (Default Y) -> ")

save = save.lower() in ('y', '')
counter = 1
file_path = 'results.txt'

if times == 0:
    while True:
        key = generate()
        # Properly capture curl output
        result = subprocess.getoutput(f'curl -s "https://portalhax.online/PORTAL-FIRMWARE-FLASHER/check-license.php?key={key}"')
        
        if save:
            with open(file_path, 'a' if os.path.exists(file_path) else 'w') as f:
                f.write(result + "\n")
        
        print(f"[ {counter} ] - Key: {key} - Response: {result}")
        if delay > 0:
            time.sleep(delay)
        counter += 1
else:
    for _ in range(times):
        key = generate()
        # Properly capture curl output
        result = subprocess.getoutput(f'curl -s "https://portalhax.online/PORTAL-FIRMWARE-FLASHER/check-license.php?key={key}"')
        
        if save:
            with open(file_path, 'a' if os.path.exists(file_path) else 'w') as f:
                f.write(result + "\n")
        
        print(f"[ {counter} ] - Key: {key} - Response: {result}")
        if delay > 0:
            time.sleep(delay)
        counter += 1
