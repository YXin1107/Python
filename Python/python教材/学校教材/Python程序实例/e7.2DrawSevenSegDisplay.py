# e7.2DrawSevenSegDisplay
import turtle
from datetime import datetime


def drawgap():  # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)


def drawline(draw):  # 绘制单端数码管
    drawgap()
    turtle.pen(speed=0)
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
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


def drawdata(data):  # 获得要输出的内容
    turtle.pencolor("red")
    for i in data:
        if i == '-':
            turtle.write('年', font=('宋体', 18, 'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=('宋体', 18, 'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=('宋体', 18, 'normal'))
            turtle.pencolor('black')
            turtle.fd(40)
        elif i == '.':
            turtle.write('点', font=('宋体', 18, 'normal'))
            turtle.fd(40)
        elif i == ',':
            turtle.write('分', font=('宋体', 18, 'normal'))
            turtle.fd(40)
        elif i == ';':
            turtle.write('秒', font=('宋体', 18, 'normal'))
        else:
            drawDigit(eval(i))


def main():  # 主程序
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-400)
    turtle.pensize(5)
    now = datetime.now()
    drawdata(now.strftime("%Y-%m=%d+%I.%M,%S;"))
    turtle.hideturtle()
    turtle.done()


main()
