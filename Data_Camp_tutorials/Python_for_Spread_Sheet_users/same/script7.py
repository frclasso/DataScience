#!/usr/bin/env python3

# lendo multiplas sheets

import pandas as pd

# lendo o workbook
fruit_workbook = pd.ExcelFile('fruit_tabs.xlsx')

print(fruit_workbook)
# saida <pandas.io.excel.ExcelFile object at 0x7fc5e99a3cf8>
print()

# Obtendo atributos das planillhas
# get sheet names
fruit_sheet_names = fruit_workbook.sheet_names
print(fruit_sheet_names)
print()

#Parse price tab
fruit_prices = fruit_workbook.parse('price')
print(fruit_prices)