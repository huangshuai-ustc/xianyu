import pandas as pd
import numpy as np
import statsmodels.api as sm


df = pd.read_csv('air-quality.csv')
df = df.iloc[:, [10, 11, 12, 5, 6, 8]][:2000]


def drop_outlines(data):
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    outliers = data[(data < q1 - 1.5 * iqr) | (data > q3 + 1.5 * iqr)]
    df.drop(outliers.index, inplace=True)


x1 = df['Temp__F_']
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
X = np.column_stack((x1, x2, x3, x4, x5))

model = sm.OLS(y, X)
results = model.fit()
yFit = results.fittedvalues
print(results.summary())
params = results.params.tolist()
a0, a1, a2, a3, a4 = params[0], params[1], params[2], params[3], params[4]
sigma = results.bse.tolist()
p_values, R_squared, adjusted_R_squared = results.pvalues.tolist()[0], results.rsquared, results.rsquared_adj
print('多元线性回归的系数分别为: ', a0, a1, a2, a3, a4)
print(sigma)
print('多元线性回归的p值,r方,调整r方分别为: ', p_values, R_squared, adjusted_R_squared)

