import pandas as pd
Dates= {'dates': ['05Sep2009','13Sep2011','21Sep2010']}
table1 = pd.DataFrame(Dates)#converting the given input into a table
print(table1)
table1['dates'] = pd.to_datetime(table1.dates)#converting the format of the input
print(table1)
