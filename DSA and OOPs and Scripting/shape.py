import turtle
sc=turtle.Screen()
sc.bgcolor('cyan')
sc.title('Basic Shapes')
t=turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)
t.left(90)
t.circle(-50,180)
t.penup()
t.setx(-100)
t.sety(100)
t.pendown()
t.right(180)
for i in range(4):
    t.forward(100)
    t.right(90)
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.right(135)
t.forward(100)
t.backward(100)
t.left(45)
t.forward(100)
t.right(45)
t.forward(100)
sc.exitonclick()