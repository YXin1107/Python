# 文本字符分析
def txt():
    ch = {}
    a = 0
    while a != '':
        a = input("enter what you want:")
        if a in ch:
            ch[a] = ch[a] + 1
        elif a == '':
            continue
        else:
            ch[a] = 1
    item = list(ch.items())
    item.sort(key=lambda x: x[1], reverse=True)
    b = len(item)
    for i in range(b):
        word, count = item[i]
        print("{0:<10}{1:>5}".format(word, count))


txt()
