# This code computes factorial

import numpy as np

n = 4

# Because we need to start with 1 and end with n
# np.arange is an alternative for Python's 'range()'
factorial = np.prod(np.arange(1, n+1))
print(factorial)