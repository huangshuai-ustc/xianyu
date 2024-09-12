<h1 align='center'>Project 4 - Forecasting</h1>

## Task 1. Check for Stationarity and Non-Stationary Properties

### 1.1 Plot the entire time series

line charts and stability test results about $x_i$

![Temp_F_](https://raw.githubusercontent.com/fjwyz/images/main/pic/Temp_F_.png)

* ADF Test Results for Temp\_\_F\_

```
Test Statistic                    -4.772090
p-value                            0.000061
#Lags Used                        40.000000
Number of Observations Used    12448.000000
Critical Value (1%)               -3.430875
Critical Value (5%)               -2.861772
Critical Value (10%)              -2.566894
```

![Humidity__](https://raw.githubusercontent.com/fjwyz/images/main/pic/Humidity__.png)

* ADF Test Results for Humidity____

```
Test Statistic                -1.470845e+01
p-value                        2.872601e-27
#Lags Used                     2.900000e+01
Number of Observations Used    1.245900e+04
Critical Value (1%)           -3.430875e+00
Critical Value (5%)           -2.861772e+00
Critical Value (10%)          -2.566893e+00
```

![Pressure_mbar_](https://raw.githubusercontent.com/fjwyz/images/main/pic/Pressure_mbar_.png)

* ADF Test Results for Pressure__mbar\_

```
Test Statistic                -1.348810e+01
p-value                        3.144924e-25
#Lags Used                     2.400000e+01
Number of Observations Used    1.246400e+04
Critical Value (1%)           -3.430875e+00
Critical Value (5%)           -2.861772e+00
Critical Value (10%)          -2.566893e+00
```

![PM_2_5_30_Minute_Avg_](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_30_Minute_Avg_.png)

* ADF Test Results for PM_2_5_30_Minute_Avg_

```
Test Statistic                -1.102868e+01
p-value                        5.741085e-20
#Lags Used                     3.000000e+01
Number of Observations Used    1.245800e+04
Critical Value (1%)           -3.430875e+00
Critical Value (5%)           -2.861772e+00
Critical Value (10%)          -2.566894e+00
```

![PM_2_5_1_Hour_Avg_](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_1_Hour_Avg_.png)

* ADF Test Results for PM_2_5_1_Hour_Avg_

```
Test Statistic                -1.087675e+01
p-value                        1.325691e-19
#Lags Used                     3.000000e+01
Number of Observations Used    1.245800e+04
Critical Value (1%)           -3.430875e+00
Critical Value (5%)           -2.861772e+00
Critical Value (10%)          -2.566894e+00
```

### 1.2 & 1.3 To be stationary or not to be stationary

The entire time series has been plotted for each field. The null hypothesis is set to assume that all data are stationary. The Augmented Dickey-Fuller (ADF) test has been conducted to test the stationarity of each series. The results of the ADF tests are:

For the **Temp\_\_F\_** , the test statistic is -4.31 with a p-value of 0.000429. This means that the time series is stationary at the 1% significance level since the test statistic is less than all three critical values. 

For the **Humidity\_\_** , the test statistic is -11.72 with a p-value close to 0. This indicates that the time series is stationary at the 1% significance level. 

For the **Pressure__mbar_** field, the test statistic is -10.76 with a p-value close to 0. This indicates that the time series is stationary at the 1% significance level. 

For the **PM_2_5_30_Minute_Avg_** field, the test statistic is -9.29 with a p-value of about 1.16e-15. This means that the time series is stationary at the 1% significance level. 

For the **PM_2_5_1_Hour_Avg_** field, the test statistic is -9.14 with a p-value of about 2.88e-15. This indicates that the time series is stationary at the 1% significance level. 

The ADF test results suggest that the time series data for all fields are stationary because their p-values are all below 0.05, and the test statistics are lower than the 1%, 5%, and 10% critical values. Therefore, based on the ADF test results, we have no reason to reject the null hypothesis, which is that the series are stationary.

Since the series are already stationary, there is no need for differencing, seasonal differencing, or log transformation to further check for stationarity properties. Please let me know if further analysis is required or if there are any other questions.

## Task 2 Fit a simple moving average model (using the training set)

About **Temp\_\_F\_** :

### 2.1 & 2.2 & 2.3 Calculate the error (RMSE) and (MAPE) by varying *k*

 `note: key: value is window size: error`

```
'RMSE': {2: 2.37, 3: 3.03, 4: 3.54, 5: 3.97, 6: 4.38, 7: 4.73, 8: 5.07, 9: 5.38, 10: 5.66, 11: 5.92, 12: 6.15, 13: 6.36, 14: 6.54, 15: 6.7, 16: 6.84, 17: 6.96, 18: 7.07, 19: 7.16, 20: 7.24, 21: 7.31, 22: 7.36, 23: 7.42, 24: 7.47, 25: 7.52, 26: 7.57, 27: 7.62, 28: 7.67, 29: 7.73, 30: 7.8, 31: 7.86, 32: 7.93, 33: 8.0, 34: 8.08, 35: 8.15, 36: 8.22, 37: 8.28, 38: 8.34, 39: 8.4, 40: 8.46, 41: 8.51, 42: 8.56, 43: 8.6, 44: 8.64, 45: 8.67, 46: 8.7, 47: 8.73, 48: 8.76, 49: 8.78, 50: 8.81}
'MAPE': {2: 0.02, 3: 0.02, 4: 0.03, 5: 0.04, 6: 0.04, 7: 0.05, 8: 0.05, 9: 0.06, 10: 0.06, 11: 0.06, 12: 0.07, 13: 0.07, 14: 0.07, 15: 0.07, 16: 0.08, 17: 0.08, 18: 0.08, 19: 0.08, 20: 0.08, 21: 0.08, 22: 0.08, 23: 0.09, 24: 0.09, 25: 0.09, 26: 0.09, 27: 0.09, 28: 0.09, 29: 0.09, 30: 0.09, 31: 0.09, 32: 0.09, 33: 0.09, 34: 0.09, 35: 0.09, 36: 0.1, 37: 0.1, 38: 0.1, 39: 0.1, 40: 0.1, 41: 0.1, 42: 0.1, 43: 0.1, 44: 0.1, 45: 0.1, 46: 0.1, 47: 0.1, 48: 0.1, 49: 0.1, 50: 0.1}
```

### 2.4 Plot RMSE and MAPE vs k and  the predicted values against the original values

image of RMSE and MAPE

![image-20240406134814406](https://raw.githubusercontent.com/fjwyz/images/main/pic/image-20240406134814406.png)

From the graph, it can be seen that *k* based on the lowest RMSE or MAPE value is 2.
The actual and predicted values when *k*=2

![image-20240406135024533](https://raw.githubusercontent.com/fjwyz/images/main/pic/image-20240406135024533.png)

### 2.5 Comment on your results

The analysis of the `Temp__F_` data column with a simple moving average model has been completed. Here are the results:

- The best value of *k* based on the lowest Root Mean Squared Error (RMSE) is 2.
- The RMSE for the test set is approximately 16.66.
- The Mean Absolute Percentage Error (MAPE) for the test set is approximately 18%.

This indicates that using a moving average with *k*=2 was the best simple model based on the training data. However, error metrics indicate that simple moving average models are not very excellent.

## Task 3 Fit an exponential smoothing model

About **Temp\_\_F\_** :

### 3.1 & 3.2 & 3.3 Calculate the error (RMSE) 

|  a   |   RMSE   |
| :--: | :------: |
| 0.1  | 5.908104 |
| 0.2  | 4.436067 |
| 0.3  | 3.505081 |
| 0.4  | 2.822462 |
| 0.5  | 2.271289 |
| 0.6  | 1.789483 |
| 0.7  | 1.341215 |
| 0.8  | 0.903866 |
| 0.9  | 0.461283 |

### 3.4 Plot RMSE vs value a

![image-20240406140620774](https://raw.githubusercontent.com/fjwyz/images/main/pic/image-20240406140620774.png)

From the graph, it can be seen that value **a** based on the lowest RMSE value is 0.9. 

### 3.5 Plot the predicted values against the original values

![image-20240406140827228](https://raw.githubusercontent.com/fjwyz/images/main/pic/image-20240406140827228.png)



### 3.6 Comment on your results

Applying Exponential Smoothing Models to α The best * * a * * value obtained by changing the "Temp_F_" data from 0.1 to 0.9 is 0.9.
The RMSE of the test set using this optimal value is approximately 16.63. This indicates that the exponential smoothing model, like a simple moving average model, has a similar level of prediction error.

## Task 4 Fit an AR(p) Model (use the training set)

About **Temp\_\_F\_** :

### 4.1 Plot PACF  in order to determine the lag k

![image-20240406141523287](https://raw.githubusercontent.com/fjwyz/images/main/pic/image-20240406141523287.png)

From the graph, it can be seen that the most suitable order p is 4.

### 4.2 Estimate the parameters & Plot the predicted values against the original values

RMSE: 4.445441176344763

![image-20240406142118194](https://raw.githubusercontent.com/fjwyz/images/main/pic/image-20240406142118194.png)

### 4.3 Carry out a residual analysis to verify the validity of the model

#### a) Q-Q plot & the residuals histogram

![image-20240406142353239](https://raw.githubusercontent.com/fjwyz/images/main/pic/image-20240406142353239.png)

![hist_residuals](https://raw.githubusercontent.com/fjwyz/images/main/pic/hist_residuals.png)

#### b) Scatter plot

![scatter_residuals](https://raw.githubusercontent.com/fjwyz/images/main/pic/scatter_residuals.png)

### 4.4  Comment on your results

Fit the AR (p) model to the Temp_F_ data from the training set and obtain the following results: 
Based on the PACF graph, the order of model p is selected as 4, which indicates that PACF stops after a lag of 4.
The RMSE predicted by the AR (4) model on the training set is approximately 4.45, which is a significant improvement compared to previous simple and exponential models.
Perform residual analysis, including Q-Q plots, histograms, scatter plots, and χ² Test to check the normality of residuals.
Residual analysis results:
χ² The value obtained from the test is approximately 2324.89, with a p-value of 0.0, indicating that the residual does not follow a normal distribution.

## Task 5 Comparison of all the models (use the testing set)

About **Temp\_\_F\_** :

After fitting the test data, the following results were obtained:

RMSE for Simple Moving Average on test set: 16.660289679407178
RMSE for Exponential Smoothing on test set: 16.63025129834154
RMSE for AR(p) Model on test set: 15.965664473709406
Best model: AR_model with RMSE: 15.965664473709406

After comparing the three training models on the test data, the AR (p) model performed the best, with the lowest RMSE of approximately 15.97.
The AR (p) model has the lowest RMSE in the test set, indicating that it can predict **Temp\_\_F\_** values with smaller errors compared to other models. This indicates that for this specific dataset, the AR (p) model is most suitable for predicting **Temp\_\_F\_** values because it takes into account the temporal correlation in the data.