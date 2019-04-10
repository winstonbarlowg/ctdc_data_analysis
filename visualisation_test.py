import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import requests

# from bokeh.io import output_notebook
# from bokeh.plotting import figure, show
# from bokeh.models import ColumnDataSource

df = pd.read_csv('global_dataset.csv', delimiter = ",", header=0, low_memory=False)

# plotting male and female cases from 2002 to 2018
fig, ax = plt.subplots(figsize=(15,7))
# use unstack()
df.groupby(['yearOfRegistration','gender']).count()['case_id'].unstack().plot(ax=ax)
fig.suptitle('Human Trafficking Cases', fontsize=20)
ax.set_ylabel('Number of Cases')
ax.set_xlabel('Year of Registration')

plt.savefig('gender_cases.png')