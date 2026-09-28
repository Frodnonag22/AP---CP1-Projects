# AP, Elif and logical Operators Notes

age = 17
licence = False

if age >= 18: # all conditionals begin with an "if"
    print("Ur an adult")
elif age >= 15 and licence: # in between, lets you add another condition. you can have as many as you want.
    print("You can drive :)")
elif age >= 15 and not licence:
    print("You could drive... but you haven't done the paperwork :( GO TO SCHOOL")
else: # marks the end of a conditional 
    print("Ur a miner")

# 3 logical Operators
# AND both must be True
# OR one must be True
# NOT it isn't True

win = False
hp = 0.9

if win or hp <= 0:
    print("Game is over")
    if hp > 0:
        pass # pass is placeholder
    else:
        print("You died :(")
else:
    print("The game is still going")