import scipy.stats as st
import pandas as pd
import numpy as np
import os
import statsmodels.api as sm
from matplotlib import pyplot as plt
from scipy import *
from sklearn.metrics import r2_score
from statsmodels.sandbox.regression.predstd import wls_prediction_std

path = './task2/'
if not os.path.exists(path):
    os.mkdir(path)
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率
df = pd.read_csv('air-quality.csv')
df = df.iloc[:, [10, 11, 12, 5, 6, 8]][:1000]
x1 = df['Temp__F_']  # 温度


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


def func(f, x):
    return f[0] * x ** 2 + f[1] * x + f[2]


def data_ols(data, name):
    x = sm.add_constant(data)  # 若模型中有截距，必须有这一步
    model = sm.OLS(y, x, hasconst=1)  # 构建最小二乘模型并拟合
    results = model.fit()
    yfit = results.fittedvalues  # 模型拟合的 y值
    prstd, ivLow, ivUp = wls_prediction_std(results)  # 返回标准偏差和置信区间
    # print(results.summary())  # 输出回归结果
    a0, a1 = results.params.tolist()[0], results.params.tolist()[1]
    sigma = results.bse.tolist()[0]
    # p_values, R_squared, adjusted_R_squared = results.pvalues.tolist()[0], results.rsquared, results.rsquared_adj
    # print('变量', name, '的a0,a1,sigma,p值,r方,调整r方分别为: ', a0, a1, sigma, p_values, R_squared, adjusted_R_squared)
    # # 进行正态检验
    # residuals = results.resid
    # kstest = sm.stats.diagnostic.kstest_normal(residuals)
    # print("Kolmogorov-Smirnov test:", kstest)
    # fig, ax = plt.subplots(figsize=(10, 8))
    # ax.plot(data, y, 'o', label="data")  # 原始数据
    # ax.plot(data, yfit, 'r-', label="fit")  # 拟合数据
    # ax.plot(data, ivUp, '--', color='orange', label="upConf")  # 95% 置信区间 上限
    # ax.plot(data, ivLow, '--', color='orange', label="lowConf")  # 95% 置信区间 下限
    # ax.legend(loc='best')  # 显示图例
    # plt.title('{} linear regression'.format(name))
    # plt.savefig(path + '{} linear regression.jpg'.format(name))
    # # plt.show()
    #
    # # residuals histogram
    # plt.figure()
    # results.resid.plot(kind='hist')
    # plt.xlabel(name)
    # plt.ylabel('')
    # plt.title('{}_resid_hist'.format(name))
    # plt.savefig(path + '{}_resid_hist.jpg'.format(name))
    # # plt.show()
    # plt.close()
    # # qq
    # plt.figure()
    # sm.qqplot(data, line='r')
    # plt.xlabel(name)
    # plt.ylabel('')
    # plt.title('{}_qq'.format(name))
    # plt.savefig(path + '{}_qq.jpg'.format(name))
    # # plt.show()
    # # residuals scatter
    # plt.figure()
    # plt.scatter(data, results.resid.tolist())
    # plt.xlabel(name)
    # plt.ylabel('')
    # plt.title('{}_resid_scatter'.format(name))
    # plt.savefig(path + '{}_resid_scatter.jpg'.format(name))
    # # plt.show()
    #
    f = np.polyfit(data, y, 2)
    print(f)
    y_pred = data.apply(lambda x: func(f, x))
    r2 = r2_score(y, y_pred)
    print(r2 ** 2)


data_ols(x1, 'Temp__F_')
data_ols(x2, 'Humidity____')
data_ols(x3, 'Pressure__mbar_')
data_ols(x4, 'PM_2_5_30_Minute_Avg_')
data_ols(x5, 'PM_2_5_1_Hour_Avg_')
