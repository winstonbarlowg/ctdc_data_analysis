import pandas as pd
import json

df = pd.read_csv('global_dataset.csv', delimiter = ",", header=0)

reduced_data = df.groupby(['yearOfRegistration', 'citizenship']).count()['case_id'].unstack()
reduced_data.to_csv(r'data\countries.csv')