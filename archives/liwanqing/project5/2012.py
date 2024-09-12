import pandas as pd
import numpy as np

df = pd.read_excel('2012.xlsx')

GO = df.iloc[3:-7, 153].tolist()
ERR = df.iloc[3:-7, 154].tolist()
d = df.iloc[3:-7, 3:142]
d = np.array(d).tolist()
X = df.iloc[3:-7, 150].tolist()
M = df.iloc[3:-7, 152].tolist()
S = df.iloc[3:-7, 148].tolist()
Y = [GO[i] - ERR[i] for i in range(len(GO))]
C = df.iloc[3:-7, 146].tolist()
K = df.iloc[3:-7, 149].tolist()
TI = df.iloc[-1, 3:142].tolist()
F = [C[i] + K[i] - S[i] for i in range(len(C))]
D = []
for i in range(139):
    D.append([])
    for j in range(139):
        D[i].append(0)
for i in range(len(d)):
    for j in range(len(d[0])):
        D[i][j] = (d[i][j] / TI[j]) * Y[i] / (Y[i] - X[i] + M[i] - S[i])
print(D)
D = np.array(D)
D = np.matrix(D)
E = np.eye(139)
E = np.matrix(E)
F = np.matrix(F).T
fenzi = ((E-D)@(E-D)).I @ F
result = [float(fenzi[i]/Y[i]) for i in range(139)]
df_result = pd.DataFrame()
df_result['产业编号'] = df.iloc[3:-7, 1]
df_result['产业名称'] = df.iloc[3:-7, 2]
df_result['产业上游度'] = result
df_result.to_excel('2012_result.xlsx', header=False, index=False)
