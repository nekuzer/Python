import numpy as np
from prettytable import PrettyTable

# Method of replacing the integral with a finite sum
def method(x, t, lambd, a, b, K, f, eps, n):
    h = (b - a) / (n - 1)
    X = np.zeros(n)
    K_ij = np.zeros((n, n))
    f_i = np.zeros(n)
    A = np.zeros(n)
    for i in range (0, n):
        X[i] = a + h * i
        f_i[i] = f.subs(x, X[i])
        if (i == 0 or i == n - 1):
            A[i] = h / 3
        elif ((i + 1) % 2 == 0):
            A[i] = 4 * h / 3
        else:
            A[i] = 2 * h / 3
    for i in range(n):
        for j in range(n):
            if (i == j):
                K_ij[i][j] = 1 - lambd * K.subs([(x, X[j]), (t, X[i])]) * A[i]
            else:
                K_ij[i][j] = 0 - lambd * K.subs([(x, X[j]), (t, X[i])]) * A[i]
    # for i in range(n):
    #     f += lambd * A[i] * Yn[i] * K.subs(t, X[i])
    Y = np.linalg.solve(K_ij.transpose(), f_i)
    print("Метод замены интеграла конечной суммой:")
    printRes(h, X, Y, n)

def printRes(h, X, Y, n):
    size = 4
    print("Шаг h =", h)
    table = PrettyTable()
    table.field_names = ["x", "y"]
    for i in range(n):
        table.add_row([f"{X[i]:.{size}f}", f"{Y[i]:.{size}f}"])
    print(table)