import pandas as pd
import numpy as np

gapminder = pd.read_csv('gapminder1.csv')

# Convert the year column to numeric
gapminder.Year = pd.to_numeric(gapminder.Year)

# Test if country is of type object
assert gapminder.Country.dtypes == np.object

# Test if year is of type int64
assert gapminder.Year.dtypes == np.int64

# Test if life_expectancy is of type float64
assert gapminder.life_expectancy.dtypes == np.float64