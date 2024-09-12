import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import math
import os

path = './task2/'
if not os.path.exists(path):
    os.mkdir(path)
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率
df = pd.read_csv('air-quality.csv')
df = df[:100]
x1 = df['Temp__F_']  # 温度
x2 = df['Humidity____']
x3 = df['Pressure__mbar_']
x4 = df['PM_2_5_30_Minute_Avg_']
x5 = df['PM_2_5_1_Hour_Avg_']
# 最大值
x1_max = x1.max()
x2_max = x2.max()
x3_max = x3.max()
x4_max = x4.max()
x5_max = x5.max()
# 最小值
x1_min = x1.min()
x2_min = x2.min()
x3_min = x3.min()
x4_min = x4.min()
x5_min = x5.min()
# 均值
x1_mean = x1.mean()
x2_mean = x2.mean()
x3_mean = x3.mean()
x4_mean = x4.mean()
x5_mean = x5.mean()
# 中位数
x1_median = x1.median()
x2_median = x2.median()
x3_median = x3.median()
x4_median = x4.median()
x5_median = x5.median()
# 方差
x1_varies = x1.var()
x2_varies = x2.var()
x3_varies = x3.var()
x4_varies = x4.var()
x5_varies = x5.var()
# 四分位数-1
x1_median_1 = np.quantile(x1, 0.25)
x2_median_1 = np.quantile(x2, 0.25)
x3_median_1 = np.quantile(x3, 0.25)
x4_median_1 = np.quantile(x4, 0.25)
x5_median_1 = np.quantile(x5, 0.25)
# 四分位数-3
x1_median_3 = np.quantile(x1, 0.75)
x2_median_3 = np.quantile(x2, 0.75)
x3_median_3 = np.quantile(x3, 0.75)
x4_median_3 = np.quantile(x4, 0.75)
x5_median_3 = np.quantile(x5, 0.75)
print('x1的均值、方差、0.25分位数、中位数、0.75分位数、IQR、最大值，最小值分别为：',
      x1_mean, x1_varies, x1_median_1, x1_median, x1_median_3, x1_median_3 - x1_median_1, x1_max, x1_min)
print('x2的均值、方差、0.25分位数、中位数、0.75分位数、IQR、最大值，最小值分别为：',
      x2_mean, x2_varies, x2_median_1, x2_median, x2_median_3, x2_median_3 - x2_median_1, x2_max, x2_min)
print('x3的均值、方差、0.25分位数、中位数、0.75分位数、IQR、最大值，最小值分别为：',
      x3_mean, x3_varies, x3_median_1, x3_median, x3_median_3, x3_median_3 - x3_median_1, x3_max, x3_min)
print('x4的均值、方差、0.25分位数、中位数、0.75分位数、IQR、最大值，最小值分别为：',
      x4_mean, x4_varies, x4_median_1, x4_median, x4_median_3, x4_median_3 - x4_median_1, x4_max, x4_min)
print('x5的均值、方差、0.25分位数、中位数、0.75分位数、IQR、最大值，最小值分别为：',
      x5_mean, x5_varies, x5_median_1, x5_median, x5_median_3, x5_median_3 - x5_median_1, x5_max, x5_min)

# pmf
x1_pmf = x1.value_counts().sort_index() / len(x1)
x1_pmf.plot(kind='line')
plt.title('PMF of Temp__F_')
plt.ylabel('probability')
plt.savefig(path + 'Temp__F_.jpg')
# plt.show()
x2_pmf = x2.value_counts().sort_index() / len(x2)
x2_pmf.plot(kind='line')
plt.title('PMF of Humidity____')
plt.ylabel('probability')
plt.savefig(path + 'Humidity____.jpg')
# plt.show()
x3_pmf = x3.value_counts().sort_index() / len(x3)
x3_pmf.plot(kind='line')
plt.title('PMF of Pressure__mbar_')
plt.ylabel('probability')
plt.savefig(path + 'Pressure__mbar_.jpg')
# plt.show()
x4_pmf = x4.value_counts().sort_index() / len(x4)
x4_pmf.plot(kind='line')
plt.title('PMF of PM_2_5_30_Minute_Avg_')
plt.ylabel('probability')
plt.savefig(path + 'PM_2_5_30_Minute_Avg_.jpg')
# plt.show()
x5_pmf = x5.value_counts().sort_index() / len(x5)
x5_pmf.plot(kind='line')
plt.title('PMF of PM_2_5_1_Hour_Avg_')
plt.ylabel('probability')
plt.savefig(path + 'PM_2_5_1_Hour_Avg_.jpg')
# plt.show()
