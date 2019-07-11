#!/usr/bin/env python3

import pandas as pd

#1
sales = pd.read_excel("movie_theater_sales_data.xlsx")
#print(sales.head())
#print(sales.info())

#2
groups = ['theater_name', 'movie_title']
by_name_title = sales.groupby(groups, as_index=False).sum()

print(by_name_title)