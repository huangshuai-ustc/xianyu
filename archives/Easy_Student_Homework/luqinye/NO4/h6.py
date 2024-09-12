import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams['axes.unicode_minus']=False

f = pd.read_csv("result.csv", encoding="utf-8")
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.DataFrame(f)
temperature = df["最低气温/最高气温"].tolist()
year_month_day = df["日期"].to_list()
month = [i.split("月")[0].split("年")[1] for i in year_month_day]
lower_temperature = [i.split("/")[0].replace("℃", "") for i in temperature]
higher_temperature = [i.split("/")[1].replace("℃", "") for i in temperature]
h = []
for i in higher_temperature:
    if i:
        h.append(i)
    else:
        h.append("0")
lower_temperature = list(map(int, lower_temperature))
higher_temperature = list(map(int, h))
plt.figure(figsize=(10, 10), dpi=400)
plt.plot(lower_temperature)
plt.plot(higher_temperature)
plt.xticks(ticks=range(0, 4955, 450),
           labels=['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
           rotation=45)
plt.xlabel("年份")
plt.ylabel("温度/℃")
plt.show()
