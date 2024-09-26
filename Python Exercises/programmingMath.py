x = 7
y = 4.3
z = 0

print(y + x - 7) # = 4.300000000000001

"""
Where this ..000001 comes from?

Floating-point algebra is not the same thing as real algebra. On computers, we
are not implementing the real algebra. We are implementing 'floating-point algebra'.
Because computers have limited precision, they cannot represent arbitrarily small or 
arbitrarily large numbers. And we got some tiny tiny computer rounding errors that are
essentially zero. We can ignore them. When we work with math in programming, we'll see
this very often.
"""