# Repeat without using NumPy and in a single line.

import numpy as np

x1 = np.linspace(-3, 3, 11)
y1 = x1**2

print(x1)
print(y1)
print("\n-----Solution-----")

lst = [i*(3/5) for i in range (-5, 6)]
print(lst)
print([j**2 for j in lst])