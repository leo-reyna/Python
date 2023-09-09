# DataFrame Examples
# LR 


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