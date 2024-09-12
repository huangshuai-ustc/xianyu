import scipy.stats as st
import pandas as pd
import numpy as np
import os
import statsmodels.api as sm
from matplotlib import pyplot as plt
from scipy import *
from statsmodels.sandbox.regression.predstd import wls_prediction_std

path = './task3/'
if not os.path.exists(path):
    os.mkdir(path)
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率
df = pd.read_csv('air-quality.csv')
df = df.iloc[:, [10, 11, 12, 5, 6, 8]][:1000]
x1 = df['Temp__F_']


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
x1 = df['Temp__F_']  # 温度
x2 = df['Humidity____']
x3 = df['Pressure__mbar_']
x4 = df['PM_2_5_30_Minute_Avg_']
x5 = df['PM_2_5_1_Hour_Avg_']
y = df['PM_2_5_24_Hour_Avg_']

X = np.column_stack((x1, x2, x3, x4, x5))  # (nSample,4): [x0,x1,x2,...,xm]

# 多元线性回归：最小二乘法(OLS)
model = sm.OLS(y, X)  # 建立 OLS 模型: Y = b0 + b1*X + ... + bm*Xm + e
results = model.fit()  # 返回模型拟合结果
yFit = results.fittedvalues  # 模型拟合的 y值
print(results.summary())  # 输出回归分析的摘要
params = results.params.tolist()
a0, a1, a2, a3, a4 = params[0], params[1], params[2], params[3], params[4]
sigma = results.bse.tolist()
p_values, R_squared, adjusted_R_squared = results.pvalues.tolist()[0], results.rsquared, results.rsquared_adj
print('多元线性回归的系数分别为: ', a0, a1, a2, a3, a4)
print(sigma)
print('多元线性回归的p值,r方,调整r方分别为: ', p_values, R_squared, adjusted_R_squared)
residuals = results.resid
# 进行正态检验
kstest = sm.stats.diagnostic.kstest_normal(residuals)
print("Kolmogorov-Smirnov test:", kstest)
plt.figure()
#ols.fit().model is a method to access to the residual.
results.resid.plot.density()
plt.savefig(path + 'multi_resid.jpg')
# plt.show()
plt.figure()
sm.qqplot(residuals, line='r')
plt.xlabel('')
plt.ylabel('')
plt.title('multi_qq')
plt.savefig(path + 'multi_qq.jpg')
# plt.show()
print(df.corr())
# residuals histogram
plt.figure()
results.resid.plot(kind='hist')
plt.title('multi_resid_hist')
plt.savefig(path + 'muti_resid_hist.jpg')
# plt.show()
plt.figure()
plt.scatter(y, results.resid.tolist())
plt.title('multi_resid_scatter')
plt.savefig(path + 'multi_resid_scatter.jpg')
# plt.show()
