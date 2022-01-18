# 重复判定续
def repeat():
    n = []
    a = input("enter what you want:")
    while a != "":
        n.append(a)
        a = input("enter what you want:")
    else:
        if len(n) == len(set(n)):  # set可以去除重复值
            return False
        else:
            return True


repeat()
