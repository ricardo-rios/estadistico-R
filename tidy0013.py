import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re


def extract_year(string):
    match = re.match(".+(\d{4})", string) 
    if match != None: return match.group(1)


    
path = 'https://raw.githubusercontent.com/ricardo-rios/estadistico-R/master'
#allFiles = glob.glob(path + "/201*-baby-names-illinois.csv")
allFiles = ["https://raw.githubusercontent.com/ricardo-rios/estadistico-R/master/2014-baby-names-illinois.csv", "https://raw.githubusercontent.com/ricardo-rios/estadistico-R/master/2015-baby-names-illinois.csv"] 
frame = pd.DataFrame()
df_list= []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    df.columns = map(str.lower, df.columns)
    df["year"] = extract_year(file_)
    df_list.append(df)

df = pd.concat(df_list)
print(df.head())

