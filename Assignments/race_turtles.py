# AP Turtle racing

# Importing libraries for the code
import turtle as t
import random as r

def clear_terminal():
    """Clears the terminal"""
    print("\033[H\033[J", end="")

def race_setup():
    """"Sets up the race"""
    red.goto(-1000, 300)
    red.shape("turtle")
    red.color("red")
    red.fd(500)
    orange.goto(-1000, 200)
    orange.shape("turtle")
    orange.color("orange")
    orange.fd(500)
    yellow.goto(-1000, 100)
    yellow.shape("turtle")
    yellow.color("yellow")
    yellow.fd(500)
    green.goto(-1000, 0)
    green.shape("turtle")
    green.color("green")
    green.fd(500)
    blue.goto(-1000, -100)
    blue.shape("turtle")
    blue.color("blue")
    blue.fd(500)
    indigo.goto(-1000, -200)
    indigo.shape("turtle")
    indigo.color("indigo")
    indigo.fd(500)
    purple.goto(-1000, -300)
    purple.shape("turtle")
    purple.color("purple")
    purple.fd(500)

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
    three.hideturtle()
    three.color(color)
    three.seth(0)
    three.penup()
    three.goto(-20, 50)
    three.pendown()
    three.right(50)
    three.circle(30, 240)
    three.left(180)
    three.circle(30, 240)
    three.right(180)

def draw_two(color):
    """Draws a two in the turtle thing"""
    two.hideturtle()
    two.color(color)
    two.seth(0)
    two.left(50)
    two.goto(0, 0)
    two.circle(-30, 190)
    two.fd(50)
    two.seth(0)
    two.forward(60) 

def draw_one(color):
    """Draws a one in the turtle thing"""
    one.hideturtle()
    one.color(color)
    one.seth(0)
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

finish_line() # Sets up the race
race_setup()

for c in (red, orange, yellow, green, blue, indigo, purple): # Makes the turtles turtle paced
    c.speed(1)

one = t.Turtle()
two = t.Turtle()
three = t.Turtle()
three.fd(0) # Fixed a weird, fake, annoying "error" so I kept it

clear_terminal() # Clearing the terminal for a more satisfying look

draw_three("white") # Countdown!
draw_three("black")
draw_two("white")
draw_two("black")
draw_one("white")
draw_one("black")

t.home()
t.hideturtle()
racer = 1 # Creates the variable that lets the code detect the winner
race_in_progress = True # Lets the while loop and the for loop break at the same time
blue_is_rigged = r.random() # Niche referenc
while race_in_progress:
    for c in (red, orange, yellow, green, blue, indigo, purple):
        distance = r.uniform(1, 10)
        if c == blue:
            if blue_is_rigged < 0.0001: # Niche reference
                c.goto(500, -100)
            c.fd(2)
        else:
            c.fd(distance)
        if c.xcor() >= 500: # Check for each color winning
            if racer % 7 == 1:
                t.color("red")
                t.write("Red won!", font=("Arial", 36, "normal")) # Types each winner in the terminal
            elif racer % 7 == 2:
                t.color("orange")
                t.write("Orange won!", font=("Arial", 36, "normal"))
            elif racer % 7 == 3:
                t.color("yellow")
                t.write("Yellow won!", font=("Arial", 36, "normal"))
            elif racer % 7 == 4:
                t.color("green")
                t.write("Green won!", font=("Arial", 36, "normal"))
            elif racer % 7 == 5:
                t.color("blue")
                t.write("Blue won!", font=("Arial", 36, "normal"))
            elif racer % 7 == 6:
                t.color("indigo")
                t.write("Indigo won!", font=("Arial", 36, "normal"))
            else:
                t.color("purple")
                t.write("Purple won!", font=("Arial", 36, "normal"))
            race_in_progress = False
            break
        racer += 1

t.exitonclick() # Exits the turtle on click

# Yay!