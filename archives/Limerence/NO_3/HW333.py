import numpy as np


def catenary_jacobian(T, angles, length):
    n = len(angles)

    Jcob = np.zeros((n + 1, n + 1))

    for i in range(n - 1):
        for j in range(n + 1):
            if j == 0:
                Jcob[i, j] = np.tan(angles[i]) - np.tan(angles[i + 1])
            elif j == i + 1:
                Jcob[i, j] = T / (np.cos(angles[i]) ** 2)
            elif j == i + 2:
                Jcob[i, j] = T / (np.cos(angles[i + 1]) ** 2)
    for z in range(1, n + 1):
        Jcob[-2, z] = length[z - 1] * np.cos(angles[z - 1])
        Jcob[-1, z] = length[z - 1] * np.sin(angles[z - 1])
    return Jcob


theta = 45
theta_rad = theta * 3.1415 / 180.0

T = 15
length = [1, 2, 3, 4,5]
error = 1
tol = 1.0e-12

iter = 0

T = 15.0
t1 = 45 * 3.1415 / 180.0
t2 = t1 / 2.0
t3 = 45 * 3.1415 / 180
angles = [t1, t2, t3]
print(angles)
length = [-4.0,-6.0,5]
Jcob = catenary_jacobian(T, angles, length)
print(Jcob)
