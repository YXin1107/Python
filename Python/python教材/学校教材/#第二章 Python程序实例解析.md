<font face="Courier New">
<font size="3">
<!-- <font face="宋体"> -->

[toc]

# 第二章 Python程序实例解析
## 2.2 Pyhton程序语法元素分析
### 2.2.4 字符串
1. 类型:string
2. 两种符号体系：
- 例子：
    $Temp[1],Temp[-1],Temp[N:M]\:(N到M，不包含M)$
- 代码:
```python
Tempstr ="110C"  
>>>print(Tempstr[-1])  
C
>>>print(Tempstr [0: -1])
110
```

<br>

### 2.2.5 赋值语句
1. <变量1>,…,<变量M> = <表达式1>,…,<表达式M>
2. 快速的转换
- 例子:
>x , y = y , x

<br>

### 2.2.6 input( )函数
#### input()函数的使用: 
1. <变量> = input(<提示性文字>)
1. 注意!
input()函数统一按照字符串类型输出  

<br>

### 2.2.7 分支（选择）语句
1. if语句:  
- 代码:
```python
if <条件1>:  
    <语句块1>  
elif <条件2>:  
    <语句块2>  
else：  
    <语句块N>
```

<br>

### 2.2.8 eval( )函数
#### eval()函数的使用
1. 能以python表达式的方式解析并执行字符串  
- 代码：
```python
x=1  
>>>eva1("x+1")  
2  
>>>eva("1.1+2.2")  
3.3
```
2. eval( )处理字符串将去掉双引号  
- 例子:
```python
>>>eval("hello")  
hello
```
<br>

### 2.2.9 print( )函数
1. 当输出变量值时，通过format( )方法将待输出変量整理成期望输出的格式  
- 例子:  
    >print("转换后的温度是: {.2f}".format(F))

<br>

### 2.2.10 循环语句
#### 1. while 语句:  
```python
while (<条件>):
    <语句块1> (True时执行)  
    <语句块2> (False时执行)  
```
- 例子：e1.2TempConvert

#### continue 和 break 用法:
- continue 用于跳过该次循环，break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下
- 例子:
- continue代码:
```python
i = 1  
while i < 10:  
    i += 1  
    if i % 2 > 0:   # 非双数时跳过输出  
        continue  
    print i # 输出双数2、4、6、8、10  
```
- break代码:
```python
i = 1  
while 1 # 循环条件为1必定成立  
    print i&    # 输出1~10  
    i += 1  
    if i > 10:  # 当i大于10时跳出循环  
        break
```

#### 2. for语句:
```python
for 变量 in 范围(循环次数):  
    <语句块>
```
- 例子:
```python
for letter in 'Python':  
    print("当前字母: %s" % letter)
```

<br>

### 2.2.11 函数
1. def语句:定义某一函数,并将其功能封装在这个函数内  
- 例子：e1.3TempConvert

<br>

## 2.4 turtle库语法元素分析
### 2.4.1 绘图坐标体系
#### 1. turtle.setup( )函数
- 定义:  
turtle.setup(width,height,startx,starty)
- 作用:  
设置主窗体的大小和位置
- 参数及其说明:  

|  参数  |           说明           |
| :----: | :----------------------: |
| width  |         窗口宽度         |
| height |         窗口高度         |
| startx | 窗口左侧与屏幕左侧的距离 |
| starty | 窗口顶部与屏幕顶部的距离 |

<br>

### 2.4.2 画笔控制函数
#### 1. turtle.penup( )和turtle.pendown( )函数
>turtle.penup( )  
>turtle.pendown( )  
##### (1) turtle.penup( )函数
- 别名:turtle.pu( ),turtlr.up( )  
- 作用:抬起画笔,之后移动画笔不绘制形状
##### (2) turtle.pendown( )函数
- 别名:turtlr.pd( ),turtle.down( )
- 作用:落下画笔,之后移动画笔将绘制形状
#### 2. turtle.pensize( )函数
>turtle.pensize(25)
##### (1) turtle.pensize(width)函数
- 别名:turtle.width( )
- 作用:设置画笔宽度,当无参数输入时返回当前画笔宽度
- 参数:  
width:设置的画笔线条宽度
#### 3. turtle.pencolor( )函数
>turtle.pencolor("purple")
- 定义:  
turtle.pencolor(colorstring)  
或  
turtle.pencolor((r,g,b))
- 作用:设置画笔颜色,当无参数输入时返回当前画笔颜色
#### 4. turtle.pen()函数
##### (1) turtle.pen(speed=0)
- 作用:  
加快绘图速度

<br>

### 2.4.3 形状绘制函数
#### 1. turtle.fd( )函数
- 代码:
```python
turtle.fd(-250)  
turtle.fd(40)  
turtle.fd(40 * 2/3)
```
- 定义:  
turtle.fd(distance)  
- 作用:  
向小海龟当前行进方向前进distance距离  
- 参数:  
distance:行进距离的像素值,当值为负数时,表示向相反方向前进  
#### 2. turtle.seth( )函数
>turtle.seth(-40)
- 定义:  
turtle.seth(to_angel)  
- 作用:  
设置小海龟当前行进方向为to_angel,该角度是绝对方向角度值  
#### 3. for循环语句和turtle.circle( )函数
- 代码:
```python
for i in range(4):  
    turtle.circle(40,80)  
    turtle.circle(-40,80)  
turtle.circle(40,80/2)  
turtle.circle(16,180)  
```

##### (1) turtle.circle( )函数  
- 定义:  
turtle.circle(radius,extent=None)
- 作用:  
根据半径radius绘制extent角度的弧形
- 参数:  
raduis:弧形半径,当值为正数时,半径在小海龟左侧,当值为负数时,半径在小海龟右侧  
extent:绘制弧形的角度,当不设置参数或参数设置为None时,绘制整个图形  
#### 4. turtle.right( )和turtle.left( )和setheading( )
##### (1) turtle.right( )函数
- 定义:  
turtle.right(degree)
- 作用:  
顺时针旋转degree
##### (2) turtle.left( )函数
- 定义:  
turtle.left(degree)
- 作用:  
逆时针旋转degree











