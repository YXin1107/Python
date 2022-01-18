# e4.2TextProgress Bar
import time
for i in range(101):
    print("\r{:2}%".format(i), end='')
    time.sleep(0.05)
print("\r充能完毕")
