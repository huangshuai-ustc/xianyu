import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

file_path = 'air-quality.csv'
df = pd.read_csv(file_path)
x1 = df['Temp__F_'].dropna()
split_index = int(0.8 * len(x1))
train_data, test_data = x1[:split_index], x1[split_index:]


def stationarity(timeseries):
    dftest = adfuller(timeseries, autolag='AIC')
    df_output = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        df_output[f'Critical Value ({key})'] = value
    return df_output


def moving_average(series, k):
    return np.convolve(series, np.ones(k), 'valid') / k


def exponential_smoothing(series, a):
    result = [series[0]]
    for n in range(1, len(series)):
        result.append(a * series[n] + (1 - a) * result[n-1])
    return result


def calculate_metrics(actual, predicted):
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mape = mean_absolute_percentage_error(actual, predicted)
    return round(rmse, 2), round(mape, 2)


def calculate_metrics2(actual, predicted):
    return np.sqrt(mean_squared_error(actual, predicted))
