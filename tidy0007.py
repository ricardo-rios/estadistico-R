import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re

df = pd.read_csv("https://raw.githubusercontent.com/ricardo-rios/estadistico-R/master/tb-raw.csv")
print(df.head())

print(df.columns)

df = pd.melt(df, id_vars=["country","year"], value_name="cases", var_name="sex_and_age")
print(df.head())
