# e3.1DayDayup365.py
'''
一年365天，如果好好学习时能力值相比前一天提高0.1%，当放任时相比前一天下降0.1%，效果相差多少？
'''
import math
dayup = math.pow((1.0 + 0.001), 365)  # 提高0.001
daydown = math.pow((1.0 - 0.001), 365)  # 放任0.001
print("向上: {:.2f},向下: {:.2f}".format(dayup, daydown))
