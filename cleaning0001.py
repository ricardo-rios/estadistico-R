import pandas as pd
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/ricardo-rios/estadistico-R/master/BL-Flickr-Images-Book.csv')

print(df.head())

to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']


df.drop(to_drop, inplace=True, axis=1)
# Otra forma
# df.drop(columns=to_drop, inplace=True) 

print(df.head())


print(df['Identifier'].is_unique) 

df = df.set_index('Identifier')
print(df.head())

print("Usando df.loc") 
print(df.loc[206]) 

print(df.get_dtype_counts())

print(df.loc[1905:, 'Date of Publication'].head(10)) 


extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)

print(extr.head())

df['Date of Publication'] = pd.to_numeric(extr)
df['Date of Publication'].dtype

print(df['Date of Publication'])

print(df['Date of Publication'].isnull().sum() / len(df)) 

