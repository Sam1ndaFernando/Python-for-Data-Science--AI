# import numpy as np
# a = np.array([1, 2, 3, 4])  
# print(a)
# print(type(a))


# //////////////////////////////////////////////////////////////////////////////////////////////

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35],'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df)
print(type(df))