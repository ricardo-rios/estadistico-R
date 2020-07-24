from sklearn.preprocessing import Normalizer
import pandas
import numpy


url = "https://raw.githubusercontent.com/nebiljabari/Pima-Indian-Diabetes-Study/master/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
print(dataframe.head())
array = dataframe.values

X = array[:,0:8]
Y = array[:,8]
print(X)
print(Y)

scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)

numpy.set_printoptions(precision=3)
print(normalizedX[0:5,:])



