# 无角正方形的绘制
import turtle
turtle.setup(1000, 500, 200, 200)
turtle.penup()  # 笔抬起
turtle.fd(-60)
turtle.pendown()  # 笔放下
turtle.pensize(6)
# 绘制正方形
turtle.penup()
for i in range(4):
    turtle.seth(90*i)
    turtle.fd(50)
    turtle.pendown()
    turtle.fd(100)
    turtle.penup()
    turtle.fd(50)
turtle.done()
