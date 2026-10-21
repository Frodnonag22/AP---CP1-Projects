# AP Tic-Tac-Toe

import sys
import time

reset = "\033[0m"
green = "\033[32m"
blue = "\033[34m"
magenta = "\033[35m"
yellow = "\033[33m"

#pointless except for comedy

def clear_terminal():
    print("\033[H\033[J", end="")
clear_terminal()

def cool_print(text: str, delay: float):
    for char in text:
        sys.stdout.write(f"{char}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def cool_input(prompt: str, delay: float = 0.05):
  for character in prompt:
    sys.stdout.write(f"{character}")
    sys.stdout.flush()
    time.sleep(delay)
  return input()

# now the real stuff begins

# DAN - This is how my typer works and how you can use it for inputs

combos = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

board = f"       │       │\n   {choices[0]}   │   {choices[1]}   │   {choices[2]}\n       │       │\n───────┼───────┼───────\n       │       │\n   {choices[3]}   │   {choices[4]}   │   {choices[5]}\n       │       │\n───────┼───────┼───────\n       │       │\n   {choices[6]}   │   {choices[7]}   │   {choices[8]}\n       │       │"
cool_print(board, 0.01)

play_again = True

player = 1

while play_again:
    taken = []
    condition = 1
    for condition in range(1, 10):
        end = "no"
        while end != "yes":
            while True:
                try:
                        choice = int(cool_input("Which slot would you like to pick (1 - 9): "))
                except:
                    print(f"Thats not a valid number!")
                else:
                    break
            if choice in taken:
                print("Slot is already taken")
            elif choice <= 0:
                print("Input must be 1 - 9")
            elif choice >= 10:
                print("Input must be 1 - 9")
            else:
                taken.append(choice)
                choices.remove(choice)
                if player % 2 == 1:
                    choices.insert(choice-1, f"{green}X{reset}")
                    player += 1
                else:
                    player += 1
                    choices.insert(choice-1, f"{blue}O{reset}")
                
                board = f"       │       │\n   {choices[0]}   │   {choices[1]}   │   {choices[2]}\n       │       │\n───────┼───────┼───────\n       │       │\n   {choices[3]}   │   {choices[4]}   │   {choices[5]}\n       │       │\n───────┼───────┼───────\n       │       │\n   {choices[6]}   │   {choices[7]}   │   {choices[8]}\n       │       │"
                break
        clear_terminal()
        cool_print(board, 0.01)
        if choices[0] == f"{green}X{reset}" and choices[1] == f"{green}X{reset}" and choices[2] == f"{green}X{reset}" or choices[3] == f"{green}X{reset}" and choices[4] == f"{green}X{reset}" and choices[5] == f"{green}X{reset}" or choices[6] == f"{green}X{reset}" and choices[7] == f"{green}X{reset}" and choices[8] == f"{green}X{reset}" or choices[0] == f"{green}X{reset}" and choices[3] == f"{green}X{reset}" and choices[6] == f"{green}X{reset}" or choices[1] == f"{green}X{reset}" and choices[4] == f"{green}X{reset}" and choices[7] == f"{green}X{reset}" or choices[2] == f"{green}X{reset}" and choices[5] == f"{green}X{reset}" and choices[8] == f"{green}X{reset}" or choices[0] == f"{green}X{reset}" and choices[4] == f"{green}X{reset}" and choices[8] == f"{green}X{reset}" or choices[2] == f"{green}X{reset}" and choices[4] == f"{green}X{reset}" and choices[6] == f"{green}X{reset}":
            print(f"{yellow}X Won!{reset}")
            break
        elif choices[0] == f"{blue}O{reset}" and choices[1] == f"{blue}O{reset}" and choices[2] == f"{blue}O{reset}" or choices[3] == f"{blue}O{reset}" and choices[4] == f"{blue}O{reset}" and choices[5] == f"{blue}O{reset}" or choices[6] == f"{blue}O{reset}" and choices[7] == f"{blue}O{reset}" and choices[8] == f"{blue}O{reset}" or choices[0] == f"{blue}O{reset}" and choices[3] == f"{blue}O{reset}" and choices[6] == f"{blue}O{reset}" or choices[1] == f"{blue}O{reset}" and choices[4] == f"{blue}O{reset}" and choices[7] == f"{blue}O{reset}" or choices[2] == f"{blue}O{reset}" and choices[5] == f"{blue}O{reset}" and choices[8] == f"{blue}O{reset}" or choices[0] == f"{blue}O{reset}" and choices[4] == f"{blue}O{reset}" and choices[8] == f"{blue}O{reset}" or choices[2] == f"{blue}O{reset}" and choices[4] == f"{blue}O{reset}" and choices[6] == f"{blue}O{reset}":
            print(f"{yellow}O Won!{reset}")
            break
        elif condition == 9:
            print(f"{magenta}It's a draw!{reset}")
        else:
            pass
    end = "no"
    time.sleep(5)
    while end != "yes":
        clear_terminal()
        while True:
            try:
                pa_input = int(input(f"Would you like to play again (1: yes, 2: no)? "))
            except:
                print("Invalid input")
            else:
                clear_terminal()
                break
        if pa_input >= 3:
            print("Invalid input, try again")
        elif pa_input <= 0:
            print("Invalid input, try again")
        else:
            end = "yes"
    if pa_input == 2:
        print(f"Play again sometime!", 0.2)
        play_again = False
    else:
        for i in range(11):
            print("Rebooting game", end="")
            cool_print("...", 0.25)
            clear_terminal()
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        board = f"       │       │\n   {choices[0]}   │   {choices[1]}   │   {choices[2]}\n       │       │\n───────┼───────┼───────\n       │       │\n   {choices[3]}   │   {choices[4]}   │   {choices[5]}\n       │       │\n───────┼───────┼───────\n       │       │\n   {choices[6]}   │   {choices[7]}   │   {choices[8]}\n       │       │"
        cool_print(board, 0.01)

clear_terminal()