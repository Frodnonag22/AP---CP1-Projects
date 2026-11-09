#AP Library notes
import turtle as t


t.shape("turtle")

t.speed(100000000000000000000000000000000000000000000000000000000000000000000)
t.exitonclick
t.showturtle()

t.forward(250)
t.left(120)
t.forward(250)
t.left(120)
t.forward(250)

t.color('red')
t.fillcolor('yellow')
t.begin_fill()
start = t.pos()

while True:
    t.forward(200)
    t.left(170)
    if t.distance(start) < 1:
        break
t.end_fill()

t.width(50)
for steps in range(150):
    for c in ('red','orange','yellow','green','blue','purple'):
        t.color(c)
        t.forward(steps)
        t.right(30)

for i in range (360):
    t.forward(1)
    t.left(1)

t.home()

t.exitonclick()