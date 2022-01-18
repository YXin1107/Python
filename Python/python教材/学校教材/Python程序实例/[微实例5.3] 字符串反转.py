# [微实例5.3]字符串反转
def reverse(s):
    if s == '':
        return s
    else:
        return(reverse(s[1:])+s[0])


str = input('please enter a string:')
print(reverse(str))
