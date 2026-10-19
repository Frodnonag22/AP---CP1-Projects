# AP Escape Room

import random
import time
import sys
import os

red = "\033[38;5;196m"
orange = "\033[38;5;208m"
yellow = "\033[38;5;226m"
yel_green = "\033[38;5;118m"
green = "\033[38;5;46m"
cyan = "\033[38;5;51m"
blue = "\033[38;5;21m"
purple = "\033[38;5;129m"
magenta = "\033[38;5;201m"
pink = "\033[38;5;213m"
black = "\033[38;5;16m"
reset = "\033[0m"
bold ="\033[1m"

code_list = []
for i in range(1,7):
    letter = random.randint(0,26)
    code_digits = "qwertyuiopasdfghjklzxcvbnm"
    code_letter = code_digits[letter: letter+1]
    code_list.append(code_letter)

int_list = []
for i in range(0,3):
    number = random.randint(0,10)
    code_int = "1234567890"
    code_number = code_int[number: number+1]
    int_list.append(code_number)

code = f"{code_list[0]}{code_list[1]}{code_list[2]}{code_list[3]}{code_list[4]}{code_list[5]}{int_list[0]}{int_list[1]}{int_list[2]}"

def cool_print(text: str, delay: float):
    for i, character in enumerate(text):
        sys.stdout.write(f"{character}") # prints one character at a time
        sys.stdout.flush() # makes sure that the text doesnt print all at once
        time.sleep(delay) # delays time between each character print
    print() # makes it so that the next line is actuall on the next line

def cool_input(prompt: str, delay: float):
  for character in prompt:
    sys.stdout.write(f"{character}")
    sys.stdout.flush()
    time.sleep(delay)
  return input()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

time.sleep(1)

playing = True

while playing:
    cool_print(f"{green}Welcome. . . user. . . ", 0.1)
    name = cool_input("What is your name: ", 0.1)
    cool_print(f"You are trapped within my escape room. . . {red}{name}{green}", 0.1)
    cool_print("You have 10 guesses to get my code. . .", 0.1)
    if "Admin" in name:
        cool_print(f"Since you are the admin, you get the code. . .", 0.1)
        cool_print(f"The code is. . . {code}", 0.1)
    guess = cool_input(f"The code is 9 digits. . . 6 letters. . . 3 numbers. . . {red}What is the code: {cyan}", 0.1).strip()
    print(reset, end="")

    guess_number = 0

    while guess_number <= 10:
        if guess == code:
            cool_print(f"{green}Congradulations. . . You won. . .{reset}", 0.1)
            break
        else:
            cool_print(f"{red}Incorrect. . . {reset}", 0.1)
            if guess_number == 9:
                cool_print(f"{green}You have been given the code. . .{reset}", 0.1)
                guess = cool_input(f"{red}Final guess. . . {cyan}", 0.1)
            else:
                cool_print(f"{green}Hint #{guess_number+1}: The #{guess_number+1} digit is {code[guess_number: guess_number+1]}{reset}", 0.1)
                guess = cool_input(f"{red}Try again. . . {cyan}", 0.1).strip()
            guess_number += 1
    else:
        cool_print(f"{red}You. . . lost. . .", 0.1)
        cool_print(f"You will be traped here forever. . . . Good. . . bye. . .", 0.1)
        cool_print(f"Unless. . .", 0.1)
        time.sleep(1)
        cool_print(f"You run the code again. . .{red}", 0.1)
    time.sleep(1)
    clear_terminal()
    print(f"""{red}
    ______                        ____                 
    / ____/___ _____ ___  ___     / __ \_   _____  _____
    / / __/ __ `/ __ `__ \/ _ \   / / / / | / / _ \/ ___/
    / /_/ / /_/ / / / / / /  __/  / /_/ /| |/ /  __/ /    
    \____/\__,_/_/ /_/ /_/\___/   \____/ |___/\___/_/     

    """)
    time.sleep(2)

    play_again = input("""
        ____  __               ___               _     ___ 
    / __ \/ /___ ___  __   /   | ____ _____ _(_)___/__ \ 
    / /_/ / / __ `/ / / /  / /| |/ __ `/ __ `/ / __ \/ _/
    / ____/ / /_/ / /_/ /  / ___ / /_/ / /_/ / / / / /_/  
    /_/   /_/\__,_/\__, /  /_/  |_\__, /\__,_/_/_/ /_(_)   
                /____/         /____/                    """).lower()

    if "ye" in play_again:
        playing = True
    else:
        playing = False