#!/usr/bin/env python3

import pandas as pd

sales = pd.ExcelFile("movie_theater_sales_data.xlsx")

# atributos nao levam parenteses
sales_sheet_names = sales.sheet_names

print(sales_sheet_names)
print()

sales_report = sales.parse('sales')
print(sales_report.head())