
import pandas as pd

# Import the ticket sales file
sales = pd.read_excel('ticket_sales.xlsx')


# Summarize by movie title and ticket type
movies_by_ticket_type = sales.groupby(['movie_title', 'ticket_type'], as_index=False).sum()

# Filter for senior tickets
senior_ticket_movies = movies_by_ticket_type[movies_by_ticket_type['ticket_type'] == 'senior'].reset_index(drop=True)

# Sort senior ticket sales descending
ordered_senior_movies = senior_ticket_movies.sort_values('ticket_quantity', ascending=False).reset_index(drop=True)

# Print the top 3 rows of the ordered table
print(ordered_senior_movies.head(3))