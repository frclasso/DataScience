

# Import viz packages
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_excel('ticket_sales.xlsx')

movie_totals = sales.groupby('movie_title', as_index=False).sum()

movie_totals = movie_totals.sort_values('revenue', ascending=False).reset_index(drop=True)

# Create barplot
sns.barplot(x='revenue', y='movie_title', data=movie_totals)

# Display barplot
plt.show()