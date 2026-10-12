# AP Escape Room

import time
import sys

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

def cool_print(text: str, delay: float):
    for i, character in enumerate(text):
        sys.stdout.write(f"{character}") # prints one character at a time
        sys.stdout.flush() # makes sure that the text doesnt print all at once
        time.sleep(delay) # delays time between each character print
    print() # makes it so that the next line is actuall on the next line

time.sleep(2.5)

cool_print(f"{green}Welcome. . . user. . . ", 0.1)
cool_print("You are trapped within my escape room. . .", 0.1)
cool_print("You have 10 guesses to get my code. . .", 0.1)

guess = 0
while guess < 10:
    cool_print("dsfsasa", 0.1)