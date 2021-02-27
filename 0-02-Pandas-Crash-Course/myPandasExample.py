import numpy as np
import pandas as pd

# df = pd.read_csv('salaries.csv')

# ser_of_bool = df['Age'] > 30

# print(df['Age'].nunique())

# print(df.index)

mat = np.arange(0, 50).reshape(5, 10)
# print(mat)
df = pd.DataFrame(data=mat)
print(df)
