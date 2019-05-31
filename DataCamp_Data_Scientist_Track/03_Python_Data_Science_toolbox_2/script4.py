

import pandas as pd

df = pd.read_csv('tweets.csv' , index_col=0)

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
for t in tweet_clock_time:
    print(t)
