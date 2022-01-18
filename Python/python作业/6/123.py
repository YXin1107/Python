dict = {}
ls = ['综合', '理工', '理工', '师范', '师范', '师范']
for word in ls:
    dict[word] = dict.get(word, 0) + 1
item = list(dict.items())
# item.sort(key=lambda x: x[1],reverse=True) # 按key从小到大排
for i in range(len(item)):
    word, count = item[i]
    print('{}:{}'.format(word, count))
