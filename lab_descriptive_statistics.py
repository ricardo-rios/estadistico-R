import pandas as pd

data = {'name': ['Max', 'Raff', 'Cayce', 'Mike', 'Rigsby'],
        'age': [10, 7, 45, 50, 2],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}

df = pd.DataFrame(data, columns = ['name', 'age', 'preTestScore', 'postTestScore'])

print(df)


print(df['age'].sum())

print(df['preTestScore'].mean())

print(df['preTestScore'].cumsum())
print(df['preTestScore'].describe())


print(df['preTestScore'].count())

print(df['preTestScore'].min())

print(df['preTestScore'].max())



