import pandas as pd

ser = pd.Series([1, 3, 5, 7])
print(ser)

prices = {'apple': 4.99,
         'banana': 1.99,
         'orange': 3.99,
         'grapes': 0.99}

ser = pd.Series(prices)
print(ser)

ser = pd.Series(2, index=range(0, 5))
print (ser)


