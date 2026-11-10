# AP Turtle racing

# Importing libraries for the code
import turtle as t
import time
import random as r

def clear_terminal():
    """Clears the terminal"""
    print("\033[H\033[J", end="")

def race_setup():
    """"Sets up the race"""
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

def finish_line():
    """Draws the finish line"""
    f_line.goto(500, 400)
    f_line.hideturtle()
    f_line.color("white")
    f_line.down()
    f_line.goto(500, -400)
    f_line.hideturtle()
    f_line.color("black")

def draw_three(color):
    """Draws a three in the turtle thing"""
    three.color(f"{color}")
    three.penup()
    three.goto(-20, 50)
    three.pendown()
    three.circle(-30, 180)
    three.circle(-30, 180)

def draw_two():
    """Draws a two in the turtle thing"""
    two.goto(0, 0)
    two.circle(-40, 180)
    two.goto(t.xcor() - 80, t.ycor() - 80)
    two.forward(80) 

def draw_one(color):
    """Draws a one in the turtle thing"""
    one.color(f"{color}")
    one.penup()
    one.goto(0, 0)
    one.pendown()
    one.left(90)
    one.forward(100)
    one.left(135)
    one.forward(30)

# Creates all of the turtles
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

one = t.Turtle()
two = t.Turtle()
three = t.Turtle()

one.color("White")
one.penup()
one.goto(0, 0)
one.pendown()
one.left(90)
one.forward(100)
one.left(135)
one.forward(30)

clear_terminal() # Clearing the terminal for a more satisfying look

racer = 1 # Creates the variable that lets the code detect the winner
race_in_progress = True # Lets the while loop and the for loop break at the same time
while race_in_progress:
    for c in (red, orange, yellow, green, blue, indigo, purple):
        distance = r.randint(1, 50)
        c.fd(distance)
        if c.xcor() >= 500: # Check for each color winning
            if racer % 7 == 1:
                print("Red won!")
            elif racer % 7 == 2:
                print("Orange won!")
            elif racer % 7 == 3:
                print("Yellow won!")
            elif racer % 7 == 4:
                print("Green won!")
            elif racer % 7 == 5:
                print("Blue won!")
            elif racer % 7 == 6:
                print("Indigo won!")
            else:
                print("Purple won!")
            race_in_progress = False
            break
        racer += 1

t.exitonclick() # Exits the turtle on click

time.sleep(5) # lets the user see the winner before ending the code
clear_terminal() 