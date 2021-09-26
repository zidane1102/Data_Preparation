#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
data1 = pd.read_csv(r'C:\Users\Admin/data/aapl.csv')
data2 = pd.read_csv(r'C:\Users\Admin/data/amzn.csv')
data3 = pd.read_csv(r'C:\Users\Admin/data/fb.csv')
data4 = pd.read_csv(r'C:\Users\Admin/data/goog.csv')
data5 = pd.read_csv(r'C:\Users\Admin/data/nflx.csv')

a = pd.DataFrame(data1)
a['ticker'] = 'aapl'
b = pd.DataFrame(data2)
b['ticker'] = 'amzn'
c = pd.DataFrame(data3)
c['ticker'] = 'fb'
d = pd.DataFrame(data4)
d['ticker'] = 'goog'
e = pd.DataFrame(data5)
e['ticker'] = 'nflx'
f = pd.concat([a,b,c,d,e], axis = 0)
f.to_csv('faang.csv', sep='\t', encoding='utf-8')
f = f.assign(date = pd.to_datetime(f.date), volume = f.volume.astype('int'))
f.sort_values(by = ['date','ticker'], ascending = [True, True])
f.sort_values(by = ['volume'], ascending = True).head(7)

data6 = pd.read_csv(r'C:\Users\Admin/data/covid19_cases.csv')
g = pd.DataFrame(data6)
g['date'] = pd.to_datetime(g.dateRep)
g.set_index('date', inplace = True)
g.replace({"United_States_of_America": "USA", "United_Kingdom": "UK"}, inplace=True)

g.pivot(index='dateRep', columns='countriesAndTerritories', values='cases').fillna(0)


# In[ ]:




