
import pandas as pd
import matplotlib.pyplot as plt


ebola = pd.read_csv('ebola_data_db_format.csv')
country = pd.read_csv('status_country.csv')

print(country.head())
print(country.columns)

# ebola_melt = pd.melt(ebola, id_vars=['Date', 'value'], var_name='type_country', value_name='counts')
# status_country = pd.melt(country)
#
# # Concatenate ebola_melt and status_country column-wise: ebola_tidy
# ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)
#
# # Print the shape of ebola_tidy
# print(ebola_tidy.shape)
#
# # Print the head of ebola_tidy
# print(ebola_tidy.head())
