import os
import pandas as pd

os.system('cls')


import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,index=None, columns=['Name','Age'])
print(df)