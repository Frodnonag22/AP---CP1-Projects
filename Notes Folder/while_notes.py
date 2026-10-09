# AP While Notes
# while loop will keep running until a condition is met
import random
import time
# 3 parts of loop
goose = random.randint(1, 20)
duck = 1 # 1: start point. Usualy outside of the loop

while goose > duck: # 2: end point. It tells us when to end
    print("duck. . .")
    time.sleep(0.1)
    duck += 1 # 3: Incramenter. Used to change your iterator. Iterator is keeping track of the current iteration if the loop.
    if duck == 15:
        print("Game over")
        break
else: # only happens when the loop ends naturally, "break" will not do the else at the bottom
    print("GOOSE")


count = 30

while count >= 1:
    print(count)
    time.sleep(0.1)
    count -= 1


number = random.randint(1, 101)

while True:
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < 0 or guess > 100:
                print("You should read the instructions")
                continue # starts the next iteration immediately (restarts the loop)
            break # exits the loop
        except:
            print("That isn't a number")
    if guess == number:
        print("You win!")
        break
    elif guess < number:
        print("That number is too low")
    elif guess > number:
        print("That number is too high")
    else:
        print("Idk how you got here. . . but you did something wrong")