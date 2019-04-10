import pandas as pd
import json

df = pd.read_csv('global_dataset.csv', delimiter = ",", header=0)

to_export = df.groupby(['yearOfRegistration', 'gender']).count()['case_id'].unstack()

to_export.to_csv(r'data/yearsssssss.json', orient='records')
