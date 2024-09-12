import pandas as pd
import numpy as np

df = pd.read_excel('2010.xlsx') #修改

GO = df.iloc[7:-7, 34].tolist()
ERR = df.iloc[7:-7, 33].tolist()
d = df.iloc[7:-7, 3:20] #中间品矩阵数据
d = np.array(d).tolist()
X = df.iloc[7:-7, 30].tolist()  # 出口EX
M = df.iloc[7:-7, 32].tolist()  # 进口IM
S = df.iloc[7:-7, 28].tolist()  # 存货增加FU202
Y = [GO[i] - ERR[i] for i in range(len(GO))]
C = df.iloc[7:-7, 26].tolist()  # 合计TC
K = df.iloc[7:-7, 29].tolist()  # 合计GCF
TI = df.iloc[-1, 3:20].tolist()
F = [C[i] + K[i] - S[i] for i in range(len(C))]

D = [[0] * 18 for i in range(18)]
for i in range(len(d)):
    for j in range(len(d[0])):
        D[i][j] = (d[i][j] / TI[j]) * GO[i] / (GO[i] - X[i] + M[i] - S[i])
D = np.array(D)
D = np.matrix(D)
E = np.eye(18)
E = np.matrix(E)
F = np.matrix(F).T
fenzi = ((E - D) @ (E - D)).I @ F
result = [float(fenzi[i] / GO[i]) for i in range(18)]
df_result = pd.DataFrame()
df_result['产业编号'] = df.iloc[7:-7, 1]
df_result['产业名称'] = df.iloc[7:-7, 2]
df_result['产业上游度'] = result
df_result.to_excel('2020_result.xlsx', header=False, index=False)
