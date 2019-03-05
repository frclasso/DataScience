import pandas as pd


airquality = pd.read_csv('airquality.csv')

# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality.fillna(oz_mean)

# Print the info of airquality
print(airquality.info())
