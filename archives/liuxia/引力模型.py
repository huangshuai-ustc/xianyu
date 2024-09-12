import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression  # 导入线性回归类
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split  # 数据集的划分

df = pd.read_excel('./1-2.xlsx')
number_of_inbound_tourists = df['入境旅游游客人数/万人'].apply(lambda x: np.log(x))
df = df.iloc[:, 3:]
for i in list(df.columns):
    Max = np.max(df[i])
    Min = np.min(df[i])
    df[i] = round(((df[i] - Min) / (Max - Min) + 1), 2)
df = df.apply(lambda x: np.log(x))
x = df

# 3. 数据集划分 ( 训练集 + 测试集)
x_train, x_test, y_train, y_test = train_test_split(x, number_of_inbound_tourists, test_size=0.2, random_state=22)
lr = LinearRegression()
lr.fit(x_train, y_train)
print("权重w:", lr.coef_)
print('截距b:', lr.intercept_)
y_pre = lr.predict(x_test)
print("真实值:", y_test)
print("预测值:", y_pre)
tolerance = 1
y_test_within_tolerance = abs(y_test - y_pre) <= tolerance
score = accuracy_score(y_test_within_tolerance, [True] * len(y_test_within_tolerance))
print("模型准确率:", score)
