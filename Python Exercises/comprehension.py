# List comprehension offers a shorter syntax.

import random

# Normally, Python is upper-bound exclusive, but
# in this 'random' module, they made it inclusive.
a = random.randint(1, 10)

# Single line condition
print("a is large") if a > 5 else print("a is small")

# This prints numbers in a list. 
erdem = [ j**2 for j in range(10) if j < 6] 
print(erdem)