
import pandas as pd

# Import the ticket sales file
sales = pd.read_excel('ticket_sales.xlsx')

# Create a summary by movie genre
genre_summary = sales.groupby('movie_title',as_index=False).sum()

# Sort summary in descending order of tickets sold
genres_sorted = genre_summary.sort_values('ticket_quantity', ascending=False).reset_index(drop=True)

# Print the sorted summary
print(genres_sorted)