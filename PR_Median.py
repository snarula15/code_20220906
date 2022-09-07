import pandas as pd
from pandas.io.json import json_normalize
import json
from datetime import datetime
import numpy as np

#Read data from the PR API JSON#
df = pd.read_json('grafana_test.json')

#parse the json
pd.json_normalize(df)

# calc for how many days was the PR open
df['diff_days'] = (df['closed_at'] - df['created_at']) / np.timedelta64(1, 'D')

# calc Median on the above DF for comparison
df['Median_PR'] = df['diff_days'].median()
df
# df.info()

# Check the perf using the median by adding the PR_Performance column on the DF

df['PR_Performance'] = df.apply(lambda x: "Good" if x['diff_days'] <=
                     x['Median_PR'] else "Bad", axis=1)
df