#!/usr/bin/env python3

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn',
              'boromir', 'legolas', 'gimli', 'gandalf']

# Filtrando strings com mais de 6 caracteres
# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda n: len(n) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Convert result into a list and print it
print(result_list)