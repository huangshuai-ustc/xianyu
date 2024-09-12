import pandas as pd
import matplotlib.pyplot as plt
from utils import stationarity
import matplotlib.dates as mdates

file_path = 'air-quality.csv'
air_quality_df = pd.read_csv(file_path)
air_quality_df['Last_Check'] = pd.to_datetime(air_quality_df['Last_Check'])
air_quality_df.set_index('Last_Check', inplace=True)
fields_of_interest = ['Temp__F_', 'Humidity____', 'Pressure__mbar_', 'PM_2_5_30_Minute_Avg_', 'PM_2_5_1_Hour_Avg_']


fig, axes = plt.subplots(nrows=len(fields_of_interest), ncols=1, dpi=120, figsize=(10, 10))
for i, field in enumerate(fields_of_interest):
    plt.figure(figsize=(12, 3), dpi=433)
    plt.plot(air_quality_df[field].dropna(), color='blue', linewidth=1)
    plt.title(field)
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gca().xaxis.set_minor_locator(mdates.MonthLocator())
    # plt.show()

adf_test_results = {}
for field in fields_of_interest:
    adf_test_results[field] = stationarity(air_quality_df[field].dropna())

# plt.show()
for field, result in adf_test_results.items():
    print(f'ADF Test Results for {field}:')
    print(result)
    print('\n')
