# This code focuses on Classes and OOP in Python
# Let's explain some things:

"""
Classes are like blueprints for creating a set of attributes (aka variables) and methods (aka functions).

Basically, classes are for creating an object and that object has a set of variables (parameters) and
a set of associated functions (methods).

What we create from a class is an 'instance'. So every class is going to produce multiple instances.
"""

"""
To create a class, we need to use reserved keyword 'class', then the name of the class, and
for the inside of the paranthesis, we need to write the 'type' of the class. In this case, it 
is 'object'.
"""

class model(object):

    # Constructor Method: This method has a weird looking function name '__init__'
    # Methods of objects are nothing more than functions that are created within the 
    # definition of the class
    def __init__(self, numlayers, numunits, name): # __init__ comes from 'initialization'. And almost every
                                                   # method in a class is going to take 'self' as the first
                                                   # and sometimes only input. In this case, we have additional
                                                   # inputs that are commonly used in Deep Learning.
        
        self.layers  = numlayers # These are referring to the specific instance of this object that we are going
        self.units   = numunits  # to create in this class. These are called attributes (of the object).
        self.name    = name
        self.weights = 1

    # Let's create another method in this class
    def howManyUnits(self): #This method is going to compute that how many units is present in the model
        totalUnits = self.layers * self.units
        print(f"There are {totalUnits} units in the model.")

    # Another method
    def trainTheModel(self, x):
        self.weights += x
        return self.weights
    
    # Another method
    def __str__(self):
        return f'This is a {self.name} architecture.'

# Let's create an instance of this model. Select your variable name, assign it to the:
#   name of the class, and all the inputs that are specified above except 'self'
m1 = model(2, 5, 'Neural Network')
print(m1) # We can see that the variable type is 'model' and the there is the address of it.

m1.howManyUnits()
print(m1.trainTheModel(3)) # We are fundamentally changing the attributes of this object (m1 instance of class 'model')
print(m1.trainTheModel(3))
print(m1.trainTheModel(3))

"""
Actually, I've got a nice opportunity to learn from a mistake: 
    print(m1.howManyUnits()) # line 48

This was the first version. And it prints:
    There are 10 units in the model.
    None

However, this 'howManyUnits' method does not return anything. In Python, if a function or
method does not explicitly return a value using the return statement, it implicitly returns None.
When we call print(m1.howManyUnits()), the howManyUnits method runs, prints the total number of 
units (i.e., "There are 10 units in the model."), and then the print function attempts to print 
the return value of howManyUnits. Since it returns None, None is printed.

"""