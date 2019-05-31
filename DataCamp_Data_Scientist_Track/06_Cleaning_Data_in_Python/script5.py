# Import pandas
import pandas as pd
import matplotlib.pyplot as plt


# Read the file into a DataFrame: df
#df = pd.read_csv('dob_job_application_filings_subset.csv')
df = pd.read_csv('DOB_Job_Application_Filings_subset.csv')

#print(df['Initial Cost'])

# Create and display the first scatter plot
df.plot(kind='scatter', x='Initial Cost', y='total_est_fee', rot=70)
plt.show()

# Create and display the second scatter plot
# df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
# plt.show()