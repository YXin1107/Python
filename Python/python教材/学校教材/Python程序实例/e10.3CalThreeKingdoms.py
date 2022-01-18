# e10.3CalThreeKingdoms
# 人物出场次数统计
import jieba
txt = open(r"C:\Users\Yxin1\Desktop\三国演义.txt", "r").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:  # 排除单字符的分词结果
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
