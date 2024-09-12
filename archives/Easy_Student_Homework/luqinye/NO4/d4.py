import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
f = pd.read_csv("result.csv", encoding="utf-8")
df = pd.DataFrame(f)
weather = df["天气状况"].tolist()
qk = set(weather)
s = {}
for item in weather:
    s[item] = s.get(item, 0) + 1
highs = sorted(s.items(), key=lambda x: x[1], reverse=True)
high = dict(highs[:10])
xx, yy = [], []
for x, y in high.items():
    xx.append(x)
    yy.append(y)
plt.figure(figsize=(10, 10), dpi=300)
plt.bar(xx, yy, color="r")
plt.xlabel("天气")
plt.ylabel("出现次数")
plt.show()

count = 0
for i in weather:
    if "浮尘" in i or "扬沙" in i:
        count += 1
print("沙尘暴天气占比约" + str(count / len(weather)))
for i in range(len(xx)):
    print(xx[i] + "天气出现的频率为:" + str(yy[i] / len(weather)))
