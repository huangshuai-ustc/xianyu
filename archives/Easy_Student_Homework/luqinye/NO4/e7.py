import pandas as pd
from matplotlib import pyplot as plt
import operator

f = pd.read_csv("result.csv", encoding="utf-8")
df = pd.DataFrame(f)
temperature = df["最低气温/最高气温"].tolist()
year_month_day = df["日期"].to_list()
month = [i.split("月")[0].split("年")[1] for i in year_month_day]
lower_temperature = [i.split("/")[0].replace("℃", "") for i in temperature]
higher_temperature = [i.split("/")[1].replace("℃", "") for i in temperature]
difference_in_temperature = []
for i in range(len(lower_temperature)):
    if lower_temperature[i] and higher_temperature[i]:
        difference_in_temperature.append(int(higher_temperature[i]) - int(lower_temperature[i]))
    else:
        difference_in_temperature.append(-1)
temperature_tuple = list(tuple(zip(month, difference_in_temperature)))
temperature_tuple.sort(key=operator.itemgetter(1), reverse=True)
# print(temperature_tuple[:100])
count = [0] * 12
for i in range(len(temperature_tuple)):
    if temperature_tuple[i][1] >= 15:
        # print(type(temperature_tuple[i][0]))
        count[int(temperature_tuple[i][0])] += 1
for i in range(12):
    print("第" + str(i) + "月昼夜温差超过15的天数有" + str(count[i]) + "天")
# print(count)
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
x = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
plt.bar(x, count)
plt.show()
