import pandas as pd
from matplotlib import pyplot as plt
import operator
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
f = pd.read_csv("result.csv", encoding="utf-8")
df = pd.DataFrame(f)
temperature = df["最低气温/最高气温"].tolist()
year_month_day = df["日期"].to_list()
month = [i.split("月")[0].split("年")[1] for i in year_month_day]
higher_temperature = [i.split("/")[1].replace("℃", "") for i in temperature]
weather = df["天气状况"].tolist()
wind = df["风力风向(夜间/白天)"].tolist()
day_wind = [i.split("/")[1] for i in wind]
alls, count = [], [0] * 12
for i in range(len(month)):
    alls.append([month[i], weather[i], higher_temperature[i], day_wind[i]])
for i in range(len(alls)):
    if higher_temperature[i]:
        if "晴" in weather[i] and 25 <= int(higher_temperature[i]) <= 30 and "无持续风向" not in day_wind[i]:
            count[int(month[i])] += 1
for i in range(len(count)):
    print(str(i+1) + "月最适合晾葡萄干的天气出现的频数为:" + str(count[i]))
x = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
plt.bar(x, count)
plt.show()

