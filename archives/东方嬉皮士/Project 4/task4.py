from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.ar_model import AutoReg
import statsmodels.api as sm
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from utils import train_data

lags_pacf = pacf(train_data, nlags=40, method='ols')
plt.figure(figsize=(10, 5), dpi=433)
plt.stem(range(len(lags_pacf)), lags_pacf)
plt.title('Partial Autocorrelation Function (PACF)')
plt.xlabel('Lag k')
plt.ylabel('PACF')
plt.grid(True)
plt.savefig('task4/pacf_plot.png')

p = np.where(lags_pacf < 0.05)[0][1] - 1

ar_model = AutoReg(train_data, lags=p).fit()
predictions = ar_model.predict(start=p, end=len(train_data)-1, dynamic=False)
rmse_ar = np.sqrt(mean_squared_error(train_data[p:], predictions))

plt.figure(figsize=(14, 7), dpi=433)
plt.plot(train_data.index, train_data, label='Original', alpha=0.7)
plt.plot(train_data.index[p:], predictions, label='Predicted', alpha=0.7)
plt.title('AR(p) Model - Predicted vs Original Values')
plt.xlabel('Index')
plt.ylabel('Temperature (F)')
plt.legend()
plt.grid(True)
plt.savefig('task4/ar_predicted_vs_original.png')

residuals = train_data[p:] - predictions

figure, axs = plt.subplots(dpi=433)
qq = sm.qqplot(residuals, line='s', fit=True, ax=axs)
plt.title('Q-Q Plot of AR(p) Model Residuals')
plt.savefig('task4/qq_plot_residuals.png')

plt.figure(figsize=(10, 5), dpi=433)
plt.hist(residuals, bins=30, density=True, alpha=0.7, color='blue')
plt.title('Histogram of AR(p) Model Residuals')
plt.xlabel('Residuals')
plt.ylabel('Density')
plt.grid(True)
hist_plot_path = 'task4/hist_residuals.png'
plt.savefig('task4/hist_residuals.png')

plt.figure(figsize=(10, 5), dpi=433)
plt.scatter(range(len(residuals)), residuals, alpha=0.7, color='blue')
plt.title('Scatter Plot of AR(p) Model Residuals')
plt.xlabel('Index')
plt.ylabel('Residuals')
plt.grid(True)
plt.savefig('task4/scatter_residuals.png')

chi_squared_value, p_value = stats.normaltest(residuals)

ar_results = {
    'selected_p': p,
    'rmse_ar': rmse_ar,
    'chi_squared_value': chi_squared_value,
    'p_value_chi_squared_test': p_value
}

print(ar_results)
