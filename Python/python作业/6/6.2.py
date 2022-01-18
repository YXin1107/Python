ch = {}


def repeat():
    a = input("enter what you want:")
    while a != "":
        if a in ch:
            ch[a] = ch[a] + 1
        else:
            ch[a] = 1
        a = input("enter what you want:")


repeat()
item = list(ch.items())
num = len(item)
for i in range(num):
    '''
    word,count = item[i]
    if count > 1:
        print(item[i],'True')
    else:
        print(item[i],'False')
    '''
    if item[i][1] > 1:
        print(item[i], 'True')
    else:
        print(item[i], 'False')
