# Exercise for transforming loops into single-line loops.

newList = ['']*10

for i in range(10):
    if i%2 == 1:
        newList[i] = 'Odd'
    else:
        newList[i] = i

print(newList)

print("\n-----Solution-----")

# First attempt. Error was trying to make two assignments at the same time.
# lst = [ newList[i] = 'Odd' if i%2 == 1 else newList[i] = i for i in range(10) ]

lst = [ 'Odd' if i%2 == 1 else i for i in range(10) ]
print(lst)