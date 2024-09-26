# Motherfucking Python!!! Turns out that, it doesn't create a copy of a, (unlike other languages)
# It only creates a pointer to the location that variable 'a' hold at hardware
a = [4, 3]

b = a
b[0] = 5

print(a)
print(b)

# To see that, let's look at their locations:
print(id(a))
print(id(b))
# It's fucking sameeeee

# So, 'b' is simply a new reference to 'a', instead of being a separate variable from 'a'
# To create a copy, we should use:
c = a[:]
c[0] = 9

print(f"'c' is {c}")
print(f"'a' is {a}")
print("Locations of c and a: ")
print(id(c))
print(id(a))

# This only works on simple things though. For further use, we need to use the library 'copy'
# It is more reasonable to do this way.

import copy

d = { 'name': 'eren', 'surname': 'cil'}
e = copy.deepcopy(d)

print("\nLocations of dictionaries copied with the 'copy' library:")
print(id(d))
print(id(e))