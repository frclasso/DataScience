# Import pandas
import pandas as pd
import matplotlib.pyplot as plt


ebola = pd.read_csv('ebola_data_db_format.csv')

print(ebola.columns)
# print(ebola.head())
# print(ebola.info())
# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'value'], var_name='type_country', value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())
