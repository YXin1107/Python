# e10.1CalHamlet
def getText():
    txt = open(r"C:\Users\Yxin1\Desktop\Hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt = txt.replace(ch, " ")
    return txt


hamletTxt = getText()
words = hamletTxt.split()
counts = {}
# 方法一
'''
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
'''
# 方法二
for word in words:
    counts[word] = counts.get(word, 0) + 1


items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
