# Exercise: 
"""
Create a new class
1) Weights should be a random numbers matrix of size 'Layers x Units'
2) Change training method to multiply by input A and add with input B
3) You can cheat from file 'oop.py'
"""

import numpy as np

layers = int(input("Enter the number of layers: "))
units  = int(input("Enter the number of units: "))


class exercise_model(object):
    def __init__(self, units, layers):
        self.layers  = layers
        self.units   = units
        self.weights = np.random.randn(units, layers)

    def trainModel(self, A, B):
        self.weights = (self.weights * A) + B
        return self.weights
    
model = exercise_model(units, layers)
print(model.trainModel(2, 3))
print()
print(model.trainModel(3, 7))
print()
print(model.trainModel(2, 4))