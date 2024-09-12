
import pandas as pd
import numpy as np

# 读取Excel文件
df = pd.read_excel(r'2010.xlsx')

# 提取需要的数据列并转换为数值类型，处理可能的数据缺失
GO = pd.to_numeric(df.iloc[7:-7, 34], errors='coerce').fillna(0).tolist()
ERR = pd.to_numeric(df.iloc[7:-7, 33], errors='coerce').fillna(0).tolist()
X = pd.to_numeric(df.iloc[7:-7, 30], errors='coerce').fillna(0).tolist()  # 出口EX
M = pd.to_numeric(df.iloc[7:-7, 32], errors='coerce').fillna(0).tolist()  # 进口IM
S = pd.to_numeric(df.iloc[7:-7, 28], errors='coerce').fillna(0).tolist()  # 存货增加FU202
C = pd.to_numeric(df.iloc[7:-7, 26], errors='coerce').fillna(0).tolist()  # 合计TC
K = pd.to_numeric(df.iloc[7:-7, 29], errors='coerce').fillna(0).tolist()  # 合计GCF
TI = pd.to_numeric(df.iloc[-1, 3:20], errors='coerce').fillna(0).tolist()
# 提取中间品矩阵数据并转换为数值类型
d = df.iloc[7:-7, 3:20].apply(pd.to_numeric, errors='coerce').fillna(0).to_numpy().tolist()

# 计算F，考虑可能的数据缺失
F = [C[i] + K[i] - S[i] for i in range(len(C))]


# 初始化D矩阵
D = np.zeros((18, 18))
print(len(M))
# 填充D矩阵
for i in range(len(d)):
    for j in range(len(d[i])):
        if TI[j] != 0 and (GO[i] - X[i] + M[i] - S[i]) != 0:
            D[i][j] = (d[i][j] / TI[j]) * GO[i] / (GO[i] - X[i] + M[i] - S[i])

# 将D转换为NumPy矩阵
D = np.matrix(D)

# 创建单位矩阵E
E = np.eye(18)
E = np.matrix(E)

# 将F转换为列矩阵
F = np.matrix(F).T

# 计算分子
fenzi = ((E - D) @ (E - D)).I @ F

# 计算产业上游度
result = [float(fenzi[i] / GO[i]) for i in range(18)]

# 创建结果DataFrame
df_result = pd.DataFrame({
    '产业编号': df.iloc[7:-7, 2].tolist(),
    '产业名称': df.iloc[7:-7, 1].tolist(),
    '产业上游度': result
})

# 保存结果到Excel
df_result.to_excel('2010_result.xlsx', header=False, index=False)

