<h1 align='center'>Data Acquisition and Analytics</h1>

本次作业挑选了空气质量检测数据的五个指标作为$x_i$，一个指标为$y$

## Task2

### 2.1 Descriptive statistics

选取了前100条数据进行分析，其统计指标见下表，其中$x_1$ is $Temp\_\_F\_$，$x_2$ is $Humidity\_\_\_\_$，$x_3$ is $Pressure\_\_mbar\_$，$x_4$ is $PM\_2\_5\_30\_Minute\_Avg\_$，$x_5$ is $PM\_2\_5\_1\_Hour\_Avg\_$

|      | $x_1$ | $x_2$  | $x_3$   | $x_4$ | $x_5$ |
| ---- | :---- | ------ | ------- | ----- | ----- |
| mean | 86.71 | 56.45  | 1005.46 | 18.97 | 19.00 |
| var  | 47.96 | 132.45 | 5.05    | 41.51 | 36.16 |
| 1/4  | 81.0  | 44.0   | 1003.70 | 13.58 | 14.20 |
| 2/4  | 85.0  | 62.5   | 1004.69 | 18.24 | 17.7  |
| 3/4  | 93.0  | 66.0   | 1006.69 | 21.22 | 20.26 |
| IQR  | 12.0  | 12.0   | 2.99    | 7.64  | 6.06  |
| max  | 98    | 70     | 1011.93 | 33.57 | 32.71 |
| min  | 77    | 36     | 1002.78 | 11.08 | 12.54 |

### 2.2 Probability Mass Function (PMF)

