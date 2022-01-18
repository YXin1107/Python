# 六角形的绘制
import turtle
turtle.setup(1000, 500, 200, 200)
turtle.penup()  # 笔抬起
turtle.fd(-60)
turtle.pendown()  # 笔放下
turtle.pensize(6)
# 绘制两个等边三角形
turtle.seth(30)
turtle.fd(300)
turtle.seth(-90)
turtle.fd(300)
turtle.seth(150)
turtle.fd(300)
###################
turtle.seth(30)
turtle.fd(100)
turtle.seth(90)
turtle.fd(100)
turtle.seth(-30)
turtle.fd(300)
turtle.seth(-150)
turtle.fd(300)
turtle.seth(90)
turtle.fd(200)
turtle.done()
