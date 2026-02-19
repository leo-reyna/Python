
import pandas as pd
import numpy as np
import os

os.system("cls")

data = [1,1,1,2] # The DataFrame can be created using a single list or a list of lists.
df = pd.DataFrame(data)
print(df)

data2 = [['John', 43], ['Bob', 55], ['Kurt', 34]] 
df = pd.DataFrame(data2, columns=['Name','Age']) # columns
print(df)

print("-----------------")

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c']) # array
print(df2)