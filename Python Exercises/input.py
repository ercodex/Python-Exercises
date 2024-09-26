# When we use the function called 'input()', it returns a value in string type

x = input("Enter value: ")
print(type(x))

# Un-comment this line of code and read the error message
# print(x + 3)

# This works because obviously we can add two strings like this:
print(x + ' monkeys having sex')

# We can convert types like this
int(x)
float(x)