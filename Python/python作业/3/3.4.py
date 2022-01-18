# 回文数判断
def judge(n):
    n_reverse = n[::-1]  # n[::-1]相当于 n[-1:-len(n)-1:-1]，也就是从最后一个元素到第一个元素复制一遍
    if n_reverse == n:
        print(n + "是回文数")
    else:
        print(n + "不是回文数")


x = input("请输入一个5位数字：")
while x != "":
    judge(x)
    x = input("请输入一个5位数字：")
