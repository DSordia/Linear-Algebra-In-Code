# LECTURE 15 - Projections onto Subspaces

import numpy as np

# Trying to solve Ax = b for 3 equations with 2 unknowns

A = np.array([[1, 1], [1, 2], [1, 3]])
b = np.array([[1], [2], [2]])

#print(f'A = \n{A}\nb = \n{b}\nSolving for x in Ax = b gives \n{np.linalg.solve(A, b)}')

#OUTPUT:
'''
numpy.linalg.LinAlgError: Last 2 dimensions of the array must be square
'''

print('Now applying the ideas from the lecture:')

newA = np.dot(A.transpose(), A)
newB = np.dot(A.transpose(), b)

print(f'Multiplying both sides of Ax = b by A transpose gives: \n{np.linalg.solve(newA, newB)}')
#OUTPUT:
'''
Now applying the ideas from the lecture:
Multiplying both sides of Ax = b by A transpose gives:
[[0.66666667]
 [0.5       ]]
'''