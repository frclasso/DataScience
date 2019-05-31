import pandas as pd

excel = pd.read_excel('225-5000-composite-inventory_2015-12-16.xlsx')
print(excel.head())
# print(excel.info())
# print(excel.describe())  # estatistica
excel = excel.sort_values('TOTAL', ascending=False)
excel = excel.reset_index(drop=True)
print(excel.head(10))

# print(excel)

# e = pd.ExcelFile('225-5000-composite-inventory_2015-12-16.xlsx')


#print(e.sheet_names)

# print(e.parse('Sheet1'))

# df = pd.DataFrame('225-5000-composite-inventory_2015-12-16.xlsx')
# print(df.info())
