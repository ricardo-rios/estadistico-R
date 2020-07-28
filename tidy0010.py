import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re

df = pd.read_csv("https://raw.githubusercontent.com/ricardo-rios/estadistico-R/master/weather-raw.csv")

print(df.columns)

df = pd.melt(df, id_vars=["id", "year", "month", "element"], value_name="value", var_name="day_raw")
print(df.head())

# Extracting day
df["day"] = df["day_raw"].str.extract("d(\d+)", expand=False)  
df["id"] = "MX17004"
print(df.head())
