# 绘制叠加等边三角形
import turtle
turtle.setup(1000, 500, 200, 200)
turtle.penup()  # 笔抬起
turtle.fd(-60)
turtle.pendown()  # 笔放下
turtle.pensize(6)
# 绘制外部大三角形
turtle.fd(200)
turtle.seth(120)
turtle.fd(200)
turtle.seth(-120)
turtle.fd(200)
# 绘制内部小三角
turtle.seth(0)
turtle.fd(100)
turtle.seth(60)
turtle.fd(100)
turtle.seth(180)
turtle.fd(100)
turtle.seth(-60)
turtle.fd(100)
turtle.done()
