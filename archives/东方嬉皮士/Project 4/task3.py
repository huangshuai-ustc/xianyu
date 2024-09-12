import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import exponential_smoothing, calculate_metrics, train_data, test_data

a_metrics = {}
for a in np.arange(0.1, 1.0, 0.1):
    smoothed = exponential_smoothing(train_data, a)
    rmse, _ = calculate_metrics(train_data[1:], smoothed[1:])  # Ignoring the first prediction
    a_metrics[a] = rmse

a_metrics_df = pd.DataFrame(list(a_metrics.items()), columns=['a', 'RMSE'])
print(a_metrics_df)

best_a = a_metrics_df.loc[a_metrics_df['RMSE'].idxmin(), 'a']
smoothed_train = exponential_smoothing(train_data, best_a)
smoothed_test = [smoothed_train[-1]] * len(test_data)
rmse_test_exponential = calculate_metrics(test_data, smoothed_test)[0]

plt.figure(figsize=(10, 5), dpi=433)
plt.plot(a_metrics_df['a'], a_metrics_df['RMSE'], marker='o')
plt.title('RMSE vs a for Exponential Smoothing')
plt.xlabel('a')
plt.ylabel('RMSE')
plt.grid(True)

plt.savefig('task3/rmse_vs_a.png')

plt.figure(figsize=(14, 7), dpi=433)
plt.plot(train_data.index, train_data, label='Actual', alpha=0.7)
plt.plot(train_data.index, smoothed_train, label='Smoothed', alpha=0.7)
plt.title(f'Exponential Smoothing Predicted vs Actual Values (a={best_a})')
plt.xlabel('Index')
plt.ylabel('Temperature (F)')
plt.legend()
plt.grid(True)
plt.savefig('task3/smoothed_vs_actual.png')

exponential_smoothing_results = {
    'best_a': best_a,
    'rmse_test_exponential': rmse_test_exponential,
}

print(exponential_smoothing_results)
