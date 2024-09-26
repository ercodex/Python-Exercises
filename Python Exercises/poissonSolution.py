# This is the instructors solution 
import numpy as np

def poissonCounter(lam):
    counter, currval = 0, 1
    target = np.exp(-lam)

    while currval > target:
        counter += 1
        currval *= np.random.rand()

    return counter

print(poissonCounter(10))

# I want to see how many steps it takes on average.
a = 0

for i in range(1000):
    a += poissonCounter(10)

print(a / 1000) # Roughly 11.