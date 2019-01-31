#!/usr/bin/env python3

import numpy as np

np_height = np.array([1.73, 1.68,  1.84, 1.89, 1.79])

np_weight = np.array([65.9, 70.3, 80.4, 56.6, 70.2])
#

# ndarray => N-dimensional array
# print(type(np_height)) # <class 'numpy.ndarray'>
# print(type(np_weight))

# 2D Numpy array
np_2D = np.array(
    [[1.73, 1.68,  1.84, 1.89, 1.79],
    [65.9, 70.3, 80.4, 56.6, 70.2]
])

print(np_2D.shape)
# (2, 5) duas linhas e 5 colunas

# Subsetting
# print(np_2D[0][2])
# print(np_2D[0,2])
# print(np_2D[:, 1:3])  # : as duas linhas , 1:3 do segundo ao 4 elemento
# print()
# print(np_2D[1, :]) # segunda linhas, todos os elementos