![](https://raw.githubusercontent.com/fjwyz/images/main/pic/Temp__F_.jpg)

![Humidity____](https://raw.githubusercontent.com/fjwyz/images/main/pic/Humidity____.jpg)

![Pressure__mbar_](https://raw.githubusercontent.com/fjwyz/images/main/pic/Pressure__mbar_.jpg)

![PM_2_5_30_Minute_Avg_](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_30_Minute_Avg_.jpg)

![PM_2_5_1_Hour_Avg_](https://raw.githubusercontent.com/fjwyz/images/main/pic/PM_2_5_1_Hour_Avg_.jpg)

### 2.3 Analysis Report: SOCS Framework

#### 2.3.1 Shape

对于$x_1$：其方差较高，四分位数的间隔较为平均，结合PMF图可以分析出，数据在最大值和最小值附近分布的比较多，在均值附近分布的比较少，数据呈U型分布。

对于$x_2$：其方差极大，四分位数的分布也不均匀，均值与中位数的距离较远，结合PMF图可以分析出，数据在较小部分和中间偏左和最右侧均有起伏，说明数据的分布是普遍在中位数的左边。

对于$x_3$：其方差最小，四分位数之间的差距不大，均值与中位数较为接近，结合PMF图可以分析出，数据呈钟型分布，也就是在中位数附近的数据多，离中位数越远越少。

对于$x_4$：其方差较高，四分位数之间的差距较大，均值与中位数较为接近，结合PMF图可以分析出，数据分布较为均匀。

对于$x_5$：与$x_4$相似，其方差较高，四分位数之间的差距较大，均值与中位数较为接近，结合PMF图可以分析出，数据分布较为均匀。

#### 2.3.2 Outliers

对于$x_1$：根据PMF图可以得出，数据不存在离群点

对于$x_2$：根据PMF图可以得出，数据不存在离群点

对于$x_3$：根据PMF图可以得出，数据不存在离群点

对于$x_4$：根据PMF图可以得出，数据不存在离群点

对于$x_5$：根据PMF图可以得出，数据不存在离群点

#### 2.3.3 Center

对于$x_1$：其平均值为86.71，其中位数为85.0，平均值大于中位数，数据呈左偏态分布，但由于二者差距较小，故对数据分析的影响不大。

对于$x_2$：其平均值为56.45，其中位数为62.5，平均值小于中位数，数据集呈右偏态分布，且由于二者差距较大，故对数据分析有一定影响。

对于$x_3$：其平均值为1005.46，其中位数为1004.69，平均值大于中位数，数据呈左偏态分布，但由于二者差距较小，故对数据分析的影响不大。

对于$x_4$：其平均值为18.97，其中位数为18.24，平均值大于中位数，数据呈左偏态分布，但由于二者差距较小，对数据分析的影响不大。

对于$x_5$：其平均值为19.00，其中位数为17.7，平均值大于中位数，数据呈左偏态分布，但由于二者差距较小，故对数据分析的影响不大。

#### 2.3.4 Spread

上表给出了$x_i$的最大最小值，以及IQR和方差等指标，从上述指标可以得出结论，$x_1$和$x_3$在数据的分布上非常均匀，它们的变化带给$y$的影响很小，而$x_2$、$x_4$、$x_5$在数据的分布上异常混乱，包括较大的方差，和IQR，它们的变化会对$y$造成较大影响。

## Task3 Data Visualization

select 1000 samples for analysising

### 3.1  boxplot for $x_i$

![x1](https://raw.githubusercontent.com/fjwyz/images/main/pic/x1.jpg)

![x2](https://raw.githubusercontent.com/fjwyz/images/main/pic/x2.jpg)

![x3](https://raw.githubusercontent.com/fjwyz/images/main/pic/x3.jpg)

![x4](https://raw.githubusercontent.com/fjwyz/images/main/pic/x4.jpg)

![x5](https://raw.githubusercontent.com/fjwyz/images/main/pic/x5.jpg)

### 3.2  Scatter plots with column $y$ and $x_i$

![x1_y](https://raw.githubusercontent.com/fjwyz/images/main/pic/x1_y.jpg)

![x2_y](https://raw.githubusercontent.com/fjwyz/images/main/pic/x2_y.jpg)

![x3_y](https://raw.githubusercontent.com/fjwyz/images/main/pic/x3_y.jpg)

![x4_y](https://raw.githubusercontent.com/fjwyz/images/main/pic/x4_y.jpg)

![x5_y](https://raw.githubusercontent.com/fjwyz/images/main/pic/x5_y.jpg)

### 3.3 the density curve of $y$

![density curve of PM_2_5_24_Hour_Avg_](https://raw.githubusercontent.com/fjwyz/images/main/pic/density curve of PM_2_5_24_Hour_Avg_.png)

### 3.4 Analysis and interpretation

#### (a) Analyze the findings from the boxplots, scatter plots, and density curve.

##### boxplots

>for $x_1$:数据较为均匀，没有离群点。
>
>for $x_2$:数据较为均匀，在数据值较小的位置有少量离群点。
>
>for $x_3$:数据较为分散，有大量离群点集中在数据值小于995的范围。
>
>for $x_4$:数据较为均匀，有少量离群点出现在数据值大于30的范围。
>
>for $x_5$:数据值集中分布在较小的部分，有少量离群点出现在数据值较大的范围。

##### scatter plots

>for $x_1$:$x_1$与$y$整体呈正相关，也就是随着$x_1$的增大，$y$也逐渐增大。
>
>for $x_2$:从图像来看，无论$x_2$取何值，$y$的取值范围都很大，说明$x_2$与$y$的关系不大。
>
>for $x_3$:$x_3$与$y$整体呈现较弱的正相关性。
>
>for $x_4$:$x_4$与$y$整体呈正相关，但相关性有限，也就是随着$x_4$的增大，$y$可能会增大。
>
>for $x_5$:与$x_4$类似，$x_5$与$y$整体呈正相关，但相关性有限，也就是随着$x_5$的增大，$y$可能会增大。

##### density curve

>从$y$的数据密度来看，其数据呈正偏的钟型分布，数据大量分布在中位数以及中位数偏左的部分。

#### (b) Discuss key observations

​	从boxplots可以看出，数据存在不少离群点，这对$x_i$与$y$的相关性分析带来了很大误差，即散点图中的数据已经无法真实的反映出$x_i$与$y$之间的关系。

​	从数据的分布来看，大部分数据还是以钟型分布或钟型的偏态分布呈现，少部分数据由于离群点的出现不具备显著的统计特征，这说明在分析之前预处理掉不合理的数据的重要性。

#### (c) Reflection

​	通过对数据的可视化观察，可以在分析之前就得出数据的特征。脏数据对于数据分析的影响是极大的，并且在分析的时候程序并不会告诉我们某些值可能是异常的会导致错误的结果，这时候就需要我们提前观察数据的特征，主动处理数据中的不合理的部分，比如剔除离群点，填充缺失值，去除重复值等。