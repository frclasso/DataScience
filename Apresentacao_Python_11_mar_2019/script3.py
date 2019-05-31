import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('g1800s.csv')

print(file.info())

file.plot(kind='scatter', x='1800', y='1899')
plt.xlabel('Life excpetance by country in 1800')
plt.ylabel('Life excpetance by country in 1899')

plt.show()