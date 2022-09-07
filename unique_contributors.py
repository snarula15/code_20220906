import pandas as pd
from pandas.io.json import json_normalize
import json
from datetime import datetime
import numpy as np

#Read data from the PR API JSON#
df = pd.read_json('grafana_test.json')

#Converting  datetime into date
df['created_at'] = pd.to_datetime(df['created_at']).dt.date

# Creating a new DF to get the contributors
df1 = df[['number']].join(pd.json_normalize(df['user']))

#Merging the df with df1 and creating df2 & filter CONTRIBUTORS
df2 = df1.merge(df, how='inner', on= 'number')
df2=df2[df2['author_association'].isin(['CONTRIBUTOR'])]
#print(df)
df3= df2.groupby(['created_at']).size().reset_index(name='UniqueLogins')

#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    print(df3)


### Ploting the graph using pyplot to show the Unique Logins on a particular date   
    
from matplotlib import pyplot as plt
import seaborn as sns
plt.bar(df3.created_at, df3.UniqueLogins, color ='green',
        width = 0.4)
 
plt.xlabel("Dates")
plt.ylabel("No. of Unique contributors")
plt.title("Graph for Unique Contributors")
plt.show()
