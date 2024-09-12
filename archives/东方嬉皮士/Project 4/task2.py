import pandas as pd
import matplotlib.pyplot as plt
from utils import moving_average, calculate_metrics, train_data, test_data

metrics = {}

for k in range(2, 51):
    predicted_values = moving_average(train_data, k)
    actual_values = train_data[k - 1:]
    rmse, mape = calculate_metrics(actual_values, predicted_values)
    metrics[k] = {'RMSE': rmse, 'MAPE': mape}

metrics_df = pd.DataFrame.from_dict(metrics, orient='index')
best_k_rmse = metrics_df['RMSE'].idxmin()
best_k_mape = metrics_df['MAPE'].idxmin()
best_k = best_k_rmse if metrics_df.loc[best_k_rmse, 'RMSE'] < metrics_df.loc[best_k_mape, 'RMSE'] else best_k_mape
predicted_train = moving_average(train_data, best_k)
predicted_test = [predicted_train[-1]] * len(test_data)
rmse_test, mape_test = calculate_metrics(test_data, predicted_test)
results = {
    'metrics_per_k': metrics_df.to_dict(),
    'best_k': best_k,
    'rmse_test_set': rmse_test,
    'mape_test_set': mape_test
}

plt.figure(figsize=(14, 7), dpi=433)
plt.subplot(1, 2, 1)
plt.plot(metrics_df.index, metrics_df['RMSE'])
plt.title('RMSE vs k')
plt.xlabel('k')
plt.ylabel('RMSE')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(metrics_df.index, metrics_df['MAPE'])
plt.title('MAPE vs k')
plt.xlabel('k')
plt.ylabel('MAPE')
plt.grid(True)
plt.savefig('task2/metrics_vs_k.png')

plt.figure(figsize=(14, 7), dpi=433)
aligned_actual_values = train_data[best_k - 1:]
aligned_predicted_values = predicted_train

plt.plot(aligned_actual_values.index, aligned_actual_values, label='Actual', alpha=0.7)
plt.plot(aligned_actual_values.index, aligned_predicted_values, label='Predicted', alpha=0.7)
plt.title(f'Predicted vs Actual Values using k={best_k}')
plt.xlabel('Index')
plt.ylabel('Temperature (F)')
plt.legend()
plt.grid(True)
plt.savefig('task2/predicted_vs_actual.png')

print(results)

