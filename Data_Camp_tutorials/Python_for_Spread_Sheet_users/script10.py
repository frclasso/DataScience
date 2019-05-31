# Import viz packages
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_excel('ticket_sales.xlsx')

genre_totals = sales.groupby('movie_genre', as_index=False).sum()

genre_totals = genre_totals.sort_values('revenue', ascending=False).reset_index(drop=True)

# Create barplot
sns.barplot(x='movie_genre', y='revenue', data=genre_totals)

# Display barplot
plt.show()