import pandas as pd

df = pd.read_csv('titanic.csv')

print(df.Age + df.Age)

print(df.Age *  df.Age)

print(df.Age + 100)

print(df.Age * 3) 

print(df.Age + pd.Series([1,100]))

print(df.Age)

rev_ages = df.Age.sort_index(ascending=False)
print(rev_ages)


