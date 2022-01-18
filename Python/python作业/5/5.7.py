# 汉诺塔
idx = 0


def hanoi(n, fir, mid, fin):
    global idx
    if n == 1:
        print('{}:{}->{}'.format(1, fir, fin))
        idx += 1
    else:
        hanoi(n-1, fir, fin, mid)
        print('{}:{}->{}'.format(n, fir, fin))
        idx += 1
        hanoi(n-1, fin, mid, fir)


hanoi(5, 'A', 'B', 'C')
print('共用了{}步'.format(idx))
