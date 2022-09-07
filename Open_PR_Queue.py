import pandas as pd
from pandas.io.json import json_normalize
import json
from datetime import datetime
import numpy as np

#Read data from the PR API JSON#
df = pd.read_json('grafana_test.json')

#Parse the json
pd.json_normalize(df) 

#Filter open PRs
df=df[df['state'].isin(['open'])]

#Converting  datetime into date
df['created_at'] = pd.to_datetime(df['created_at']).dt.date
#print(df)
#df.groupby(['created_at', 'state']).size().reset_index(name='OpenCount')

#Create a new df1 with the newly added column OpenCount
df1 = df.groupby(['created_at', 'state']).size().reset_index(name='OpenCount')


#Plot the graph to see how many pull requests were open on particular date and if the queue grows or gets down over time
from matplotlib import pyplot as plt
import seaborn as sns
plt.bar(df1.created_at, df1.OpenCount, color ='blue',
        width = 0.3)
 
plt.xlabel("Dates")
plt.ylabel("No. of Open PR")
plt.title("Datewise Open PRs")
plt.show()