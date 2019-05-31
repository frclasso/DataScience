import pandas as pd

# Import the ticket sales file
sales = pd.read_excel('ticket_sales.xlsx')

# Join the tables
sales_complete = ticket_type_sales.merge(ticket_prices,on='ticket_type', how='left')

# Add a revenue column and multiply tickets_sold x ticket_price
sales_complete['revenue'] = sales_complete['tickets_sold'] * sales_complete['ticket_price']

# Print the table
print(sales_complete)