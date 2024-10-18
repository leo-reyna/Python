# DataFrame Examples
# LR 
import  os
os.system = ('cls')

# empty dataframe
import pandas as pd
df = pd.DataFrame()
print (df)

# adding values
import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df)

# adding values ex.2
import pandas as pd
data =['Alex', 28], ['Peter', 20], ['Joe', 23]
df = pd.DataFrame(data)
print (df)

# Other Data Types List
import pandas as pd
records = [["John", 41,"EMP001"], ["Jane", 45, "EMP001"], ["Jean", 56],["Jake", 44,"EMP001"]]
staff = pd.DataFrame(records, columns=['Name','Age', 'ID'])
print(staff)

# Create a DataFrame from Dict of ndarrays / Lists. All the ndarrays must be of same length. If index is passed, then the length of the
# index should equal to the length of the arrays. #If no index is passed, then by default, index will be range(n), where n is the array length.
# running the code below,  note the values 0,1,2,3. They are the default index assigned to each using the function range(n).
import os
import pandas as pd

os.system = ('cls')
data = {'name':['Joe', 'Paul', 'Thomas'], 'occupation': ['dentist','barber','farmer'], 'age' : [29, 30, 54]}
data2 = {'name':['Jack', 'OJ', 'Jerome'], 'occupation': ['cleaner','actor','artist'], 'age' : [25, 36, 33],'location':['usa', 'europe', 'japan']}
# with index: 
# df = pd.DataFrame(data, index=['rnk1', 'rnk2', 'rnk3'])
# without index:
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

# merging 2 dataframes
df_merged = pd.concat([df1, df2], ignore_index=True, sort=False) 
print (df_merged)
print(f"This set contains {len(df_merged)} rows of data")

# import the pandas library and aliasing as pd

import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)

# Create a Series from dict
import pandas as pd
import numpy as np
data = {'a' : 0, 'b' : 1., 'c' : 4.}
s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s)

