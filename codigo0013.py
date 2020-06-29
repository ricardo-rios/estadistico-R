import pandas as pd

df = pd.read_csv('titanic.csv')

print(df.Age.mean())
print(df.Age.min())
print(df.Age.max())
print(df.Age.median())

print(df.Age.describe())
