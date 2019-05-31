import pandas as pd

file = pd.read_csv('clientes_grande.csv')

# print(file.info())
# print(file.head())
# print(file.tail())
# print(file.shape)
# print(file['nome'])


d1 = file[['nome', 'idade', 'cidade', 'email']].head()
print(d1)

d1.to_csv('dataframe1.csv')