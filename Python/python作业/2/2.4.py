# 等边三角形的绘制
import turtle
turtle.setup(1000, 500, 200, 200)
turtle.penup()  # 笔抬起
turtle.fd(-60)
turtle.pendown()  # 笔放下
# 绘制三角形
turtle.pensize(6)
turtle.pencolor()
turtle.fd(100)
turtle.seth(120)
turtle.fd(100)
turtle.seth(-120)
turtle.fd(100)
turtle.done()
