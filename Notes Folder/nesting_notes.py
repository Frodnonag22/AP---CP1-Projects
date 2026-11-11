# AP, Nesting Notes

import random as r

win = False
text = True

if win:
    if text:
        print("Hallelujia")
    else:
        print("You suck")
else:
    print("You failed")

i = 0
random = r.randint(1, 10)

while i <= 10:
    print(i)
    i +=1
    j = 0
    while j <= i + random:
        print(j+i)