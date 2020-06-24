import pandas as pd
mdf = pd.read_csv("http://bit.ly/imdbratings")

print(mdf.head())

print(mdf.loc[0])

print(mdf.loc[[0, 10, 30]]


