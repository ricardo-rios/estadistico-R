import pandas as pd
mdf = pd.read_csv("http://bit.ly/imdbratings")

print(mdf.iloc[0])

print(mdf.iloc[99])

print(mdf.ix[2]) 


