#!/usr/bin/env python
# coding: utf-8

# In[76]:


import pandas as pd
data1 = pd.read_csv(r'C:\Users\Admin\data\weather_stations.csv')
data2 = pd.read_csv(r'C:\Users\Admin\data\nyc_weather_2018.csv')
a = pd.DataFrame(data1)
b = pd.DataFrame(data2)
c = pd.merge(a, b, how = 'inner', left_on = 'id', right_on = 'station')
c.drop_duplicates(subset = ['datatype', 'station'])['elevation'][(c['datatype'] == "SNOW") & (c['name'].str.contains('NJ US'))].mean()


# In[97]:


import pandas as pd
data1 = pd.read_csv(r'C:\Users\Admin\data\fb_2018.csv')
a = pd.DataFrame(data1)
a = a.assign(pct_change = a['volume'].pct_change()).fillna(0)
a.sort_values(by = 'pct_change', ascending = False).head(5)


# In[26]:


import pandas as pd
data1 = pd.read_csv(r'C:\Users\Admin\data\earthquakes.csv')
a = pd.DataFrame(data1)
bins = pd.interval_range(start=0, end=5)
bined = pd.cut(a.mag[a['magType'] == 'ml'], bins)
bined.value_counts()


# In[134]:


import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date
data1 = pd.read_csv(r'C:\Users\Admin\data\weather_by_station.csv')
a = pd.DataFrame(data1)
a['date'] = pd.to_datetime(a['date'])
a['month'] = a['date'].dt.month
pd.crosstab(index = a['station'], columns = a['month'][a['datatype'] == 'SNOW'],
           colnames = ['month'], values = a['value'], aggfunc = np.mean)
pd.crosstab(index = a['station'], columns = a['month'][a['datatype'] == 'SNOW'],
           colnames = ['month'], values = a['datatype'], aggfunc = np.sum)


# In[ ]:




