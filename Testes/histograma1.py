import pandas as pd
import matplotlib.pyplot as plt

data_url = 'http://bit.ly/2cLzoxH'
gapminder = pd.read_csv(data_url)
gapminder['lifeExp'].hist(bins=100)
plt.show()