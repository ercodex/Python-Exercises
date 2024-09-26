# This code explains dictionaries

# lists []
# tuples ()
# dictionaries {}

# Dictionaries are made of key/value pairs. And both cannot exist without the other.
# They are also not in order.

# We can initialize dictionaries in two ways
D = dict()
print(D) # In this case, it is an empty dictionary
D['name'] = 'erdem' # You can create key/value pairs like this
print(D)

# Other method
E = { 'name': 'eren', 'age': 20, 'height': 178.2, 'brothers': ['erdem', 'hamza'] }
print(E)

# How to know every key in a dict?
print(E.keys())

# We can check whether a dict contains a specific element. Only works in keys.
print('name' in E)

# How to know every value in a dict?
print(E.values())

# This function returns every item in tuples form
print(E.items())