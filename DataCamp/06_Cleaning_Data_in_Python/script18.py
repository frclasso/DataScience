import pandas as pd

ebola = pd.read_csv('ebola_data_db_format.csv')


#print(ebola.head())

# #Assert that there are no missing values
assert pd.notnull(ebola).all().all()

## Assert that all values are >= 0
assert (ebola >= 0).all().all()
