from sympy import *
import numpy as np
from prettytable import PrettyTable

# The method of successive approximations
def method(x, t, lambd, a, b, K, f, eps,  n):
    eps = 0.04
    h = (b - a) / (n - 1)
    X = np.zeros(n)
    for i in range (0, n):
        X[i] = a + h * i
    Y = np.zeros((2, n))
    f_streak = [0] * 2
    f_streak[0] = f
    for i in range(n):
        Y[1][i] = float(f.subs(x, X[i]))
    i = 0
    while (max(abs(Y[0]-Y[1])) > eps):
    # for z in range(3):
        i += 1
        f_streak[1] = integrate(K * f_streak[0].subs(x, t), (t, a, b))
        f += lambd**(i) * f_streak[1]
        f_streak[0] = f_streak[1]
        Y[0] = Y[1]
        for j in range(n):
            Y[1][j] = f.subs(x, X[j])
    print("Метод последовательных приближений:")
    printRes(h, X, Y, n)

def printRes(h, X, Y, n):
    size = 4
    print("Шаг h =", h)
    table = PrettyTable()
    table.field_names = ["x", "y"]
    for i in range(n):
        table.add_row([f"{X[i]:.{size}f}", f"{Y[1][i]:.{size}f}"])
    print(table)