import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re

df = pd.read_csv("https://raw.githubusercontent.com/ricardo-rios/estadistico-R/master/billboard.csv", encoding="mac_latin2")

# Melting
id_vars = ["year",
           "artist.inverted",
           "track",
           "time",
           "genre",
           "date.entered",
           "date.peaked"]


df = pd.melt(frame=df,id_vars=id_vars, var_name="week", value_name="rank")

print(df.head())

# Formatting 
df["week"] = df['week'].str.extract('(\d+)', expand=False).astype(int)

#print(df["week"].unique())


#print(df["rank"].unique())
#df["rank"] = df["rank"].fillna(-1) 

# Cleaning out unnecessary rows
df = df.dropna()

df["rank"] = df["rank"].astype(int)


# Create "date" columns
df['date'] = pd.to_datetime(df['date.entered']) + pd.to_timedelta(df['week'], unit='w') - pd.DateOffset(weeks=1)

df = df[["year", 
         "artist.inverted",
         "track",
         "time",
         "genre",
         "week",
         "rank",
         "date"]]
df = df.sort_values(ascending=True, by=["year","artist.inverted","track","week","rank"])

# Assigning the tidy dataset to a variable for future usage
billboard = df

print(df.head(10))
