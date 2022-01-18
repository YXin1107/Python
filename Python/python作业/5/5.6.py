# 生日输出
from datetime import datetime
bir = datetime(2001, 11, 7, 13, 30, 5)
print(bir.isoformat())
print(bir.strftime("%Y-%m-%d %X"))
print(bir.strftime("%Y-%B-%d %X"))
print(bir.strftime("%Y-%b-%d %X"))
print(bir.strftime("%x %X"))
print(bir.strftime("%x %X"))
print(bir.strftime("%Y|%m|%d|%H|%M|%S"))
