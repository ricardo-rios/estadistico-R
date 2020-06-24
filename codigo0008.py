import pandas as pd

df = pd.read_csv('titanic.csv') 

print(df.groupby('Pclass')['Survived'].mean())
print(df.groupby('Pclass')['Age'].mean())
