import numpy as np
import pandas as pd

# Variable names
labels = ['Temp (C)', 'Ice Cream']

var1 = np.random.randn(100) *5 + 20
var2 = var1 > 20

D = { labels[0]: var1, labels[1]:var2}

df = pd.DataFrame(data = D)
print(type(df))
print(df)

# You can use nice methods of dataframes
print(df.head())
print(df.count())
print(df.mean())