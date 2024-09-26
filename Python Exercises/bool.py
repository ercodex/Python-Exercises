# This code explains some Boolean terms

print(4 == 4)
print(4 == 4.0) #Even though they are different data types, Python recognizes that they're equal.
print(3 > 5)

# There is no || or && in Python. You'll use direct keywords.
x = 12
print("\n", x > 10 and x < 16) # Is x is higher than 10 and lower than 16?
print(x > 16 or x < 13)

# Like int(), str(), float(); we can turn numbers into boolean data type
a = 0
print("\n", type(a))
print(type(bool(a)))

# 0 is the only number that will convert to False. Every other number or string will return True.
b = 35
print(bool(b))
c = 'asd'
print(bool(c))

# The only way to get False with strings is entering an 'empty string' into bool function.
print(bool(''))