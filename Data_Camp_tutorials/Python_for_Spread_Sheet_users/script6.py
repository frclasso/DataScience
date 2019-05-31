
import pandas as pd

# Import the ticket sales file
sales = pd.read_excel('ticket_sales.xlsx')


# Create a summary by theater location and movie title
totals = sales.groupby(['theater_location', 'movie_title'], as_index=False).sum()

# Sort totals by ticket quantity in descending order
totals_sorted = totals.sort_values('ticket_quantity', ascending=False).reset_index(drop=True)

# Take the top row for each theater location
top_movies = totals_sorted.groupby('theater_location').head(1).reset_index(drop=True)

# Print results
print(top_movies)