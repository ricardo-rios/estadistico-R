import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('Datos.xlsx', sheet_name='Sheet1')

print(df.head())

print("Column headings:")
print(df.columns)

print(df['A'])

print(df['B'])

print(df['C'])
