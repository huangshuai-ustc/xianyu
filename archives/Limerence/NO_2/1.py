import numpy as np

# 创建一个矩阵
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# 计算特征值
eigenvalues = np.linalg.eigvals(matrix)

# 打印特征值
print("特征值:", eigenvalues)
