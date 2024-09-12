import pandas as pd
import numpy as np

df = pd.read_excel('2015.xlsx')

GO = df.iloc[7:-7, 58].tolist()
ERR = df.iloc[7:-7, 57].tolist()
d = df.iloc[7:-7, 3:45]
d = np.array(d).tolist()
X = df.iloc[7:-7, 54].tolist()  # 出口EX
M = df.iloc[7:-7, 56].tolist()  # 进口IM
S = df.iloc[7:-7, 52].tolist()  # 存货增加FU202
Y = [GO[i] - ERR[i] for i in range(len(GO))]
C = df.iloc[7:-7, 50].tolist()  # 合计TC
K = df.iloc[7:-7, 53].tolist()  # 合计GCF
TI = df.iloc[-1, 3:45].tolist()
F = [C[i] + K[i] - S[i] for i in range(len(C))]
D = []
for i in range(42):
    D.append([])
    for j in range(42):
        D[i].append(0)
for i in range(len(d)):
    for j in range(len(d[0])):
        D[i][j] = (d[i][j] / TI[j]) * Y[i] / (Y[i] - X[i] + M[i] - S[i])
# print(D)
D = np.array(D)
D = np.matrix(D)
E = np.eye(42)
E = np.matrix(E)
F = np.matrix(F).T
fenzi = ((E - D) @ (E - D)).I @ F
result = [float(fenzi[i] / Y[i]) for i in range(42)]
df_result = pd.DataFrame()
df_result['产业编号'] = df.iloc[7:-7, 1]
df_result['产业名称'] = df.iloc[7:-7, 2]
df_result['产业上游度'] = result
df_result.to_excel('2015_result.xlsx', header=False, index=False)
