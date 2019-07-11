#!/usr/bin/env python3

import pandas as pd

#1
fruit_sales = pd.read_excel("fruit_stores.xlsx")

#print(fruit_sales.head())

#2 - summary - by fruit by store
totals = fruit_sales.groupby(['store', 'product_name'], as_index=False).sum()
print(totals)

#3 - sort the summary
print()
totals = (totals.sort_values('revenue', ascending=False).reset_index(drop=True))
print(totals)

# 4 First row for each store
print()
top_store_sellers = totals.groupby('store').head(1).reset_index(drop=True)
print(top_store_sellers)