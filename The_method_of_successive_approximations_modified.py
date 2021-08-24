import numpy as np
from prettytable import PrettyTable

# The method of successive approximations (modified)
def method(x, t, lambd, a, b, K, f, eps, n):
    h = (b - a) / (n - 1)
    X = np.zeros(n)
    A = np.zeros(n)
    K_ij = np.zeros((n, n))
    NM = np.zeros((n, n))
    phi = np.zeros(n)
    phi_streak = np.zeros(n)
    Y = np.zeros((2, n))
    for i in range (0, n):
        X[i] = a + h * i
        if (i == 0 or i == n - 1):
            A[i] = h / 3
        elif ((i + 1) % 2 == 0):
            A[i] = 4 * h / 3
        else:
            A[i] = 2 * h / 3
    for i in range(n):
        for j in range(n):
            K_ij[i][j] = K.subs([(x, X[i]), (t, X[j])])
    for i in range(n):
        for j in range(n):
            NM[i][j] = lambd * A[i] * K_ij[j][i]
        phi[i] = f.subs(x, X[i])
        Y[1][i] = phi[i]
    while (max(abs(Y[0]-Y[1])) > eps):
        for i in range(n):
            for j in range(n):
                phi_streak[i] += NM[j][i] * phi[j]
        Y[0] += phi
        Y[1] += phi_streak
        for i in range(n):
            phi[i] = phi_streak[i]
            phi_streak[i] = 0
    print("Метод последовательных приближений (модифицированный):")
    printRes(h, X, Y, n)

def printRes(h, X, Y, n):
    size = 4
    print("Шаг h =", h)
    table = PrettyTable()
    table.field_names = ["x", "y"]
    for i in range(n):
        table.add_row([f"{X[i]:.{size}f}", f"{Y[1][i]:.{size}f}"])
    print(table)