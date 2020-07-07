import pandas as pd

smartdudes = pd.DataFrame( \
               data={'Occupation':['Genius', 'SmartestHumanEver'],
               'Born':['1879-03-14', '1643-01-04'],
               'Died':['1955-04-18', '1727-03-31'],
               'Age':[76, 84]},
               index=['Albert Einstein', 'Isaac Newton'],
               columns=['Occupation','Born','Died','Age'])


print(smartdudes)


smartdudes.columns = ['Occupation','Born','Died','Age']

smartdudes.rename(columns={'Occupation': 'Title'}, inplace=True)
print(smartdudes)

