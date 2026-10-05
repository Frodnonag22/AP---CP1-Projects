# AP Tic-Tac-Toe

import sys
import time

reset = "\033[0m"
green = "\033[32m"
blue = "\033[34m"
magenta = "\033[35m"
yellow = "\033[33m"

#pointless except for comedy

def cool_print(text: str, delay: float):
    """Prints text character by character cycling through an RGB color wheel."""
    # Custom 24-bit RGB neon spectrum
    colors = [(255, 255, 255)]
    
    for i, char in enumerate(text):
        r, g, b = colors[i % len(colors)]
        # Construct dynamic 24-bit color string
        color_code = f"\033[1;38;2;{r};{g};{b}m"
        
        sys.stdout.write(f"{color_code}{char}")
        sys.stdout.flush()
        time.sleep(delay)
        
    print(reset)

# now the real stuff begins

combos = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

board = f"       │       │\n   {choices[0]}   │   {choices[1]}   │   {choices[2]}\n       │       │\n───────┼───────┼───────\n       │       │\n   {choices[3]}   │   {choices[4]}   │   {choices[5]}\n       │       │\n───────┼───────┼───────\n       │       │\n   {choices[6]}   │   {choices[7]}   │   {choices[8]}\n       │       │"
print(board)

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
                        choice = int(input("Which slot would you like to pick (1 - 9): "))
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
        print(board)
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
    while end != "yes":
        while True:
            try:
                pa_input = int(input(f"Would you like to play again (1: yes, 2: no)? "))
            except:
                print("Invalid input")
            else:
                break
        if pa_input >= 3:
            print("Invalid input, try again")
        elif pa_input <= 0:
            print("Invalid input, try again")
        else:
            end = "yes"
    if pa_input == 2:
        cool_print(f"Bruh...", 1)
        play_again = False
    else:
        print("Rebooting game", end="")
        cool_print("...", 1)
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        board = f"       │       │\n   {choices[0]}   │   {choices[1]}   │   {choices[2]}\n       │       │\n───────┼───────┼───────\n       │       │\n   {choices[3]}   │   {choices[4]}   │   {choices[5]}\n       │       │\n───────┼───────┼───────\n       │       │\n   {choices[6]}   │   {choices[7]}   │   {choices[8]}\n       │       │"
        print(board)