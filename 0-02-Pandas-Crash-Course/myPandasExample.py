import numpy as np
import pandas as pd

# df = pd.read_csv('salaries.csv')
# # print(df['Salary'].mean())

# ser_of_bool = df['Age'] > 30
# # print(df[ser_of_bool])
# # print(df[df['Age'] > 30])

# # print(df['Age'].unique())
# # print(df.columns)

# # print(df.info())

# print(df.index)

mat = np.arange(0, 10).reshape(5, 2)
# print(mat)
df = pd.DataFrame(data=mat, columns=['A', 'B'], index=[
                  'A', 'B', 'C', 'D', 'E'])
print(df)
