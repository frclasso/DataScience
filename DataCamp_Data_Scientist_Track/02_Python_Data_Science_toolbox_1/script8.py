#!/usr/bin/env python3


import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets_like_Trump.csv', index_col=0)

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x:x[0:2] =='RT' , tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)