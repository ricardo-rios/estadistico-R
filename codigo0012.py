import pandas as pd

smartdudes = pd.DataFrame( \
               data={'Occupation':['Genius', 'SmartestHumanEver'],
               'Born':['1879-03-14', '1643-01-04'],
               'Died':['1955-04-18', '1727-03-31'],
               'Age':[76, 84]},
               index=['Albert Einstein', 'Isaac Newton'],
               columns=['Occupation','Born','Died','Age'])
               

print(smartdudes)

first_row = smartdudes.loc['Albert Einstein']
print(type(first_row))
print(first_row)

print(first_row.index)
print(first_row.values)
print(first_row.keys())
