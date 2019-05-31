import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_url = 'http://bit.ly/2cLzoxH'

gapminder = pd.read_csv(data_url)
gapminder.head(n=3)

df = gapminder[gapminder.continent == "Africa"]
sns.distplot(df['lifeExp'], kde=False, label='Africa')

df = gapminder[gapminder.continent == "America"]
sns.distplot(df['lifeExp'], kde=False, label='America')


plt.legend(prop={'size':12})
plt.title('Expectativa de vida em dois continentes')
plt.xlabel('Expectiva de vida(anos')
plt.ylabel('Densidade')

plt.show()