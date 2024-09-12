import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

f = pd.read_csv("result.csv", encoding="utf-8")
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.DataFrame(f)
temperature = df["最低气温/最高气温"].tolist()
year_month_day = df["日期"].to_list()
year = [i.split("年")[0] for i in year_month_day]
month = [i.split("月")[0].split("年")[1] for i in year_month_day]
lower_temperature = [i.split("/")[0].replace("℃", "") for i in temperature]
higher_temperature = [i.split("/")[1].replace("℃", "") for i in temperature]
alls, year_month, list1 = [], [], []
for i in range(len(year)):
    if 2018 <= int(year[i]) <= 2022:
        year_month.append(month[i])
        alls.append([month[i], lower_temperature[i], higher_temperature[i]])
codes = list(set([element[0] for element in alls]))
res = []
for code in codes:
    aux = [code]
    res01 = 0
    res02 = 0
    for element in alls:
        if element[0] == code:
            res01 += int(element[1])
            res02 += int(element[2])
    aux += [res01, res02]
    res.append(aux)
yue, y1, y2 = [], [], []
for i in range(12):
    y1.append(res[i][1]/len(alls))
    y2.append(res[i][2]/len(alls))
listDate = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
width = 0.4
plt.bar(x=np.arange(len(y1)), height=y1, width=width, label='平均最低气温')
plt.bar(x=np.arange(len(y2)) + width, height=y2, width=width, label='平均最高气温')
plt.xticks(np.arange(12), listDate)  # 用星期几替换横坐标x的值
plt.xlabel("月份")
plt.ylabel("温度")
plt.legend()  # 给出图例
plt.show()
