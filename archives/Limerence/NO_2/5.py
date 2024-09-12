import numpy as np


def iterEqs(x, omega, A, b):
    n = len(x)
    for i in range(n):
        x[i] = (1.0 - omega) * x[i]
        for j in range(n):
            # if j != i:
            x[i] += (omega / A[i, i]) * (b[i] - A[i, j] * x[j])
    return x


# Define the coefficient matrix A and the right-hand side vector b


A = np.array([[3, 1, -1], [2, 4, 1], [-1, 2, 5]])
b = np.array([[4], [1], [1]])

# Initial guess for the solution x
x = np.array([0.0, 0.0, 0.0])

# Relaxation factor (omega)
omega = 1.1430956678289939

# Perform a single iteration
x = iterEqs(x, omega, A, b)

print("Solution after one iteration:", x)
