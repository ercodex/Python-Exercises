"""
Exercise:
1) Create a vector of integers from 0 to 8 (v)
2) Reshape v into a 3x3 matrix (M) (np.reshape)
3) Repeat M into a 9x3 (C) (np.tile)
4) Broadcast-multiple C with v (B)
"""

import numpy as np

v = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8], ndmin=2)
print(v)
M = v.reshape(3, 3)
print("\n ", M) 

C = np.tile(M, (3, 1))
print("\n", C)

# Now we need to convert first vector it into a column.
v = v.T

B = C*v
print(f"\n-----Final Matrix-----\n{B}")