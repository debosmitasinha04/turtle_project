import turtle
screen=turtle.Screen()
t=turtle.Turtle()
t.color("red")
t.pensize(3)
t.speed(30)
for i in range(10):
    for j in range(4):
        t.circle(50, 60)
        t.left(120)
        t.circle(50, 60)
        t.left(36)

    

turtle.done()