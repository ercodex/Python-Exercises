# This code flips a coin N times and returns the average

import numpy as np

N = int(input("Enter n: "))

coins = (np.random.randn(N)) > 0
rate = np.mean(coins)
print(f"Chance of getting heads with {N} flips is: {rate}")