import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import warnings

warnings.filterwarnings('ignore')
matplotlib.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('1-2.xlsx')
datas = df['y']
sm.graphics.tsa.plot_pacf(datas, lags=30)
plt.title('PACF')
plt.show()
sm.graphics.tsa.plot_acf(datas, lags=30)
plt.title('ACF')
plt.show()
