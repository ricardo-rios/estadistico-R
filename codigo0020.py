import pandas as pd
import numpy as np
import re as re

# Create dataframe
raw_data = {'team': ['kiddies', 'kiddies', 'kiddies', 'kiddies', 'FireDogs', 'FireDogs', 'FireDogs', 'FireDogs', 'Mambaas', 'Mambaas', 'Mambaas', 'Mambaas'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'Lastname': ['Miller', 'Jackson', 'Smith', 'Williams', 'West', 'Jack', 'Ryaner', 'Stone', 'Sloan', 'Piper', 'Roesewood', 'Petaway'], 
        'email': ['miller@gmail.com', 'jackson@gmail.com', 'smith@gmail.com', 'williams@gmail.com', 'west@gmail.com', 'jack@gmail.com',  'ryaner@gmail.com', 'stone@gmail.com', 'sloan@gmail.com', 'pipper@gmail.com', 'rosewood@gmail.com', 'petaway@gmail.com'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['team', 'company', 'Lastname', 'email', 'preTestScore', 'postTestScore'])
print(df)

print(df['email'].str.contains('gmail'))


regPat = '([A-Z0-9._%+-]+)+@([A-Z0-9.-]+)\\.([A-Z]{2,4})'

print(df['email'].str.findall(regPat, flags=re.IGNORECASE))


