# Import pandas
import pandas as pd
import matplotlib.pyplot

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')


# Describe the column
df['Existing Zoning Sqft'].describe()

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
matplotlib.pyplot.show()


