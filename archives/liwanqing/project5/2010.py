import pandas as pd
import numpy as np

df = pd.read_excel('2010.xls')

GO = df.iloc[5:-7, 57].tolist()
ERR = df.iloc[5:-7, 56].tolist()
d = df.iloc[5:-7, 3:44]
d = np.array(d)
X = df.iloc[5:-7, 53].tolist()
M = df.iloc[5:-7, 55].tolist()
S = df.iloc[5:-7, 51].tolist()
Y = [GO[i] - ERR[i] for i in range(len(GO))]
C = df.iloc[5:-7, 49].tolist()
K = df.iloc[5:-7, 52].tolist()
TI = df.iloc[-1, 3:44].tolist()
F = [C[i] + K[i] - S[i] for i in range(len(C))]
D = []
for i in range(41):
    D.append([])
    for j in range(41):
        D[i].append(0)
for i in range(len(d)):
    for j in range(len(d[0])):
        D[i][j] = (d[i][j] / TI[j]) * Y[i] / (Y[i] - X[i] + M[i] - S[i])
# print(D)
D = np.array(D)
D = np.matrix(D)
E = np.eye(41)
E = np.matrix(E)
F = np.matrix(F).T
fenzi = ((E-D)@(E-D)).I @ F
result = [float(fenzi[i]/Y[i]) for i in range(41)]
df_result = pd.DataFrame()
df_result['产业编号'] = df.iloc[5:-7, 1]
df_result['产业名称'] = df.iloc[5:-7, 2]
df_result['产业上游度'] = result
# df_result.to_excel('2010_result.xlsx', header=False, index=False)

