import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from utils import exponential_smoothing, train_data, test_data


predicted_test_sma = [train_data.iloc[-1]] * len(test_data)
predicted_test_es = [exponential_smoothing(train_data, 0.9)[-1]] * len(test_data)
ar_model = AutoReg(train_data, lags=4).fit()
predicted_test_ar = ar_model.predict(start=len(train_data), end=len(train_data) + len(test_data) - 1, dynamic=False)


def plot_predictions_vs_actual(test_data, predictions, model_name, plot_color):
    plt.figure(figsize=(10, 5))
    plt.plot(test_data.index, test_data, label='Actual Test Data', alpha=0.7)
    plt.plot(test_data.index, predictions, label=f'{model_name} Predictions', color=plot_color, alpha=0.7)
    plt.title(f'{model_name} Model - Predictions vs Actual Test Data')
    plt.xlabel('Index')
    plt.ylabel('Temperature (F)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'task5/{model_name.lower().replace(" ", "_")}_predictions_vs_actual.png')
    plt.close()


plot_predictions_vs_actual(test_data, predicted_test_sma, 'Simple Moving Average', 'red'),
plot_predictions_vs_actual(test_data, predicted_test_es, 'Exponential Smoothing', 'green'),
plot_predictions_vs_actual(test_data, predicted_test_ar, 'AR Model', 'blue')

