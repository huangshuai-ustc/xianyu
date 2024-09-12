import pandas as pd
from scipy.interpolate import lagrange
from scipy.stats import linregress
import numpy as np

data = pd.read_excel('1-5.xlsx', header=None)


def least_square_method(x, y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return slope * 2019 + intercept


datas = []
xx = [2013, 2014, 2015, 2016, 2017, 2018]
for i in range(27):  # 遍历每一列
    datas.append(least_square_method(xx, data[i].tolist()[:6]))
df = pd.concat([data.iloc[:-1, :], pd.DataFrame(datas).T],axis=0)
df.to_excel('1-5.xlsx')
