# LECTURE 31 - Change of Basis; Image Compression

import numpy as np

# Showing that the vectors of the wavelets basis are orthogonal

W = np.array([[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, -1, -1, -1, -1], [1, 1, -1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, -1, -1],
[1, -1, 0, 0, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 0, 0, 1, -1]])

for i in range (0, len(W)):
    for j in range (0, len(W)):
        if i != j:
            print(f'Dot product of column {i+1} and column {j+1}: {np.dot(W[i], W[j])}')

#OUTPUT:
'''
Dot product of column 1 and column 2: 0
Dot product of column 1 and column 3: 0
Dot product of column 1 and column 4: 0
Dot product of column 1 and column 5: 0
Dot product of column 1 and column 6: 0
Dot product of column 1 and column 7: 0
Dot product of column 1 and column 8: 0
Dot product of column 2 and column 1: 0
Dot product of column 2 and column 3: 0
Dot product of column 2 and column 4: 0
Dot product of column 2 and column 5: 0
Dot product of column 2 and column 6: 0
Dot product of column 2 and column 7: 0
Dot product of column 2 and column 8: 0
Dot product of column 3 and column 1: 0
Dot product of column 3 and column 2: 0
Dot product of column 3 and column 4: 0
Dot product of column 3 and column 5: 0
Dot product of column 3 and column 6: 0
Dot product of column 3 and column 7: 0
Dot product of column 3 and column 8: 0
... and so on
'''

# Changing basis using the wavelets basis (C = W^-1p)

p = np.random.randint(256, size=(8, 1))

print(f'Original basis p = \n{p}\nNew basis C using wavelets basis = \n{np.dot(np.linalg.inv(W), p)}')

#OUTPUT:
'''
Original basis p =
[[208]
 [ 19]
 [135]
 [116]
 [119]
 [105]
 [225]
 [ 59]]
New basis C using wavelets basis =
[[121.625]
 [  2.625]
 [ 47.125]
 [-57.875]
 [165.125]
 [-59.875]
 [ 24.125]
 [-34.875]]
'''