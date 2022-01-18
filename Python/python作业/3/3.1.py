# 重量计算
kg = float(input("请输入你的体重："))
year = 10
print("初始体重，地球：{:.2f}kg，月球：{:.2f}kg\n".format(kg, kg * 0.165))
for i in range(1, year + 1):
    kg_moon = kg * 0.165
    kg += 0.5
    print("第{}年，地球：{:.2f}kg，月球：{:.2f}kg".format(i, kg, kg_moon))
