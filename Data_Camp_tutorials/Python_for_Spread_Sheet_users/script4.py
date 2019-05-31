
import pandas as pd

# Import the ticket sales file
sales = pd.read_excel('ticket_sales.xlsx')

# Create a list of groups to group by
groups = ['theater_location', 'movie_title']

# Create summary table of genres and locations
by_location_genre = sales.groupby(groups, as_index=False).sum()

# Print the summary table
print(by_location_genre)

by_location_genre.to_excel('tickets_copy.xlsx')

