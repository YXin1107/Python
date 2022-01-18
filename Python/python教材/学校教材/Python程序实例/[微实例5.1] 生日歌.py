# [微实例5.1] 生日歌
def happy():
    print("Happy birthday to you!")


def happyB(name):
    happy()
    happy()
    print("Happy birthday,dear {}!".format(name))
    happy()


name1 = input("输入名字:")
happyB(name1)
