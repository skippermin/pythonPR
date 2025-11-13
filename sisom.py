import turtle
t = turtle.Turtle("turtle")
#사각형 만들기
t.penup()
t.goto(-100, -50)
t.pendown()
t.circle(40, steps = 4)
#육각형 만들기
t.penup()
t.goto(0, -50)
t.pendown()
i = 0
for i in range(6):
    t.forward(100)
    t.right(60)

turtle.mainloop()