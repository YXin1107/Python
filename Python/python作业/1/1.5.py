# 猴子吃桃
n = 1
for i in range(4, 0, -1):
    # range(x,y,z)其中x为起始值，y为终止值，z为步长（默认1）
    n = (n+1) << 1
print(n)
