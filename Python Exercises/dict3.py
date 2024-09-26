# Is there a way to check whether an element exists in 'values' part of a dict?

E = { 
    'name': 'eren',
    'age': 20, 
    'height': 178.2, 
    'brothers': ['erdem', 'hamza'] 
    }

print('name' in E) # It prints True

values_of_E = E.values()

print('eren' in values_of_E) # Yes :)