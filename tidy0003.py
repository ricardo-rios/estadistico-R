import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re

df = pd.read_csv("https://raw.githubusercontent.com/ricardo-rios/estadistico-R/master/billboard.csv", encoding="mac_latin2")

print(df.head(10))

print(df.tail(10))

indexs = df["artist.inverted"] == "Santana"
print(df[indexs]) 

print(df.columns)
