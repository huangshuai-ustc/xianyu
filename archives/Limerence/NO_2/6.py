import numpy as np
import math


def iterEqs(x, omega, A, b):
    n = len(x)
    for i in range(n):
        sigma = 0
        x[i] = (1.0 - omega) * x[i]
        for j in range(n):
            if i == j:
                sigma += b[i][0]
            if j != i:
                sigma -= x[j] * A[i][j]
        x[i] = x[i] + omega * sigma / A[i][i]
    return x


A = np.array([[3, 1, -1], [2, 4, 1], [-1, 2, 5]])
b = np.array([[4], [1], [1]])
# x = np.array([0.0, 0.0, 0.0])
x = np.array([1.0, 1.0, 1.0])

# Relaxation factor (omega)
omega = 1
maxiter = 200
tol = 1e-6
p = 1

for iteration in range(maxiter):
    Xold = np.copy(x)
    x = iterEqs(x, omega, A, b)
    diff = np.max(np.abs(x - Xold))
    dx = math.sqrt(np.dot(x - Xold, x - Xold))
    dx1 = 0
    if iteration == 10:
        dx1 = dx
    if iteration == 11:
        dx2 = dx
        omega = 2.0 / (1.0 + math.sqrt(1.0 - (dx2/dx1)**(1.0/p)))
    if diff < tol:
        break

    print("Solution after", iteration, "iteration:", x)
    print("relaxation factor now is", omega)
