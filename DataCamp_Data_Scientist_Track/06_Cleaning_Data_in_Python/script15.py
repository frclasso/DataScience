import pandas as pd
import re

tips = pd.read_csv('tips2.csv')

# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x))

# Print the head of tips
print(tips.head())
