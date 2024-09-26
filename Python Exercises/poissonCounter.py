# Poisson counter is widely used in neuroscience when simulating 
# random distributions of brain cells firing

"""
Steps: 
1) Specify a target np.exp(-lambda) -> 10
2) Initialize a counter= 0, currval= 1
3) Multiply currval by a random number U[0, 1]
4) Repeat step 3 until currval < target
5) Return the number of times that you go through steps 4
"""

import numpy as np
import random

randomFloat = random.randint(0, 100) / 100 # Divided with a hundred to convert into floats
target = np.exp(-10)
print(f"Target is initialized as: {target}")
counter = 0
currval = 1

while currval >= target:
    currval *= random.randint(0, 100) / 100
    print(currval)
    counter += 1

print(f"Step 4 is repeated {counter} times")

# Yes I did it! Code is successfull.