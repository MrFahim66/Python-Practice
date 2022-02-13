import pandas as pd

lst = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

df = pd.DataFrame(lst, index=['A', 'B'], columns=['a','b','c','d','e','f'])
print(df)
print(df.iloc[0]['a'])