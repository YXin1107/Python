# e2.1DrawPython修改版
# 每个小段画笔绘制颜色会发生变化
# import引用函数库的方法一
# import<库名>
import turtle
color = ['purple', 'red', 'yellow', 'blue']
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.seth(-40)
for i in range(4):
    turtle.pencolor(color[i])
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.pencolor('gold')
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()
