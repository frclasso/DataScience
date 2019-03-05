import pandas as pd
import numpy as np

gapminder = pd.read_csv('gapminder1.csv')

# Create the series of countries: countries
countries = gapminder['Country']

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Assert that country does not contain any missing values
assert pd.notnull(gapminder.Country).all()

# Assert that year does not contain any missing values
assert pd.notnull(gapminder.Year).all()

# Drop the missing values
gapminder = gapminder.dropna()

# Print the shape of gapminder
print(gapminder.shape)
