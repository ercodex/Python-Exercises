a = range(3, 15)
print(type(a))
print(a) # We need to convert this range into a list

a = list(range(3, 15))
print(type(a))
print(a)

# You can select a range to print (slicing)
print(a[0:2])

# What happens when we want to take elements in specific pattern
print(a[::2]) # Skip by two
print(a[::3]) # Skip by three
# This method is used to down-sample data. When we have thousands of lines of data, we can take a
# smaller subset with this method

# We can interpret this notation like this:
#     a( 'start' : 'stop' : 'skip' )

start = 0
stop  = 3
skip  = 1

print(a[start:stop:skip]) # Same with a[0:3:1]

# To reverse a list:

print(a[::-1])