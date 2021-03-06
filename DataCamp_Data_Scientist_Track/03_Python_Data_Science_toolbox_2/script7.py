#!/usr/bin/env python3

"""Now let's use your generator function to process the World Bank dataset
like you did previously. You will process the file line by line, to create
a dictionary of the counts of how many times each country appears in a column
in the dataset. For this exercise, however, you won't process just 1000 rows
of data, you'll process the entire dataset!"""

def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print
#print(counts_dict)
for result in counts_dict.items():
    print(result)