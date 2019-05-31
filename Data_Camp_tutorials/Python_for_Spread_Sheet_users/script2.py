
import pandas as pd

# Import the ticket sales file
sales = pd.read_excel('ticket_sales.xlsx')

# print(sales.head())
# print(sales.iloc[:, 3])
# print(sales.info())
# print(sales.columns)


# Filter for Portland theaters
portland_sales = sales[sales['theater_location'] == "Portland"].reset_index(drop=True)

# Create sales_usd column
portland_sales['sales_usd'] = portland_sales['ticket_quantity'] * 20

# Sort by sales_usd descending
portland_sales = portland_sales.sort_values('sales_usd', ascending=False).reset_index(drop=True)

# Print the first row
print(portland_sales.head(1))
print()

print(sales.sum(numeric_only=True))