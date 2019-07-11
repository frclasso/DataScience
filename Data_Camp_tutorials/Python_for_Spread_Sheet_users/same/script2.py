#!/usr/bin/env python3

# Pivot data
import pandas as pd

#1
fruit_sales = pd.read_excel("fruit_stores.xlsx")
print(fruit_sales.head())
print()

#2
print(fruit_sales.sum(numeric_only=True))
print()

#3
# group by
print(fruit_sales.groupby('store', as_index=False).sum())