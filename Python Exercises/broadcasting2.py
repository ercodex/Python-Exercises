import numpy as np

# We can also make column-wise operations. But first, we need to convert vectors

v = np.array([-1, 0, 1, 0])
print(v)

n = np.array([-1, 0, 1, 0], ndmin= 2) # Minimum dimensions = 2
print(n) # Innermost square brackets specify that this is all one row

m = np.array([-1, 0, 1, 0], ndmin=2).T
print(m) # And lastly, with T, we transpose.

# Let's get X
X = np.array([ [1, 2, 3],
               [2, 3, 4],
               [3, 4, 5],
               [4, 5, 6] ])
Z = X * m
print(f"\n----Final Matrix----\n{Z}")

# And this was the column-wise broadcasting.
# Important part is specifying the vector as a row or column vector.

