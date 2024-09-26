"""
Yes, print() function shows things on screen. But it always returns None.
It doesn't produce a value by itself. So if you try to assign it to a variable
and print, -since it returns None- it will print "None".
"""

recepivedik = print("bohohoyt") # Side effect of this line is, it prints even you're just assigning it.
print(recepivedik) # This variable has a value of "None"

# This prints numbers.
erdem = [ j**2 for j in range(10) ] # This is the list of squared numbers from 0 to 9.
print(erdem) # And it prints squared numbers in a list, normally.

erdem = [ print(j**2) for j in range(10) ] # Side effect of this line is, it prints even you're just assigning it.
print(erdem) # Since we're printing the 'prints' here, they all return None