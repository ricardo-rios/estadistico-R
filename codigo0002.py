import pandas as pd
mdf = pd.read_csv("http://bit.ly/imdbratings")

print(mdf.head())

print(type(mdf))

print(mdf.shape)

print(mdf.columns)

print(mdf.dtypes)
