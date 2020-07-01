import pandas as pd

df = pd.read_csv('titanic.csv')

ages = df['Age']
print(ages)

print(ages[ages < ages.mean()])

print(ages[ages > ages.mean()])

print(ages > ages.mean())

print(type(ages > ages.mean()))
