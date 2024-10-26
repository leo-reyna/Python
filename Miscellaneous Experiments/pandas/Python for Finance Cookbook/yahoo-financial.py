import pandas
import yfinance as yf
import os
os.system("cls")

# Examples book Python for Finance 2nd Edition
# df.head() will display the first five rows of the dataframe, 
# and df.head(n) will display the first n rows of the dataframe.
# df.tail() will display the last five rows of the dataframe, 
# and df.tail(n) will display the last n rows of the dataframe.

df = yf.download((["AAPL", "MSFT"]), # Apple and Microsoft
                 start="2020-01-01",
                 end="2021-12-31",
                 progress=False)

print(f"Downloaded {len(df)} rows of data")
print(df.head)
