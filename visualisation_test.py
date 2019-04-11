import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
# import requests

# from bokeh.io import output_notebook
# from bokeh.plotting import figure, show
# from bokeh.models import ColumnDataSource

df = pd.read_csv('global_dataset.csv', delimiter = ",", header=0, low_memory=False)

# total number of cases globally by gender
df.groupby('gender')['case_id'].nunique().plot(kind='bar')

# looking only at Female cases per year, globally
female_cases = df[df['gender'].str.startswith('Fem', na=False)]
female_cases.groupby('yearOfRegistration')['case_id'].nunique().plot(kind='bar')

plt.show()

# plotting male and female cases from 2002 to 2018
fig, ax = plt.subplots(figsize=(15,7))
# use unstack()
df.groupby(['yearOfRegistration','gender']).count()['case_id'].unstack().plot(ax=ax)
fig.suptitle('Human Trafficking Cases', fontsize=20)
ax.set_ylabel('Number of Cases')
ax.set_xlabel('Year of Registration')

plt.savefig('gender_cases.png')

# scatter plot of cases per country per year
df2 = pd.read_csv('data/cases_per_citizenship.csv', delimiter = ",", header=0)

ax1 = df2.plot(kind='scatter', x='yearOfRegistration', y='UA', color='r', s=0.5*df2.UA, label="Ukraine")    
ax2 = df2.plot(kind='scatter', x='yearOfRegistration', y='RO', color='g', s=0.5*df2.RO, label="Romania", ax=ax1)    
ax3 = df2.plot(kind='scatter', x='yearOfRegistration', y='ID', color='b', s=0.5*df2.ID, label='Indonesia', ax=ax1)
ax4 = df2.plot(kind='scatter', x='yearOfRegistration', y='BY', color='y', s=0.5*df2.BY, label='Belarus', ax=ax1)

