# 4.3 最大公约数的计算(最小公倍数)
a, b = eval(input("请输入两个整数:"))
x = a * b
if a < b:
    a, b = b, a
r = a % b
while r:
    a = b
    b = r
    r = a % b
print("最大公约数是:", b)
print("最小公倍数是:", int(x/b))
