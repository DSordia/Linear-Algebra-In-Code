# LECTURE 16 - Projection Matrices and Least Squares

import numpy as np

# Finding the error vector e from the solution found in the previous lecture and showing that b = p + e

# recall from the previous lecture, we have that x = [2/3, 1/2] for Ax = b, so the best line is y = 2/3 + 1/2t

tvalues = [1, 2, 3]
b = [1, 2, 2]
C = 2/3; D = 1/2

pvalues = []; errors = []

print('p + e = b?')
for i in range(0, len(tvalues)):
    pvalues.append(round(C + D * tvalues[i], 3))
    errors.append(round(b[i] - pvalues[i], 3))
    print(f'p = {pvalues[i]}, e = {errors[i]}, p + e = {round(pvalues[i] + errors[i], 3)}, b = {b[i]}')

#OUTPUT:
'''
p + e = b?
p = 1.167, e = -0.167, p + e = 1.0, b = 1
p = 1.667, e = 0.333, p + e = 2.0, b = 2
p = 2.167, e = -0.167, p + e = 2.0, b = 2
'''

# Show that p and e are orthogonal

p = np.array(pvalues)
e = np.array(errors)

print(f'p = \n{p}\ne = \n{e}\np dot e = \n{abs(round(np.dot(p, e), 2))} so p and e are orthogonal')

#OUTPUT:
'''
p =
[1.167 1.667 2.167]
e =
[-0.167  0.333 -0.167]
p dot e =
0.0 so p and e are orthogonal
'''