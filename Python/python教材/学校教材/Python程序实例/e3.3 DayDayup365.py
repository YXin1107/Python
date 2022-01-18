# e3.3 DayDayup365
'''
一年365天，如果好好学习时能力值相比前一天提高1%，当放任时相比前一天下降1%，效果相差多少？
'''
import math
dayfactor = 0.01
dayup = math.pow((1 + dayfactor), 365)
daydown = math.pow((1 - dayfactor), 365)
print("向上:{:.2f},向下:{:.2f}".format(dayup, daydown))
