#!/usr/bin/env python3

import pandas as pd

file = pd.read_excel('fruits.xlsx')

print(file)
print()

#2
print(file.head())

print()
print(file.info())


print()
print(file.describe())

# 3
print()
file_sorted = file.sort_values('name', ascending=False)
print(file_sorted)

# 4 filter
# file_filter = file[file['name'] == 'Orange'].reset_index(drop=True)
# print(file_filter(5))

# 5 - criando uma coluna
print()
file['files_usd'] = file['price'] * 2
print(file.head())