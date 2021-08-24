from sympy import *
import sympy as sym

import The_method_of_successive_approximations
import The_method_of_successive_approximations_modified
import Method_of_replacing_the_integral_with_a_finite_sum

x, t = symbols("x t")

lambd = 1
a = 0
b = 1
K = (sym.exp(-x * t))
f = (sym.sin(2 * sym.pi * x))

eps = 0.0001
n = 9

The_method_of_successive_approximations.method(x, t, lambd, a, b, K, f, eps, n)
The_method_of_successive_approximations_modified.method(x, t, lambd, a, b, K, f, eps, n)
Method_of_replacing_the_integral_with_a_finite_sum.method(x, t, lambd, a, b, K, f, eps, n)