#!/usr/bin/env python3

import pandas as pd

sales = pd.read_excel("movie_theater_sales_data.xlsx")

#print(sales.info())
# theater_name, movie_title, ticket_type, ticket_quantity


# 1 summary movies and theaters
theater_movies_summary = sales.groupby(['theater_name', 'movie_title'], as_index=False).sum()

# 2 Get average ticket sales by movie title
avg_sales_by_movie = theater_movies_summary.groupby('movie_title', as_index=False).mean()
print(avg_sales_by_movie)