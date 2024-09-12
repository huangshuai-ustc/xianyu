import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_csv('d:/result_ansi.csv', encoding="utf-8", header=None)
word = np.array(df.iloc[0:20, 0]).tolist()  # 取第0到20行，第0列
freq = np.array(df.iloc[0:20, 1]).tolist()  # 取第0到20行，第1列
plt.bar(word, height=freq)
plt.show()


