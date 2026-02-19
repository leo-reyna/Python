import os
import pandas as pd
import numpy as np

os.system('cls')

# data = [["John", 41], ["Jane", 45], ["Jean", 56],  ["Jose", 49]]
# df = pd.DataFrame(data, columns=['Name','Age'])
# print(df)
 
records = [["John", 41,"EMP001"], ["Jane", 45, "EMP001"], ["Jean", 56],["Jake", 44,"EMP001"]]
staff = pd.DataFrame(records, columns=['Name','Age', 'ID'])
print(staff)

coffeetype = {'Event': ["January 28th-29th Blizzard", "February 19th Snow Squall"]}
