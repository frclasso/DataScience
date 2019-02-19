import pandas as pd

# Assign the filename: file
file = 'Titanic_2.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())
