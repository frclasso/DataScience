# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop_data.csv', chunksize=10)



# Print two chunks
print(next(df_reader))
print(next(df_reader))



"""Another way to read data too large to store in memory in chunks is to 
read the file in as DataFrames of a certain length, say, 100. For example, 
with the pandas package (imported as pd), you can do pd.read_csv(filename, 
chunksize=100). This creates an iterable reader object, which means that 
you can use next() on it."""