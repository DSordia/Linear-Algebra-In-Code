# LECTURE 6 - Column Space and Nullspace

import numpy as np
from sympy import linear_eq_to_matrix, symbols
import ast

# Solving Ax = b with 4 equations and 3 unknowns

x, y, z = symbols('x y z')
eqns = [x + y + 2*z - 1,
        2*x + y + 3*z - 2,
        3*x + y + 4*z - 3,
        4*x + y + 5*z - 4] # = 0 is implied for these equations

tempA, tempb = linear_eq_to_matrix(eqns, [x, y, z])

tempA = str(tempA); tempb = str(tempb)
tempA = tempA[7:len(tempA)-1]; tempb = tempb[7:len(tempb)-1]
tempA = ast.literal_eval(tempA); tempb = ast.literal_eval(tempb)

A = np.array(tempA)
b = np.array(tempb)
x = np.linalg.lstsq(A, b)

print(f'\nA solution to the system of 4 equations {eqns} with 3 unknowns is: \n{x} \n')

#OUTPUT:
'''
A solution to the system of 4 equations [x + y + 2*z - 1, 2*x + y + 3*z - 2, 3*x + y + 4*z - 3, 4*x + y + 5*z - 4] with 3 unknowns is:
(array([[ 0.66666667],
       [-0.33333333],
       [ 0.33333333]]), array([], dtype=float64), 2, array([9.34413269e+00, 8.28965828e-01, 1.60246891e-16]))
'''

# Solving Ax = 0 with 4 equations and 3 unknowns

x, y, z = symbols('x y z')
eqns = [x + y + 2*z,
        2*x + y + 3*z,
        3*x + y + 4*z,
        4*x + y + 5*z] # = 0 is implied for these equations

tempA, tempb = linear_eq_to_matrix(eqns, [x, y, z])

tempA = str(tempA); tempb = str(tempb)
tempA = tempA[7:len(tempA)-1]; tempb = tempb[7:len(tempb)-1]
tempA = ast.literal_eval(tempA); tempb = ast.literal_eval(tempb)

A = np.array(tempA)
b = np.array(tempb)
x = np.linalg.lstsq(A, b)

print(f'\nA solution to the system of 4 equations {eqns} with 3 unknowns is: \n{x} \n')

#OUTPUT:
'''
x, y, z = symbols('x y z')
eqns = [x + y + 2*z - 1,
        2*x + y + 3*z - 2,
        3*x + y + 4*z - 3,
        4*x + y + 5*z - 4] # = 0 is implied for these equations

tempA, tempb = linear_eq_to_matrix(eqns, [x, y, z])

tempA = str(tempA); tempb = str(tempb)
tempA = tempA[7:len(tempA)-1]; tempb = tempb[7:len(tempb)-1]
tempA = ast.literal_eval(tempA); tempb = ast.literal_eval(tempb)

A = np.array(tempA)
b = np.array(tempb)
x = np.linalg.lstsq(A, b)

print(f'\nA solution to the system of 4 equations {eqns} with 3 unknowns is: \n{x} \n')

#OUTPUT:
'''

# Showing that if Av = 0 and Aw = 0 then Av + Aw = 0 where v and w are vectors

A = np.array([[1, 1, 2], [2, 1, 3], [3, 1, 4], [4, 1, 5]])
v = np.array([[1], [1], [-1]])
w = np.array([[2], [2], [-2]])

print(f'A = \n{A}\nv = \n{v}\nw = \n{w}\n Av = \n{np.dot(A, v)}\nAw = \n{np.dot(A, w)}\n')
print(f'Av + Aw = \n{np.dot(A, v) + np.dot(A, w)}\n')

#OUTPUT
'''
A = 
[[1 1 2]
 [2 1 3]
 [3 1 4]
 [4 1 5]]
v =
[[ 1]
 [ 1]
 [-1]]
w =
[[ 2]
 [ 2]
 [-2]]
 Av =
[[0]
 [0]
 [0]
 [0]]
Aw =
[[0]
 [0]
 [0]
 [0]]

Av + Aw =
[[0]
 [0]
 [0]
 [0]]
 '''

# Showing that if Ax = 0 then A(cx) = 0 where c is a scalar

A = np.array([[1, 1, 2], [2, 1, 3], [3, 1, 4], [4, 1, 5]])
x = np.array([[1], [1], [-1]])
print(f'A = \n{A}\nx = \n{x}\nAx = \n{np.dot(A, x)}\nA(2x) = \n{np.dot(A, np.dot(2, x))}\nA(-7x) = \n{np.dot(A, np.dot(-7, x))}')

#OUTPUT
'''
A =
[[1 1 2]
 [2 1 3]
 [3 1 4]
 [4 1 5]]
x =
[[ 1]
 [ 1]
 [-1]]
Ax =
[[0]
 [0]
 [0]
 [0]]
A(2x) =
[[0]
 [0]
 [0]
 [0]]
A(-7x) =
[[0]
 [0]
 [0]
 [0]]
'''