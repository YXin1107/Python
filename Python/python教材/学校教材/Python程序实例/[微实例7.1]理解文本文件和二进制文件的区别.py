# [微实例7.1]理解文本文件和二进制文件的区别
textFile = open(r"C:\Users\Yxin1\Desktop\7.1.txt",
                "rt", encoding="utf-8")  # t 表示文本文件方式
print(textFile.readline())
textFile.close()
binFile = open(r"C:\Users\Yxin1\Desktop\7.1.txt", "rb")  # r 表示二进制文件方式
print(binFile.readline())
binFile.close()
