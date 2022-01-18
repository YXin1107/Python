# 文本进度条
import time
scale = 50
for i in range(scale+1):
    a = '.' * i
    b = '-' * (scale - i)
    c = (i / scale) * 100
    print("\rStarting {:^3.0f}% {}->{}".format(c, a, b),
          end='')  # \r:换行,光标移动到下行首行;end='':不换行
    time.sleep(0.05)
print("\b\b Done!")  # \b:回退一格
