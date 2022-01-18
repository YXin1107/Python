# 改良田字格
def tian(n):  # 为了让田字格看起来更像是田字也是没谁了
    a = 5*n+1
    for i in range(1, a+1):
        if i % 5 == 1:
            print("+ — — — — "*n, end="")  # 确定单个田字格的横线
            print("+")
        else:
            print("|         "*n, end="")  # 确定单个田字格竖线的间隔
            print("|")


def main():
    n = eval(input("please enter n for width you want: "))
    tian(n)  # 可以输出任意个田字格


main()
