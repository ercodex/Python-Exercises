# List can be used in multiple ways

# Integers in a list
aList = [ 1, 2, 3 ]
print(type(aList))

# Strings in a list
bList = [ 'eren', 'irem']
print(type(bList))

# Multiple variable types in a list
cList = [ 21, 'eren', -3.1, 'i' ]
print(type(cList))

# List in a list
dList = [ 5, 3, [8, 'erdem', 'hamza', 5.9], 'eren', 9.3 ]

# We can implement lists like this to make it more readable
dList = [
        5, 
        3, 
        [8, 'erdem', 'hamza', 5.9], 
        'eren', 
        9.3
        ]
print(type(dList))
# We also see that no matter what's inside a list, it's variable type is a 'list'

# Checking whether a list contains a specific element
print("\n'21' being in cList: ", 21 in cList)
print("'hamza' being in cList: ", 'hamza' in cList)

# We can also use 'not in' keyword
print("\n'21' not being in cList: ", 21 not in cList)
print("'hamza' not being in cList: ", 'hamza' not in cList)

# We can concatenate and multiply lists
print("\nConcatenated list: ", aList + bList)
print("Multiplied list: ", aList * 3)

# We can find the length of a list with 'len'
print("\nLength of dList: ", len(dList))

# We can add and remove elements from lists
aList.append(4)
print("\nAppended element '4' to aList: ", aList)
aList.pop(3) # Element at index 3
print("Removed the element '4' in aList: ", aList)
aList.remove(1) # Remove what's inside the 'remove()' function
print("Removed the element '1' in aList", aList)

# We can sort elements in lists with 'sort()' function
sortingList = [ 9, 5, 6, 1, 7, 5, 4, 0, 2 ]
print("\nUnsorted list: ", sortingList)
sortingList.sort() #If you want vice versa, use like this: sort(reverse=True). Default is ascending order
print("Sorted list: ", sortingList)

# We can find 'how many times a specific element appeared in a list' with a list method
eList = [ 1, 1, 1, 2, 3, 4, 4]
print(f"\nElement '1' appeared {eList.count(1)} times in eList")

# We can insert an element wherever we want
eList.insert(3, 5) # Insert 5 at index 3. We can also insert string (obviously)
print("\nInserted '9' at index 3: ", eList)