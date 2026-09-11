# Andrew Petersen Dice Roller

import random

play = True
roll_number = 1

print(f"WARNING: IF YOU TRY TO ROLL ANYTHING OTHER THAN A VALID DICE, IT WILL NOT WORK")
print(f"WARNING: PLEASE DO NOT ROLL TOO MANY DICE")

while play == True:
    while True:
        try:
            dice_rolled = int(input(f"What dice would you like to roll? (Traditional D&D dice, D4, D6, D8, D10, D12, D20. If you want a D100, just roll 2 D10s): D"))
        except:
            print("Thats not a valid number!")
        else:
            break

    while True:
        try:
            times_rolled = int(input(f"How many D{dice_rolled}s would you like to roll? "))
        except:
            print("Thats not a valid number!")
        else:
            break
    if dice_rolled == 10 and times_rolled == 2:
        print(f"D100 roll was: {random.randint(1, 100)}")
    elif dice_rolled == 20 or dice_rolled == 12 or dice_rolled == 10 or dice_rolled == 8 or dice_rolled == 6 or dice_rolled == 4:
        while roll_number < times_rolled + 1:
            print(f"roll number {roll_number} was: {random.randint(1, dice_rolled)}")
            roll_number += 1
    else:
        print(f"Input Error: D{dice_rolled} was not a valid dice")

    play_again = input(f"Would you like to play again? ").strip().title()
    if play_again == "Yes" or play_again  == "Sure":
        print("Here you go:")
        roll_number = 1
    else:
        print(f"Ok, have a good day. ")
        play = False