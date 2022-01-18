import turtle
color = ['purple', 'red', 'yellow', 'blue', 'gray', 'green', 'black', 'brown']
turtle.pen(speed=0)
turtle.setup(1000, 500, 200, 200)
turtle.penup()
turtle.fd(-100)
turtle.pendown()
turtle.pensize(20)
turtle.seth(-40)
length = 50
for i in range(8):
    turtle.pencolor(color[i])
    turtle.circle(length, 80)
    turtle.circle(-length, 80)
    turtle.right(90)
    length += 25
turtle.done()
