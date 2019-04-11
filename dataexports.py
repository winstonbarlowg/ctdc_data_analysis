import pandas as pd
import json

# df = pd.read_csv('global_dataset.csv', delimiter = ",", header=0)

# reduced_data = df.groupby(['yearOfRegistration', 'citizenship']).count()['case_id'].unstack()
df2 = pd.read_csv('data/cases_per_citizenship.csv', delimiter = ",", header=0)

df2.groupby(['yearOfRegistration'])

df2 = df2.T

df2.to_csv(r'transposed.csv')