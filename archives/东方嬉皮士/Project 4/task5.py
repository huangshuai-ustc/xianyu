import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.ar_model import AutoReg
from utils import exponential_smoothing, calculate_metrics2, train_data, test_data

predicted_test_sma = [train_data.iloc[-1]] * len(test_data)
rmse_test_sma = calculate_metrics2(test_data, predicted_test_sma)
predicted_test_es = [exponential_smoothing(train_data, 0.9)[-1]] * len(test_data)
rmse_test_es = calculate_metrics2(test_data, predicted_test_es)
lags_pacf = pacf(train_data, nlags=40, method='ols')
p = np.where(lags_pacf < 0.05)[0][1] - 1
ar_model = AutoReg(train_data, lags=p).fit()
start_index = len(train_data)
end_index = start_index + len(test_data) - 1
predicted_test_ar = ar_model.predict(start=start_index, end=end_index, dynamic=False)
rmse_test_ar = calculate_metrics2(test_data, predicted_test_ar)

rmse_results = {
    'simple_moving_average': rmse_test_sma,
    'exponential_smoothing': rmse_test_es,
    'AR_model': rmse_test_ar
}

best_model = min(rmse_results, key=rmse_results.get)
best_model_rmse = rmse_results[best_model]

print(f"RMSE for Simple Moving Average on test set: {rmse_test_sma}")
print(f"RMSE for Exponential Smoothing on test set: {rmse_test_es}")
print(f"RMSE for AR(p) Model on test set: {rmse_test_ar}")
print(f"Best model: {best_model} with RMSE: {best_model_rmse}")
