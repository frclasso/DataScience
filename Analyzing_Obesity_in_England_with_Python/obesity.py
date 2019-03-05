#!/usr/bin/env python3
# -*-coding:utf-8-*-

import pandas as pd
import matplotlib.pyplot as plt

data = pd.ExcelFile("obes-phys-acti-diet-eng-2015-tab.xlsx")
print(data.sheet_names)


# Read 2nd section, by age
data_age = data.parse('7.2', skiprows=4, skipfooter=14)
print(data_age)

# Rename unamed to year
data_age.rename(columns={u'Unnamed: 0': u'Year'}, inplace=True)

# Drop empties
data_age.dropna(inplace=True)
data_age.set_index('Year', inplace=True)
print('After cleanup: ')
print(data_age)

# Plot
# data_age.plot()
#
# data_age_minus_total = data_age.drop('Total', axis=1)
# data_age_minus_total.plot()
# plt.show()


print('Done.')