# Andrew Petersen Fix the game

import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        while True:
            try:
                guess = int(input("Guess a number between 1 and 20: ")) # Stupid proofing
            except:
                print("Thats not a valid number!")
            else:
                break
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

        if guess == secret_number: # Missing colon. Original code: if guess == secret_number. Syntax error. No colon, no run
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
print("Your guesses per round: ", scores) # Replaced "+" with ",". Original code: print("Your guesses per round: " + scores). Runtime error. Wouldn't print the list properly because it thought it was trying to add the list to the string

total = 0
for score in scores:
    """total = 0""" # Remove total = 0. Original code: total = 0. Logic Error. Kept resetting total to 0 so the score wasnt included
    total = total + score

average = total / rounds
print("Your average guesses per round was " + str(round(average, 2))) # Made user friendly

best_round = scores[0]
for i in range(1, rounds): # Remove "-1". Original code: for i in range(1, rounds - 1):. Logic Error, wouldn't inclue the last round as part of the best score
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")