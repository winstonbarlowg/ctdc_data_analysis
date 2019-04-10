import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

df = pd.read_csv('global_dataset.csv', delimiter = ",", header=0, low_memory=False)

group = df.groupby(['yearOfRegistration', 'citizenship']).count()['case_id'].unstack()
source = ColumnDataSource(group)



