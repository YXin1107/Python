# e3.5DayDayup365
'''
一年365天，每周工作5天,休息2天,休息日能力下降0.01,试问工作日要多努力,一年后的水平与每天努力1%取得的效果相同?
'''


def dayUP(df):
    dayup, dayfactor = 1.0, 0.01
    for i in range(365):
        if i % 7 in [0, 6]:
            dayup = dayup * (1 - dayfactor)
        else:
            dayup = dayup * (1 + df)
    return dayup


dayfactor1 = 0.001
while(dayUP(dayfactor1) < 37.78):
    dayfactor1 += 0.0001
print("每天的努力参数是:{:.4f}".format(dayfactor1))
