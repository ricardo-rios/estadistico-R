import pandas as pd

df = pd.read_csv('titanic.csv') 

print(df.groupby('Age')['Sex'].nunique())
