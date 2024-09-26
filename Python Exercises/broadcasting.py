# In Linear Algebra, adding matrices and vectors directly is not legal.

# But Python analyses both and determines whether you want to do this operation
# column-wise or row-wise, then proceeds to calculate properly. And this is called "broadcasting"

# Python can handle different-sized matrices at the same time, determining what to do in a 
# logical way.

import numpy as np
import copy 
# Matrix X
X = np.array([ [1, 2, 3],
               [2, 3, 4],
               [3, 4, 5],
               [4, 5, 6] ])

# Vector W
w = np.array([10, 20, 30])

print(f"---Matrix X---\n{X}")
print(f"\n---Vector w---\n{w}")

# Now, we want to add these both together. I mean, vector w to the each row of X.
Z = X + w # Also works for multiplication etc.
print(f"\n---Added Matrix---\n{Z}") # What in the actual fuck?

#---------------------------------------------------------------------------

# What we actually doing is:
Y  = copy.deepcopy(X)  # This was the one way of copying. Did this to not lose original X

Y_ = np.zeros(X.shape) # And this is the other one. Creates a matrix 
                       # as the same size as X and fills it with zeros.
                       # Just created for educational purposes. Y_ will 
                       # not be used.

for i in range(X.shape[0]): # shape() method returns the number of rows (shape[0]) and columns (shape[1]).
    X[i, :] += w


#---------------------------------------------------------------------------
# We can also make column-wise operations. But first, we need to convert vectors.
# Learn more on broadcasting2.py