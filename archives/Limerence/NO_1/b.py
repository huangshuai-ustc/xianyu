## module LUdecomp
''' a = LUdecomp(a)
    LUdecomposition: [L][U] = [a]

    x = LUsolve(a,b)
    Solution phase: solves [L][U]{x} = {b}
'''
import numpy as np
from scipy import linalg as la
import copy


def LUdecomp(a):
    n = len(a)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k + 1:n] = a[i, k + 1:n] - lam * a[k, k + 1:n]
                a[i, k] = lam
    return a


def LUsolve(a, b):
    n = len(a)
    for k in range(1, n):
        b[k] = b[k] - np.dot(a[k, 0:k], b[0:k])
    # b[n-1] = b[n-1]/a[n-1,n-1]
    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1:n], b[k + 1:n])) / a[k, k]
    return b


# A = np.array([[1, -1, 1, 0],
#               [0, 2, 1, 0],
#               [1, 3, 4, 4],
#               [0, 2, 1, -1]])
#
# b = np.array([1, 3, 12, 2])
input_str = input("请输入一组数字，以空格分隔：")
input_strs = input("请输入另一组数字，以空格分隔：")
input_arr = [int(x) for x in input_str.split()]
input_arrs = [int(x) for x in input_strs.split()]
print(np.array(input_arr).reshape(4,4))
print(np.array(input_arrs).reshape(4,1))
LU = LUdecomp(np.array(input_arr).reshape(4,4))
print(LU)
result = LUsolve(LU, np.array(input_arrs).reshape(4,1))
print(result)

