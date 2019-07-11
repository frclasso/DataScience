#!/usr/bin/env python3

import pandas as pd

sales = pd.read_excel("movie_theater_sales_data.xlsx")

#print(sales.info())
# theater_name, movie_title, ticket_type, ticket_quantity

# 1 Create a summary by theater location and movie title
totals= sales.groupby(['theater_name', 'movie_title'], as_index=False).sum()
print(totals)
print()

# 2 Sort totals by ticket quantity in descending order
totals_sorted = totals.sort_values('ticket_quantity', ascending=False).reset_index(drop=True)
print(totals_sorted)
print()

# 3 Take the top row for each theater location
top_movies = totals_sorted.groupby('theater_name').head(1).reset_index(drop=True)
print(top_movies)
print()
