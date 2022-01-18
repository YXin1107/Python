idx = 0


def move(n, a, b, c):
    global idx
    if(n == 1):
        print(n, ':', a, "->", c)
        idx += 1
        return
    move(n-1, a, c, b)
    print(n, ':', a, "->", c)
    idx += 1
    move(n-1, b, a, c)


move(5, "a", "b", "c")
print('共用了{}步'.format(idx))
