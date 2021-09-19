#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = pd.read_csv(r"C:\Users\Admin\Untitled Folder\earthquakes.csv")
a = pd.DataFrame(data)
#A.
len(a[(a['magType'] == 'ml') & (a['type'] == 'explosion')])
#B.
a[['distance','place', 'None']] = a['place'].str.split('of', expand = True)
a[['distance','direction','None','None', 'None']] = a['distance'].str.split(' ', expand = True)
a.drop(columns = ['None'])
data['distance'] = data['distance'].astype('str')
a = a.convert_dtypes()
np.mean(a['mag'][(a['place'].str.contains('Alaska', regex = True)) & (a['distance'].str.len() < len('100km'))])
#C.
a['time'] = pd.to_datetime(a['time'], unit="ms")
np.mean(a['mag'][(a['time'] < datetime(2018,3,1)) & (a['time'] > datetime(2018,1,1))])
np.mean(a['mag'][(a['time'] < datetime(2018,6,1)) & (a['time'] > datetime(2018,4,1))])
np.mean(a['mag'][(a['time'] < datetime(2018,9,1)) & (a['time'] > datetime(2018,7,1))])
np.mean(a['mag'][(a['time'] < datetime(2018,12,1)) & (a['time'] > datetime(2018,10,1))])


# In[53]:





# In[131]:





# In[ ]:




