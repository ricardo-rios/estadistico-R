import pandas as pd
import numpy as np

# Create dataframe
raw_data = {'team': ['kiddies', 'kiddies', 'kiddies', 'kiddies', 'FireDogs', 'FireDogs', 'FireDogs', 'FireDogs', 'Mambaas', 'Mambaas', 'Mambaas', 'Mambaas'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'Lastname': ['Miller', 'Jackson', 'Smith', 'Williams', 'West', 'Jack', 'Ryaner', 'Stone', 'Sloan', 'Piper', 'Roesewood', 'Petaway'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['team', 'company', 'Lastname', 'preTestScore', 'postTestScore'])
print(df)


print(df.sort_values(by="Lastname", ascending=0))

print(df.sort_values(by="team", ascending=0))


print(df.sort_values(by=["preTestScore", "Lastname"]))
