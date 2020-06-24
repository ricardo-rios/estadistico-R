import pandas as pd
mdf = pd.read_csv("http://bit.ly/imdbratings")

print(mdf.head())

print(mdf.tail())

subset = mdf[['start_time', 'duration']]

print(subset.head())

subset = mdf[[0, 1]]

print(subset.head())
