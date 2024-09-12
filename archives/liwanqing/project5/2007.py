import pandas as pd
import numpy as np

df = pd.read_excel('2007.xls')

GO = df['单位：万元'].tolist()[5:-7]
ERR = df.iloc[5:-7, 150].tolist()
d = df.iloc[5:-7, 3:138]
d = np.array(d).tolist()
X = df.iloc[5:-7, 147].tolist()  # 出口EX
M = df.iloc[5:-7, 149].tolist()  # 进口IM
S = df.iloc[5:-7, 145].tolist()  # 存货增加FU202
Y = [GO[i] - ERR[i] for i in range(len(GO))]
C = df.iloc[5:-7, 143].tolist()  # 合计TC
K = df.iloc[5:-7, 146].tolist()  # 合计GCF
TI = df.iloc[-1, 3:138].tolist()
F = [C[i] + K[i] - S[i] for i in range(len(C))]
D = []
for i in range(135):
    D.append([])
    for j in range(135):
        D[i].append(0)
for i in range(len(d)):
    for j in range(len(d[0])):
        D[i][j] = (d[i][j] / TI[j]) * Y[i] / (Y[i] - X[i] + M[i] - S[i])
# print(D)
D = np.array(D)
D = np.matrix(D)
E = np.eye(135)
E = np.matrix(E)
F = np.matrix(F).T
fenzi = ((E - D) @ (E - D)).I @ F
result = [float(fenzi[i] / Y[i]) for i in range(135)]
print(result)
