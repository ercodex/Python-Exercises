# This code explains tuples.

# They are very much like lists
tupleA = (5, 'eren', 3.14)
listA = [5, 'eren', 3.14]
print(type(tupleA))
print(tupleA) # But we see paranthesis when printing.

"""
We may not use paranthesis, it is not necessary. But makes it more readable and it is recommended.
It can be confused with multiple assignment.
"""

tupleB = 3, 'asdf'
tupleC, tupleD = 3, 'asdf'

print(f"\ntupleB: {type(tupleB)}\ntupleC: {type(tupleC)}\ntupleD: {type(tupleD)}")

"""
Then what is the difference between a list and a tuple? Answer is: 

list is mutable
tuple is immutable

What the fuck is 'mutable'? It means you CAN change the values after you defined it.
In tuples, you CAN'T change the values after you defined it.
"""

listA[0] = 7
print(listA) # See? You can change it. Python doesn't give a fuck

tupleA[0] = 7
print(tupleA) # Did you think you can change it? You dumbass.