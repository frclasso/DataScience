#!/usr/bin/env python3

import pandas as pd

movies = pd.read_excel('movie_theater_sales_data.xlsx')

print(movies)

#2
print(movies.head())

# 3

print(movies.info())


print()
print(movies.describe())


# 4
print()
sorted_movies = movies.sort_values('theater_name', ascending=False).reset_index(drop=True)
print(sorted_movies)
print()

#5
empirical_house = movies[movies["theater_name"] == 'The Empirical House'].reset_index(drop=True)
print(empirical_house.head(3))



