import pandas as pd

# Import the ticket sales file
sales = pd.read_excel('ticket_sales.xlsx')

# Summary of movies and locations
theater_movie_summary = sales.groupby(['theater_location', 'movie_title'], as_index=False).sum()

# Get average ticket sales by movie title
avg_sale_by_movie = theater_movie_summary.groupby('movie_title', as_index=False).mean()

# Sort average ticket sales in descending order
movies_sorted = avg_sale_by_movie.sort_values('ticket_quantity', ascending=False).reset_index(drop=True)

# Print results
print(movies_sorted.head(1))