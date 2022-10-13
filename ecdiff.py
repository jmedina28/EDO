

import matplotlib.pyplot as plt
import sympy
import numpy as np
from scipy import integrate

sympy.init_printing(use_latex='mathjax')

x = sympy.Symbol('x')
y = sympy.Function('y')

f = (x**2 + 1)*(y(x)**-1 + 1)


sol = sympy.dsolve(y(x).diff(x) - f, y(x))

print(sol)
sympy.pprint(sol)