import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re

df = pd.read_csv("https://raw.githubusercontent.com/ricardo-rios/estadistico-R/master/pew-raw.csv")
print(df.head())

formatted_df = pd.melt(df,
                       ["religion"],
                       var_name="income",
                       value_name="freq")
formatted_df = formatted_df.sort_values(by=["religion"])
print(formatted_df.head(10))


