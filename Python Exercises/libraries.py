# This code explains some properties of libraries

import numpy as np
import pandas as pd

# Taking the average
numbers = [1, 2, 3, 4, 5]
print(f"Mean of 'numbers' is: {np.mean(numbers)}")

# Creating linearly spaced numbers from 0 to 6, and there will be 4 of them
numbers1 = np.linspace(0, 6, 4) # This returns a numpy array
print(f"Linearly spaced numbers: {numbers1}, and this is a {type(numbers1)}")

print("\n", np.random.randn(3))
print("\n", np.random.randn(2, 4))