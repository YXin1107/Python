# 实现isPrime()函数
def isPrime():
    num = input('请输入一个整数:')
    try:
        num = eval(num)
        if isinstance(num, int):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        return False
                        break  # 第一次整除就跳出
                    else:
                        return True
            else:  # 小于1的整数必然不是质数
                return False
        else:  # 不是整数的必然不是质数
            return False
    except:
        print('输入格式有误')


isPrime()
