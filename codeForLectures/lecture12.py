# LECTURE 12 - Graphs, Networks, Incidence Matrices

from sympy import *

# Four fundamental subspaces of an incidence matrix

A = Matrix([[-1, 1, 0, 0], [0, -1, 1, 0], [-1, 0, 1, 0], [-1, 0, 0, 1], [0, 0, -1, 1]])

print(f'A = \n{A}\nRank of A = {A.rank()}\nNull space of A = \n{A.nullspace()}\nNull space of null space = \n'
f'Left null space = \n{A.T.nullspace()}\nColumn space = \n{A.columnspace()}\nRow space = \n{A.T.columnspace()}')

#OUTPUT:
'''
A = 
Matrix([[-1, 1, 0, 0], [0, -1, 1, 0], [-1, 0, 1, 0], [-1, 0, 0, 1], [0, 0, -1, 1]])
Rank of A = 3
Null space of A =
[Matrix([
[1],
[1],
[1],
[1]])]
Null space of null space =
Left null space =
[Matrix([
[-1],
[-1],
[ 1],
[ 0],
[ 0]]), Matrix([
[ 1],
[ 1],
[ 0],
[-1],
[ 1]])]
Column space =
[Matrix([
[-1],
[ 0],
[-1],
[-1],
[ 0]]), Matrix([
[ 1],
[-1],
[ 0],
[ 0],
[ 0]]), Matrix([
[ 0],
[ 1],
[ 1],
[ 0],
[-1]])]
Row space =
[Matrix([
[-1],
[ 1],
[ 0],
[ 0]]), Matrix([
[ 0],
[-1],
[ 1],
[ 0]]), Matrix([
[-1],
[ 0],
[ 0],
[ 1]])]
'''