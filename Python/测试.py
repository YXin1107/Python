import numpy as np
''''''
# 加密通话
# chinese = input("请输入中文:")
# # 中文转Unicode编码
# re = chinese.encode("unicode_escape")
# print(re)
# # Unicode编码转中文
# chinese_1 = re.decode('unicode_escape')
# print('转换后的中文为:', chinese_1)

''''''
# x = ord('a')
# y = ord('z')
# print(x, y)

''''''
# format()函数试验
# s = 'python'
# print("{0:30}".format(s))  # 默认左对齐
# print("{0:>30}".format(s))  # 右对齐
# print("{0:*^30}".format(s))  # 居中且使用*填充
# print("{0:3}".format(s))

''''''
# for i in range(1, 8):
#     print(i % 7)

''''''
# a = '12345'
# b = a[::-1]
# print(b)

''''''
# print(type('123'))

''''''
# for i in "BIT":
#     for j in range(10):
#         print(i, end="")
#         if i == 'I':
#             break

''''''
# random库函数试验
# seed
# import random
# random.seed(3)
# print(random.random())
# random.seed()
# print(random.random())
# # randint
# print(random.randint(1, 10))
# # getrandbits
# print(random.getrandbits(3))
# # uniform
# print(random.uniform(1, 10))
# # choice
# print(random.choice([1, 3, 5, 7, 9]))
# # sample
# print(random.sample([1, 3, 5, 7, 9], 3))
# # shuffle
# items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# random.shuffle(items)
# print(items)

''''''
# **形参 (我不理解)


# def funcF(a, **b):
#     print(a)
#     s = b
#     for x in b:
#         print(x + ": " + str(b[x]))
#     print(s, type(s))


# funcF(100, c='你好', b=200, d='啊', e=5)

''''''


# def func(a, b):
#     return a*b


# s = func("knock~", 2)
# t = func(2, 3)
# print(s, t)
# print(type(s), type(t))

''''''
# from datetime import datetime
# today = datetime.now()
# print(today, type(today))

''''''
# from datetime import datetime
# today = datetime.now()
# print(today)
# print(type(today))

# s = today.isoformat()
# t = today.isoweekday()
# print(s)
# print(t)

''''''
# from datetime import datetime
# now = datetime.now()
# a = now.strftime("%Y-%m-%d")
# b = now.strftime("%Y-%m-%d,%I:%M:%S %p")
# print(a, "\n", b)
# print("今天是{0:%Y}年{0:%m}月{0:%d}日".format(now))

''''''
# 利用datetime库对一个程序运行计时

# from random import *
# from datetime import datetime
# index = 0
# now = datetime.now()
# a = eval(now.strftime("%M"))
# b = eval(now.strftime("%S"))
# # 此处放入运行的程序
# num = randint(-1, 100)
# n = 0
# while 1:
#     try:
#         x = eval(input("请输入0到100之间的整数："))
#     except:
#         print("输入内容必须为整数!")
#     else:
#         if isinstance(x, int):  # 判断x是否是整数
#             n += 1
#             if x < num:
#                 print("遗憾，太小了")
#             elif x > num:
#                 print("遗憾，太大了")
#             else:
#                 print("预测{}次，你猜对了，数字是{}".format(n, x))
#                 break
# now_1 = datetime.now()
# a_1 = eval(now_1.strftime("%M"))
# b_1 = eval(now_1.strftime("%S"))
# delta = (a_1-a)*60+(b_1-b)
# print("程序运行了{0:.0f}s".format(delta))

''''''
# # 1
# import random
# lst = random.sample(range(1, 100), 10)
# print(lst)

# # 2
# lst_1 = random.sample(range(1, 100, 2), 10)
# print(lst_1)

# # 3
# str = 'abcdefghijklmnop'
# lst_3 = random.sample(range(16), 4)
# for i in lst_3:
#     print(str[i], end='')

''''''

# a = 55
# print(type(a))
# b = str(a)
# print(type(b))

''''''
# W = set('apple')
# V = set(('cat', 'dog', 'tiger', 'human'))
# a = 1, 2, 3, 4, 5, 'abc', 'a'
# b = (1, 2, 3, 4, 5, 'abc', 'a')
# c = [1, 2, 3, 4, 5, 'abc', 'a']
# d = {1, 2, 3, 4, 5, 'abc', 'a'}
# X = set(a)
# print(W, V, X)
# print(type(a), type(b), type(c), type(d))

''''''
# S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# T = {2, 4, 6, 8, 10}
# X = S.symmetric_difference(T)
# print(X, S)
# S ^= T
# print(S)

''''''
# S = {'python', 'bit', 123, 'good'}
# print('BIT' in S)
# B = ('python', 'bit', 123, 'good')
# set(B)
# newS = tuple(set(B)-{'python'})
# print(B, newS)
# print(type(B), type(newS))

''''''
# ls = [425, 'bit', [10, 'abc'], 425]  # 用数据赋值产生列表ls
# lt = ls  # lt是ls所对应数据的引用,lt并不包含真实数据
# lt[0] = 0
# print(lt)

''''''
# ls = [1, 2, 3, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '苹果', '哈哈哈']
# lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(ls)
# del ls[::2]
# print(ls)
# ls = [1, 2, 3, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '苹果', '哈哈哈']
# ls += lt
# print(ls)
# ls = [1, 2, 3, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '苹果', '哈哈哈']
# ls *= 5
# print(ls)
# ls = [1, 2, 3, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '苹果', '哈哈哈']
# ls.reverse()
# print(ls)

''''''
# ls = [2, 5, 7, 1, 6]
# ls.sort()
# print(ls)
# ls1 = [30, 1, 2, 0]
# ls2 = ls1
# ls1[0] = 22
# print(ls1, ls2)
# ls = [[1, 2, 3], 123, 3, [5, 2, 1], 123]
# print(len(ls))

''''''
# D = {'张三': '88', '李四': '90', '王五': '73', '赵六': '82'}
# D['钱七'] = '90'
# D['王五'] = '93'
# del D['赵六']
# print(D)

''''''
# a = {1: 2, 3: 4}
# print(a[1])  # 1 为字典里的键
# b = set(a)

''''''
# a = 123
# b = "abc"
# c = f"{a}{b}"
# d = "{}{}".format(a, b)
# print(c)
# print(d)

''''''
# chr = input("enter what you want:")
# ch = {"other": 0, "a": 0, "9": 0, " ": 0}
# for letter in chr:
#     if letter == 'a':
#         ch[letter] += 1
#     elif letter == 9:
#         ch[letter] += 1
#     elif letter == ' ':
#         ch[letter] += 1
#     else:
#         ch['other'] += 1
# item = list(ch.items())
# print(item)

''''''
# chr = 'abc123'
# for i in chr:
#     if i >= 'a' and i <= 'z':
#         print(i)

''''''
# import numpy as np
# ar = np.zeros((8, 8), dtype = np.int32)
# n = 1
# sum = 0
# for i in range(15):
#     sum = i+2
#     for x in range(8):
#         y = sum - x - 1
#         if y >= 1 and y <= 8:
#             if sum % 2 == 0:
#                 ar[y-1][x] = n
#             else:
#                 ar[x][y-1] = n
#             n += 1
# print(ar)

''''''
# import numpy as np
# n = 1
# ar = np.random.randint(0, 2, size=(8, 8))
# print(ar)
# for i in range(15):
#     for x in range(8):
#         y = i - x
#         if y >= 0 and y <= 7:
#             if i % 2 == 1:
#                 print(ar[x][y], end='')
#             else:
#                 print(ar[y][x], end='')
#             n += 1

''''''
ar = np.arange()
