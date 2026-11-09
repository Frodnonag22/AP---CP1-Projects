# AP Turtle racing

import turtle as t
import time
import random as r

f_line = t.Turtle()
red = t.Turtle()
orange = t.Turtle()
yellow = t.Turtle()
green = t.Turtle()
blue = t.Turtle()
indigo = t.Turtle()
purple = t.Turtle()
bg = t.Screen()

bg.bgcolor("black")


red.goto(-500, 300)
red.shape("turtle")
red.color("red")
orange.goto(-500, 200)
orange.shape("turtle")
orange.color("orange")
yellow.goto(-500, 100)
yellow.shape("turtle")
yellow.color("yellow")

green.goto(-500, 0)
green.shape("turtle")
green.color("green")

blue.goto(-500, -100)
blue.shape("turtle")
blue.color("blue")
indigo.goto(-500, -200)
indigo.shape("turtle")
indigo.color("indigo")
purple.goto(-500, -300)
purple.shape("turtle")
purple.color("purple")

f_line.goto(500, 400)
f_line.color("white")
f_line.down()
f_line.goto(500, -400)
f_line.hideturtle()
f_line.color("black")
f_line.goto(-500,0)

racer = 1
race_in_progress = True
while race_in_progress:
    for c in (red, orange, yellow, green, blue, indigo, purple):
        distance = r.randint(1, 50)
        c.fd(distance)
        if c.xcor() >= 500:
            if racer % 7 == 0:
                print("Red won!")
            elif racer % 7 == 1:
                print("Orange won!")
            elif racer % 7 == 2:
                print("Yellow won!")
            elif racer % 7 == 3:
                print("Green won!")
            elif racer % 7 == 4:
                print("Blue won!")
            elif racer % 7 == 5:
                print("Indigo won!")
            else:
                print("Purple won!")
            race_in_progress = False
            break
    racer += 1

t.exitonclick()