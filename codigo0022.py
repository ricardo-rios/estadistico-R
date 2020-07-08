import pandas as pd
import numpy as np 
from sklearn import preprocessing
import matplotlib.pyplot as plt

data = {'score': [234, 24, 14, 27, -74, 46, 73, -18, 59, 160]}

df = pd.DataFrame(data)
print(df.head())

df['score'].plot(kind='bar')
plt.show()

x = df['score'].values.astype(float)
print(x.shape)
x = np.reshape(x,(-1, 1))
print(x.shape)

min_max_scaler = preprocessing.MinMaxScaler()

x_scaled = min_max_scaler.fit_transform(x)

df_normalized = pd.DataFrame(x_scaled)

print(df_normalized.head())


