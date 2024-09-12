import numpy as np
def catenary_jacobian(T, angles):
    n = len(angles)
    Jcob = np.zeros((n+1, n+1))

    for i in range(n-1):
        for j in range(n+1):
            if j == 0:
                Jcob[i, j] = np.tan(angles[i])-np.tan(angles[i+1])
            elif j == i + 1:
                Jcob[i, j] = T / (np.cos(angles[i]) ** 2)
                print(Jcob[i, j])
            elif j == i+2:
                Jcob[i, j] = T / (np.cos(angles[i+1]) ** 2)
    return Jcob

T = 15
t1 = 45 * 3.1415 / 180.0
t2 = t1 / 2.0
t3 = 45 * 3.1415 / 180
angle = [t1, t2, t3]
j = catenary_jacobian(T,angle)
print(j)
