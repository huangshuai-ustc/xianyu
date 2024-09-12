from statsmodels.tsa.stattools import adfuller  # 平稳性检测
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima.model import ARIMA  # ARIMA模型
from statsmodels.graphics.api import qqplot  # 画qq图
from scipy.stats import shapiro  # 正态检验
from icecream import ic
import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import itertools
import warnings
import seaborn as sns

warnings.filterwarnings('ignore')
matplotlib.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('1-4.xlsx')
y2013, y2014 = df.iloc[:, 1].apply(lambda x: int(10000 * x)), df.iloc[:, 2].apply(lambda x: int(10000 * x))
y2015, y2016 = df.iloc[:, 3].apply(lambda x: int(10000 * x)), df.iloc[:, 4].apply(lambda x: int(10000 * x))
y2017, y2018 = df.iloc[:, 5].apply(lambda x: int(10000 * x)), df.iloc[:, 6].apply(lambda x: int(10000 * x))
yy = [sum(y2013), sum(y2014), sum(y2015), sum(y2016), sum(y2017), sum(y2018)]
xx = df.columns.values[1:]
data = pd.DataFrame({'Date': xx, 'Value': yy})
data = data.set_index('Date')
# y2013, y2014 = df.iloc[:, 1].apply(lambda x: np.log(x)), df.iloc[:, 2].apply(lambda x: np.log(x))
# y2015, y2016 = df.iloc[:, 3].apply(lambda x: np.log(x)), df.iloc[:, 4].apply(lambda x: np.log(x))
# y2017, y2018 = df.iloc[:, 5].apply(lambda x: np.log(x)), df.iloc[:, 6].apply(lambda x: np.log(x))
# y2019 = df.iloc[:, 7].apply(lambda x: np.log(x))
# yy = [sum(y2013), sum(y2014), sum(y2015), sum(y2016), sum(y2017), sum(y2018), sum(y2019)]
# 切分为测试数据和训练数据
n_sample = data.shape[0]
n_train = int(0.95 * n_sample) + 1
n_forecast = n_sample - n_train
data_train = data.iloc[:n_train]['Value']
data_test = data.iloc[n_train:]['Value']

# plt.plot(data)
# plt.title('Value走势图"')
# plt.show()

ic(adfuller(data))  # 原始数据
ic(adfuller(data.diff(2).dropna()))  # 一阶差分
ic(acorr_ljungbox(data, lags=3))

sm.graphics.tsa.plot_acf(data, lags=20)
plt.title('PACF')
# plt.show()
sm.graphics.tsa.plot_acf(data, lags=20)
plt.title('ACF')
# plt.show()


# 这里最大最小的参数可以自己调
p_min = 0
d_min = 0
q_min = 0
p_max = 7
d_max = 1
q_max = 7

# Initialize a DataFrame to store the results,，以BIC准则
results_bic = pd.DataFrame(index=['AR{}'.format(i) for i in range(p_min, p_max + 1)],
                           columns=['MA{}'.format(i) for i in range(q_min, q_max + 1)])

for p, d, q in itertools.product(range(p_min, p_max + 1),
                                 range(d_min, d_max + 1),
                                 range(q_min, q_max + 1)):
    if p == 0 and d == 0 and q == 0:
        results_bic.loc['AR{}'.format(p), 'MA{}'.format(q)] = np.nan
        continue

    try:
        model = sm.tsa.ARIMA(data_train, order=(p, d, q),
                             # enforce_stationarity=False,
                             # enforce_invertibility=False,
                             )
        results = model.fit()
        results_bic.loc['AR{}'.format(p), 'MA{}'.format(q)] = results.bic
    except:
        continue
results_bic = results_bic[results_bic.columns].astype(float)
fig, ax = plt.subplots(figsize=(10, 8))
ax = sns.heatmap(results_bic,
                 mask=results_bic.isnull(),
                 ax=ax,
                 annot=True,
                 fmt='.2f',
                 )
ax.set_title('BIC')
plt.show()

train_results = sm.tsa.arma_order_select_ic(data_train, ic=['aic', 'bic'], trend='c', max_ar=7, max_ma=7)

ic('AIC', train_results.aic_min_order)
ic('BIC', train_results.bic_min_order)
model = ARIMA(data_train, order=(2, 1, 0))
result = model.fit()
result.summary()
# 获取残差
resid = result.resid
# 画qq图
qqplot(resid, line='q', fit=True)
plt.show()
shapiro(resid)
ic(sm.stats.durbin_watson(resid.values))
predict = result.predict(2019)
listy = [yy[-1], predict]
print('预测的2019年入境四川旅游人数约为：', listy, '万人')
plt.plot(np.arange(2013, 2019), yy, label='原始数据')
plt.plot(np.arange(2018, 2020), listy, 'r', label='预测数据')
plt.title('外国入境四川旅游人数及预测')
plt.xlabel('年份')
plt.ylabel('旅游人数/万人')
plt.legend(loc=3, borderaxespad=0., bbox_to_anchor=(0, 0.8))
plt.show()
