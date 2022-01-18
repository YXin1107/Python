# 正方形螺旋线的绘制
import turtle
turtle.pen(speed=0)  # 设置绘图速度
turtle.setup(1000, 1000, 200, 200)
turtle.penup()  # 笔抬起
turtle.fd(-100)
turtle.pendown()  # 笔放下
turtle.pensize(1)
turtle.setheading(90)
# 循环
length = 400
while length != 0:
    turtle.fd(length)
    turtle.right(90)
    length -= 5
turtle.done()
