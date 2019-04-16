# use this script to export sub sets of data for better handling
import pandas as pd
import json

df = pd.read_csv('global_dataset.csv', delimiter = ",", header=0)
# reduced_data = df.groupby(['yearOfRegistration', 'citizenship']).count()['case_id'].unstack()

# df2 = pd.read_csv('data/cases_per_citizenship.csv', delimiter = ",", header=0)
#
# df2.groupby(['yearOfRegistration'])
#
# df2 = df2.T
#
# df2.to_csv(r'transposed.csv')

genders = df.groupby(['yearOfRegistration', 'gender']).count()['case_id'].unstack()

genders.to_csv('gender_cases_per_year.csv')
