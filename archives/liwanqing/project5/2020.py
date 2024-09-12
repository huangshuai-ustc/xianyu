import pandas as pd
import numpy as np

df = pd.read_excel('2020.xlsx')

GO = df.iloc[5:-7, 168].tolist()
# ERR = df.iloc[7:-7, 57].tolist()
d = df.iloc[5:-7, 3:156]
d = np.array(d).tolist()
X = df.iloc[5:-7, 165].tolist()  # 出口EX
M = df.iloc[5:-7, 167].tolist()  # 进口IM
S = df.iloc[5:-7, 163].tolist()  # 存货增加FU202
# Y = [GO[i] - ERR[i] for i in range(len(GO))]
C = df.iloc[5:-7, 161].tolist()  # 合计TC
K = df.iloc[5:-7, 164].tolist()  # 合计GCF
TI = df.iloc[-1, 3:156].tolist()
F = [C[i] + K[i] - S[i] for i in range(len(C))]
D = []
for i in range(153):
    D.append([])
    for j in range(153):
        D[i].append(0)
for i in range(len(d)):
    for j in range(len(d[0])):
        D[i][j] = (d[i][j] / TI[j]) * GO[i] / (GO[i] - X[i] + M[i] - S[i])
# print(D)
D = np.array(D)
D = np.matrix(D)
E = np.eye(153)
E = np.matrix(E)
F = np.matrix(F).T
fenzi = ((E - D) @ (E - D)).I @ F
result = [float(fenzi[i] / GO[i]) for i in range(153)]
df_result = pd.DataFrame()
df_result['产业编号'] = df.iloc[5:-7, 1]
df_result['产业名称'] = df.iloc[5:-7, 2]
df_result['产业上游度'] = result
df_result.to_excel('2020_result.xlsx', header=False, index=False)
