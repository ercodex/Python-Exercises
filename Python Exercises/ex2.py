# Create a pandas dataframe with:
# Integers going from 0 to 10, their square, and their log

import pandas as pd
import numpy as np

nums = np.array(range(11))

df = pd.DataFrame( {'nums': nums, 'square': nums**2, 'log': np.log(nums)} )
print(df)
