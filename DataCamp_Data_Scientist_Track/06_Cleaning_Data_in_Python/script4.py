# Import pandas
import pandas as pd
import matplotlib.pyplot as plt


# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')


# Create the boxplot
df.boxplot(column='Initial Cost', by='Borough', rot=90)

# Display the plot
plt.show()
