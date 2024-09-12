from statsmodels.tsa.stattools import adfuller, kpss
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

df = pd.read_excel('./1-3.xlsx', parse_dates=['年份'])
y1 = df.iloc[:, 3]
y2 = df.iloc[:, 4]
y3 = df.iloc[:, 5]
y4 = df.iloc[:, 6]
y5 = df.iloc[:, 7]
y6 = df.iloc[:, 8]
y7 = df.iloc[:, 9]
yy1 = df.iloc[:, 3].apply(lambda x: np.log(x))
yy2 = df.iloc[:, 4].apply(lambda x: np.log(x))
yy3 = df.iloc[:, 5].apply(lambda x: np.log(x))
yy4 = df.iloc[:, 6].apply(lambda x: np.log(x))
yy5 = df.iloc[:, 7].apply(lambda x: np.log(x))
yy6 = df.iloc[:, 8].apply(lambda x: np.log(x))
yy7 = df.iloc[:, 9].apply(lambda x: np.log(x))
diff_y1 = np.diff(yy1, n=1)
diff_y2 = np.diff(yy2, n=1)
diff_y3 = np.diff(yy3, n=1)
diff_y4 = np.diff(yy4, n=1)
diff_y5 = np.diff(yy5, n=1)
diff_y6 = np.diff(yy6, n=1)
diff_y7 = np.diff(yy7, n=1)


def canshu(c):
    # ADF Test
    result = adfuller(c, autolag='AIC')
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    for key, value in result[4].items():
        print('Critial Values:')
        print(f'   {key}, {value}')

    # KPSS Test
    result = kpss(c, regression='c')
    print('\nKPSS Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    for key, value in result[3].items():
        print('Critial Values:')
        print(f'   {key}, {value}')


canshu(diff_y1)
