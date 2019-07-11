#!/usr/bin/env python3

import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')


# Control the number of bins
sns.distplot(df["sepal_length"], bins=20)
plt.show()
