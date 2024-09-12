<h1 align='center'>Project 3 - Regression and Forecasting</h1>

## Task 1. Basic Statistic Analysis

### 1.1 Calculate: histogram, mean, variance.

histgram

<img src="https://raw.githubusercontent.com/fjwyz/images/main/pic/Temp__F_s.jpg" alt="Temp__F_" />

![Humidity____](https://raw.githubusercontent.com/fjwyz/images/main/pic/Humidity____s.jpg)

![Pressure__mbar_s](https://raw.githubusercontent.com/fjwyz/images/main/pic/Pressure__mbar_s.jpg)

![PM_2_5_30_Minute_Avg_](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_30_Minute_Avg_s.jpg)

![PM_2_5_1_Hour_Avg_](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_1_Hour_Avg_s.jpg)

|      | $x_1$  | $x_2$  | $x_3$   | $x_4$ | $x_5$ |
| ---- | :----- | ------ | ------- | ----- | ----- |
| mean | 72.29  | 57.42  | 1006.50 | 10.57 | 10.62 |
| var  | 132.17 | 139.73 | 41.93   | 46.63 | 45.22 |

其中$x_1$ is $Temp\_\_F\_$，$x_2$ is $Humidity\_\_\_\_$，$x_3$ is $Pressure\_\_mbar\_$，$x_4$ is $PM\_2\_5\_30\_Minute\_Avg\_$，$x_5$ is $PM\_2\_5\_1\_Hour\_Avg\_$

### 1.2  Remove outliers

```python
def drop_outlines(data):
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    outliers = data[(data < q1 - 1.5 * iqr) | (data > q3 + 1.5 * iqr)]
    df.drop(outliers.index, inplace=True)
```

使用上述函数去除异常值，其中判断指标是`(data < q1 - 1.5 * iqr) | (data > q3 + 1.5 * iqr)`，1000条数据共去除60行异常值。

![image-20240305173736541](https://raw.githubusercontent.com/fjwyz/images/main/pic/image-20240305173736541.png)

### 1.3 Calculate the correlation matrix

|                       | $x_1$  | $x_2$  | $x_3$  | $x_4$  | $x_5$  | $y$   |
| --------------------- | ------ | ------ | ------ | ------ | ------ | ----- |
| Temp__F_              | 1      | 0.033  | -0.184 | 0.432  | 0.458  | 0.705 |
| Humidity____          | 0.033  | 1      | -0.141 | 0.504  | 0.488  | 0.305 |
| Pressure__mbar_       | -0.184 | -0.141 | 1      | -0.081 | -0.084 | 0.046 |
| PM_2_5_30_Minute_Avg_ | 0.432  | 0.504  | -0.081 | 1      | 0.993  | 0.688 |
| PM_2_5_1_Hour_Avg_    | 0.458  | 0.488  | -0.084 | 0.993  | 1      | 0.718 |
| PM_2_5_24_Hour_Avg_   | 0.705  | 0.305  | 0.046  | 0.688  | 0.718  | 1     |

### 1.4 Draw conclusions

|       | $x_1$                | $x_2$                | $x_3$         | $x_4$                | $x_5$                | $y$                  |
| ----- | -------------------- | -------------------- | ------------- | -------------------- | -------------------- | -------------------- |
| $x_1$ | 1                    | weak positive        | weak negative | correlation positive | correlation positive | strong positive      |
| $x_2$ | weak positive        | 1                    | weak negative | correlation positive | correlation positive | weak positive        |
| $x_3$ | weak negative        | weak negative        | 1             | weak negative        | weak negative        | weak positive        |
| $x_4$ | correlation positive | correlation positive | weak negative | 1                    | strong positive      | correlation positive |
| $x_5$ | correlation positive | correlation positive | weak negative | strong positive      | 1                    | strong positive      |
| $y$   | strong positive      | weak positive        | weak positive | correlation positive | strong positive      | 1                    |

In this table, weak is weak correlation; strong is strong correlation; positive is positive correlation; negative is negative correlation; single correlation means that the two are correlated.

## Task 2. Simple Linear Regression

### 2.1 Determine the estimates for $a_0$, $a_1$, and $σ^2$

|       | $a_0$  | $a_1$ | $σ^2$ |
| ----- | ------ | ----- | ----- |
| $x_1$ | -9.16  | 0.29  | 0.69  |
| $x_2$ | 4.32   | 0.13  | 0.76  |
| $x_3$ | -31.76 | 0.04  | 30.65 |
| $x_4$ | 6.17   | 0.51  | 0.22  |
| $x_5$ | 5.83   | 0.54  | 0.21  |

### 2.2 The p-values, R-squared, and adjusted R-squared

|       | $p-values$ | $R-squared$ | $adjusted R-squared$ |
| ----- | ---------- | ----------- | -------------------- |
| $x_1$ | 8.11e-37   | 0.497       | 0.496                |
| $x_2$ | 1.49e-08   | 0.093       | 0.092                |
| $x_3$ | 0.30       | 0.002       | 0.001                |
| $x_4$ | 1.90e-126  | 0.473       | 0.472                |
| $x_5$ | 1.70e-121  | 0.515       | 0.514                |

### 2.3 Plot the regression line against the data

![Temp__F_ linear regression](https://raw.githubusercontent.com/fjwyz/images/main/pic/Temp__F_ linear regression.jpg)

![Humidity____ linear regression](https://raw.githubusercontent.com/fjwyz/images/main/pic/Humidity____ linear regression.jpg)

![Pressure__mbar_ linear regression](https://raw.githubusercontent.com/fjwyz/images/main/pic/Pressure__mbar_ linear regression.jpg)

![PM_2_5_30_Minute_Avg_ linear regression](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_30_Minute_Avg_ linear regression.jpg)

![PM_2_5_1_Hour_Avg_ linear regression](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_1_Hour_Avg_ linear regression.jpg)

### 2.4 Do a residuals analysis

#### （a）Q-Q plot and  residuals histogram

For $x_1$: 

![Temp__F__qq](https://raw.githubusercontent.com/fjwyz/images/main/pic/Temp__F__qq.jpg)

由图可得，变量$x_1$基本呈正态分布

![Temp__F__resid_hist](https://raw.githubusercontent.com/fjwyz/images/main/pic/Temp__F__resid_hist.jpg)

`Kolmogorov-Smirnov test: (0.0769028441155084, 0.0009999999999998899)`

卡方检验得基本呈正态分布

For $x_2$: 

![Humidity_____qq](https://raw.githubusercontent.com/fjwyz/images/main/pic/Humidity_____qq.jpg)

由图可得，变量$x_1$基本呈正态分布

![Humidity_____resid_hist](https://raw.githubusercontent.com/fjwyz/images/main/pic/Humidity_____resid_hist.jpg)

`Kolmogorov-Smirnov test: (0.12948275942035553, 0.0009999999999998899)`

卡方检验得基本呈正态分布

For $x_3$: 

![Pressure__mbar__qq](https://raw.githubusercontent.com/fjwyz/images/main/pic/Pressure__mbar__qq.jpg)

由图可得，变量$x_1$基本呈正态分布

![Pressure__mbar__resid_hist](https://raw.githubusercontent.com/fjwyz/images/main/pic/Pressure__mbar__resid_hist.jpg)

`Kolmogorov-Smirnov test: (0.11601104022751668, 0.0009999999999998899)`

卡方检验得基本呈正态分布

For $x_4$: 

![PM_2_5_30_Minute_Avg__qq](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_30_Minute_Avg__qq.jpg)

由图可得，变量$x_1$基本呈正态分布

![PM_2_5_30_Minute_Avg__resid_hist](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_30_Minute_Avg__resid_hist.jpg)

`Kolmogorov-Smirnov test: (0.09349277645364218, 0.0009999999999998899)`

卡方检验得基本呈正态分布

For $x_5$: 

![PM_2_5_1_Hour_Avg__qq](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_1_Hour_Avg__qq.jpg)

由图可得，变量$x_1$基本呈正态分布

![PM_2_5_1_Hour_Avg__resid_hist](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_1_Hour_Avg__resid_hist.jpg)

`Kolmogorov-Smirnov test: (0.09512262038967512, 0.0009999999999998899)`

卡方检验得基本呈正态分布

#### （b）scatter plot of the residuals

![Temp__F__resid_scatter](https://raw.githubusercontent.com/fjwyz/images/main/pic/Temp__F__resid_scatter.jpg)

![Humidity_____resid_scatter](https://raw.githubusercontent.com/fjwyz/images/main/pic/Humidity_____resid_scatter.jpg)

![Pressure__mbar__resid_scatter](https://raw.githubusercontent.com/fjwyz/images/main/pic/Pressure__mbar__resid_scatter.jpg)

![PM_2_5_30_Minute_Avg__resid_scatter](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_30_Minute_Avg__resid_scatter.jpg)

![PM_2_5_1_Hour_Avg__resid_scatter](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_1_Hour_Avg__resid_scatter.jpg)

### 2.5 Use a higher-order polynomial regression

对$x_1$使用二阶非线性拟合得到的拟合表达式为
$$
y = -0.0034{x_1^2}-0.0200x_1+7.91
$$
$r^2$为0.26

对$x_2$使用二阶非线性拟合得到的拟合表达式为
$$
y = -0.0046{x_2^2}-0.0352x_2+16.078
$$
$r^2$为0.01

对$x_3$使用二阶非线性拟合得到的拟合表达式为
$$
y = -0.038{x_3^2}+77.13x_3-38843.26
$$
$r^2$为0.005

对$x_4$使用二阶非线性拟合得到的拟合表达式为
$$
y = 0.016{x_4^2}+0.1167x_4+7.8820
$$
$r^2$为0.24

对使用二阶非线性拟合得到的拟合表达式为
$$
y = -0.0195{x_5^2}-0.0720x_5+7.87
$$
$r^2$为0.29

### 2.6 Comment on your results

在使用自定义函数去除离群点后，留下来的数据在分布上均与正态分布相似，为正态分布的左偏或右偏。

对$x_1$，得到的拟合表达式为
$$
y = -9.16+0.29x_1+0.69
$$
对$x_2$，得到的拟合表达式为
$$
y = 4.32+0.13x_2+0.76
$$
对$x_3$，得到的拟合表达式为
$$
y = -31.76+0.04x_3+30.65
$$
对$x_4$，得到的拟合表达式为
$$
y = 6.17+0.51x_4+0.22
$$
对$x_5$，得到的拟合表达式为
$$
y = 5.83+0.54x_5+0.21
$$
对$x_1$，使用二阶一元非线性回归拟合后得到的$r^2$有一定降低，说明相比来说$x_1$与$y$的关系更接近一元线性回归。

对$x_2$，$x_3$，$x_4$，$x_5$也是一样。

## Task 3:  Multi-variable Linear Regression

### 3.1 Determine the values for all the coefficients, and $σ^2$



测试发现不含有常数项系数得到的$r^2$更大，拟合效果更好，最终拟合曲线公式如下：
$$
y = 0.185x_1+0.033x_2-0.007x_3-0.881x_4+1.243x_5
$$
$σ^2$为0.008.

### 3.2 Identify which independent variables need to be removed

多元线性回归的p值,$r^2$,调整$r^2$分别为:  3.13e-86, 0.9578, 0.9576

该值说明拟合效果非常好，没有变量需要删除。

### 3.3 Do a residuals analysis:

#### （a）Q-Q plot and  residuals histogram

![multi_qq](https://raw.githubusercontent.com/fjwyz/images/main/pic/multi_qq.jpg)

由图可得，变量们基本呈正态分布

![muti_resid_hist](https://raw.githubusercontent.com/fjwyz/images/main/pic/muti_resid_hist.jpg)

`Kolmogorov-Smirnov test: (0.09899924133384891, 0.0009999999999998899)`

卡方检验得基本呈正态分布

#### （b）scatter plot of the residuals

![multi_resid_scatter](https://raw.githubusercontent.com/fjwyz/images/main/pic/multi_resid_scatter.jpg)

### 3.4 Comment on your results

**原假设（H0）**是：$y$与$x_i$**不存在**多元线性相关的关系。

**备择假设（Ha）**是：$y$与$x_i$**存在**多元线性相关的关系。

从多元线性拟合的结果来看，其置信度p-value=3.13e-86<0.05，于是拒绝原假设，支持备择假设$y$与$x_i$**存在**多元线性相关的关系。

而后观察$r^2$,调整$r^2$分别为:  0.9578, 0.9576，统计学中$r^2$越接近1说明拟合结果越好，那么该多元线性拟合的结果很好。

从相关系数与$r^2$综合考虑，所有变量均在多元线性回归中起作用，即不存在无效变量，不需要删除列。

从相关矩阵来看，变量的系数的正负与相关矩阵表中的正负相关性一致。

拟合得到的表达式为：
$$
y = 0.185x_1+0.033x_2-0.007x_3-0.881x_4+1.243x_5
$$