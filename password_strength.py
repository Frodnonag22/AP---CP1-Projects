# Andrew Petersen password checker

import time
import sys

def cool_print(text: str, delay: float = 0.05, end = "\n"):
    for char in text:
        sys.stdout.write(f"{char}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def cool_input(prompt: str, delay: float = 0.05):
  for character in prompt:
    sys.stdout.write(f"{character}")
    sys.stdout.flush()
    time.sleep(delay)
  return input()

def clear_terminal():
    print("\033[H\033[J", end="")

clear_terminal()

while True:
    password = cool_input("What is your password? ")
    if password == "":
        cool_print("You didn't input anything!")
    else:
        break

if password == "49DSwFqyrjSS#":
    cool_print("Bro! That's my password!")

capitals = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for capital in password:
    if capital in capitals:
        cap_in_pass = 1
        break
    else:
        cap_in_pass = 0

lowercases = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for lowercase in password:
    if lowercase in lowercases:
        low_in_pass = 1
        break
    else:
        low_in_pass = 0

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
for number in password:
    if number in numbers:
        num_in_pass = 1
        break
    else:
        num_in_pass = 0

symbols = ["(", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ", ", ".", "<", ">", "?", ")", " "]
for symbol in password:
    if symbol in symbols:
        sym_in_pass = 1
        break
    else:
        sym_in_pass = 0

if len(password) >= 8:
   len_of_pass = 1
else:
   len_of_pass = 0

pass_strength = cap_in_pass + low_in_pass + len_of_pass + num_in_pass + sym_in_pass

cool_print("Password is ", end="")

if pass_strength == 1 or pass_strength == 5:
    cool_print("very ", end="")

if pass_strength == 3:
    cool_print("medium strength.")
elif pass_strength > 3:
    cool_print("strong.")
else:
    cool_print("weak.")