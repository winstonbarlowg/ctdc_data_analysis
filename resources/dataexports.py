# use this script to export sub sets of data for better handling
import pandas as pd
import json
import country_converter as coco

df = pd.read_csv('global_dataset.csv', delimiter = ",", header=0)
# df2 = pd.read_csv('data/cases_per_citizenship.csv', delimiter = ",", header=0)
# df2.groupby(['yearOfRegistration'])
# df2 = df2.T
# df2.to_csv(r'transposed.csv')

# subset with year, type of exploit, and case ID
exploit_type2 = df[['yearOfRegistration', 'typeOfExploitConcatenated', 'case_id']]

genders = df.groupby(['yearOfRegistration', 'gender']).count()['case_id'].unstack()

# genders.to_csv('gender_cases_per_year.csv')

# export CSV with type of exploitation of female cases
exploit_type = df[['typeOfExploitConcatenated', 'gender']]
female_cases = exploit_type[ exploit_type[ 'gender'].str.startswith('Fem', na=False)]
export = female_cases.groupby(['typeOfExploitConcatenated']).count()

# export.to_csv('female_typeOfExploit.csv')

# COUNTRY RELATIONSHIPS ORIGIN-EXPLOIT (subsets)
country_relation = df[['case_id', 'gender', 'citizenship', 'CountryOfExploitation']]
# subsets by gender
fem_rel = country_relation[country_relation['gender'].str.startswith('Fem', na=False)]
mal_rel = country_relation[country_relation['gender'].str.startswith('Mal', na=False)]

# DATA FOR BAR CHARTS
#group female cases
group_fem_citi = fem_rel.groupby('citizenship')['case_id'].nunique().reset_index()
group_fem_expl = fem_rel.groupby('CountryOfExploitation')['case_id'].nunique().reset_index()

# group male cases
group_mal_citi = mal_rel.groupby('citizenship')['case_id'].nunique().reset_index()
group_mal_expl = mal_rel.groupby('CountryOfExploitation')['case_id'].nunique().reset_index()

# creating a list with e.g. only the countries
countries_fem_citi = group_fem_citi['citizenship'].values.tolist()

# match the ISO2 country code to the Country name, print list
full_countries_fem_citi = coco.convert(names=countries_fem_citi, to='name_short')
# print(full_countries_fem_citi)

# ALL COUNTRY RELATIONSHIPS FOR ALL CASES
all_origin = country_relation.groupby('citizenship')['case_id'].nunique().reset_index()
all_exploit = country_relation.groupby('CountryOfExploitation')['case_id'].nunique().reset_index()

list_all_origin = all_origin['citizenship'].values.tolist() # use coco.convert
list_all_origin_values = all_origin['case_id'].values.tolist()

list_all_exploit = all_exploit['CountryOfExploitation'].values.tolist() # use coco.convert
list_all_exploit_values = all_exploit['case_id'].values.tolist()

# CREATE AGE CLUSTERS
age_subset = df[['ageBroad','case_id']]
age_cluster = age_subset.groupby('ageBroad')['case_id'].nunique().reset_index()
age_sets = age_cluster['ageBroad'].values.tolist()
age_values = age_cluster['case_id'].values.tolist()

# RECRUITMENT RELATIONSHIP
recruitment = df[['RecruiterRelationship', 'case_id']]
recruitment_sub = recruitment.groupby('RecruiterRelationship')['case_id'].nunique().reset_index()

recr = df[['recruiterRelationIntimatePartner','recruiterRelationFriend','recruiterRelationFamily','recruiterRelationOther',
'case_id', 'typeOfExploitConcatenated']]
rec_sex = recr[recr['typeOfExploitConcatenated'].str.startswith('Sexual', na=False)]
rec_lab = recr[recr['typeOfExploitConcatenated'].str.startswith('Labour', na=False)]

rec_sex_data = rec_sex.groupby(['typeOfExploitConcatenated'])['recruiterRelationIntimatePartner'].count()
