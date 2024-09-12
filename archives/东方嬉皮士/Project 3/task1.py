import os
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
path = './task1/'
if not os.path.exists(path):
    os.mkdir(path)
df = pd.read_csv('air-quality.csv')
df = df.iloc[:, [10, 11, 12, 5, 6, 8]][:1000]
x1 = df['Temp__F_']  # 温度
x2 = df['Humidity____']
x3 = df['Pressure__mbar_']
x4 = df['PM_2_5_30_Minute_Avg_']
x5 = df['PM_2_5_1_Hour_Avg_']
y = df['PM_2_5_24_Hour_Avg_']
# # hist
# plt.figure()
# plt.hist(x1)
# plt.title('hist of Temp__F_')
# plt.ylabel('frequency')
# plt.savefig(path + 'Temp__F_.jpg')
# # plt.show()
# plt.figure()
# x2.plot(kind='hist')
# plt.title('hist of Humidity____')
# plt.ylabel('frequency')
# plt.savefig(path + 'Humidity____.jpg')
# # plt.show()
# plt.figure()
# plt.hist(x3.tolist())
# plt.title('hist of Pressure__mbar_')
# plt.ylabel('frequency')
# plt.savefig(path + 'Pressure__mbar_.jpg')
# # plt.show()
# plt.figure()
# x4.plot(kind='hist')
# plt.title('hist of PM_2_5_30_Minute_Avg_')
# plt.ylabel('frequency')
# plt.savefig(path + 'PM_2_5_30_Minute_Avg_.jpg')
# # plt.show()
# plt.figure()
# x5.plot(kind='hist')
# plt.title('hist of PM_2_5_1_Hour_Avg_')
# plt.ylabel('frequency')
# plt.savefig(path + 'PM_2_5_1_Hour_Avg_.jpg')
# # plt.show()

# mean
x1_mean = x1.mean()
x2_mean = x2.mean()
x3_mean = x3.mean()
x4_mean = x4.mean()
x5_mean = x5.mean()
# variance
x1_varies = x1.var()
x2_varies = x2.var()
x3_varies = x3.var()
x4_varies = x4.var()
x5_varies = x5.var()
# print('x1的均值、方差：', x1_mean, x1_varies)
# print('x2的均值、方差：', x2_mean, x2_varies)
# print('x3的均值、方差：', x3_mean, x3_varies)
# print('x4的均值、方差：', x4_mean, x4_varies)
# print('x5的均值、方差：', x5_mean, x5_varies)

def drop_outlines(data):
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    outliers = data[(data < q1 - 1.5 * iqr) | (data > q3 + 1.5 * iqr)]
    df.drop(outliers.index, inplace=True)


drop_outlines(x1)
x2 = df['Humidity____']
drop_outlines(x2)
x3 = df['Pressure__mbar_']
drop_outlines(x3)
x4 = df['PM_2_5_30_Minute_Avg_']
drop_outlines(x4)
x5 = df['PM_2_5_1_Hour_Avg_']
drop_outlines(x5)
# print(df)

# df.corr().to_csv(path + 'corr_result.csv')
# print(type(df.corr()))
