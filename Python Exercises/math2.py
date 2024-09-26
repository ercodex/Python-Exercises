# You can take powers and square roots like this in Python
# I named this file as 'math2.py' because otherwise, it overwrites to the 'math.py' library

print(3 ** 2)
print(9 ** (1/2))

# Let's play!
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))

c = (a**2 + b**2) ** (1/2)
print(f"Hypotenuse is {c}")