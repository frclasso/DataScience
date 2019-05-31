import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_excel('ticket_sales.xlsx')
genre_totals = sales.groupby('movie_genre', as_index=False).sum()


sns.barplot(x='movie_genre', y='revenue', data=genre_totals)

# Add a title
plt.title('Revenue by Genre')

# Add x axis label
plt.xlabel('Movie Genre')

# Add y axis label
plt.ylabel = ('Revenue (USD)')

plt.show()