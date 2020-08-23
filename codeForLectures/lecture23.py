# LECTURE 23 - Differential Equations and exp(At)

import numpy as np
from sympy import *

# Solving a 2-equation differential equation

#du/dt = -u1 + 2u2
#du/dt = u1 - 2u2
#u(0) = [1, 0]

A = Matrix([[-1, 2], [1, -2]])
evalues = A.eigenvals(); evectors = A.eigenvects()
x1 = evectors[1]
x2 = evectors[0]

#solution: u(t) = c1e^lamda1t * x1 + cse^lamda2t * x2
# lamda1 is 0, so u(t) = c1 * x1 + c2 * e^-3t * x2
# initial condition: u(0) = [1, 0]

# c1[2, 1] + c2[1, -1] = [1, 0]: construct a matrix

A = np.array([[2, 1], [1, -1]])
b = np.array([[1], [0]])
solution = np.linalg.solve(A, b)

print(f'c1 and c2 are \n{solution}')

#OUTPUT:
'''
c1 and c2 are
[[0.33333333]
 [0.33333333]]
'''# so solution is u(t) = 1/3[2, 1] + 1/3e^-3t[1, -1] 