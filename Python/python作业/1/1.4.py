# 计算1!+...+n!(输入数字n)
multi, sum, = 1, 0
n = input('请输入n:')
n = int(n)
for i in range(1, n+1):
    multi *= i
    sum = sum + multi
print("运算结果是: {}".format(sum))
