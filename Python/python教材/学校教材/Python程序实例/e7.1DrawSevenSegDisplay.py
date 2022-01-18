# e7.1DrawSevenSegDisplay
import turtle
from datetime import datetime


def drawline(draw):  # 绘制单段数码管
    turtle.pen(speed=0)
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)


def drawDigit(d):  # 根据数字绘制七段数码管
    drawline(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if d in [0, 2, 6, 8] else drawline(False)
    turtle.left(90)
    drawline(True) if d in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
    turtle.right(180)
    turtle.penup()
    turtle.fd(25)


def drawdata(data):  # 获得要输出的数字
    for i in data:
        # 方法一
        # try:
        #     a = eval(i)
        #     drawDigit(a)
        # except SyntaxError:
        #     turtle.fd(25)

        # 方法二
        if i == ' ':
            turtle.fd(25)
        else:
            drawDigit(eval(i))


def main():  # 主程序
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-400)
    turtle.pensize(5)
    now = datetime.now()
    drawdata(now.strftime("%Y %m%d %I%M%S"))
    turtle.hideturtle()
    turtle.done()


main()
