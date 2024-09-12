import numpy as np
a = np.array([[1, -1, 1, 0], [0, 2, 1, 0], [1, 3, 4, 4], [0, 2, 1, -1]])
print(a)
n = len(a)
for k in range(0, n - 1):
    for i in range(k + 1, n):
        if a[i, k] != 0.0:
            lam = a[i, k] / a[k, k]
            a[i, k + 1:n] = a[i, k + 1:n] - lam * a[k, k + 1:n]
            a[i, k] = lam

print(a)
