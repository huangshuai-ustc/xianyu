import numpy as np
import time

def gauss(a, b):
    n, m = a.shape
    x = np.empty(m)  # 解
    # x = [1,2,3]
    # 一共要有（行-1）次消元
    for k in range(n - 1):
        # 每一次消元都需要l，第k行消元，就从k+l处开始计算l，通过k+1列的k+1行后所有行进行计算
        for i in range(k + 1, n):
            l = a[i][k] / a[k][k]
            # 第三层循环计算每行的所有列，目前是第i行第k列
            for j in range(n):
                # 注意这里是 range(n)，而不是 range(k+1,n)，观察表达式
                a[i][j] = a[i][j] - l * a[k][j]
            b[i] = b[i] - l * b[k]
    x[m - 1] = b[m - 1] / a[m - 1][m - 1]
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += a[i][j] * x[j]
        x[i] = (b[i] - sum) / a[i][i]
    print(x)



if __name__ == '__main__':
    """
    a = np.array([[0.2641, 0.1735, 0.8642],
                  [0.9411, -0.0175, 0.1463],
                  [-0.8641, -0.4243, 0.071]])
    b = np.array([-0.7521, 0.6310, 0.2501])
    gauss(a, b)
    """
    a = np.array([[2, -2, -1],
                  [4, 1, -2],
                  [-2, 1, -1]], dtype=float)
    b = np.array([2, 1, -3], dtype=float)
    time1 = time.time_ns()
    gauss(a, b)
    time2 = time.time_ns()
    print(time2-time1)
