#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction"
r = requests.get(url)

#print(r)

soup = BeautifulSoup(r.text , "lxml")
table = soup.find("table" , class_ = "ih-td-tab auction-tbl")
#print(table)

header = table.find_all("tr",class_ = "ih-pt-tbl")
#print(header)


titles = []

for i in header:
    title = i.text
    titles.append(title)

#print(titles)


df = pd.DataFrame(columns = titles)
#print(df)

rows = table.find_all("tr")
for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    l = len(df)
    df.loc[l] = row


print(df)
df.to_csv("auction2024.csv")


# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


url = "https://www.iplt20.com/auction"
r = requests.get(url)


# In[3]:


print(r)


# In[4]:


soup = BeautifulSoup(r.text , "lxml")
table = soup.find("table" , class_ = "ih-td-tab auction-tbl")
print(table)


# In[6]:


header = table.find_all("tr",class_ = "ih-pt-tbl")
print(header)


# In[7]:


titles = []

for i in header:
    title = i.text
    titles.append(title)

print(titles)


# In[8]:


df = pd.DataFrame(columns = titles)
print(df)


# In[ ]:





# In[13]:





# In[20]:


print(f"Type of data: {type(data)}")
print(f"Contents of data: {data}")


# In[ ]:





# In[27]:


rows = table.find_all("tr")
for i in rows[1:]:
    try:
        first_td_element = i.find_all("td")[0].find("div", class_="ih-pt-ic")
        first_td = first_td_element.text.strip() if first_td_element else ""
    except IndexError:
        print(f"Warning: Row doesn't have expected structure: {i}")
        continue  # Skip this row and continue with the next

    data = i.find_all("td")[1:]
    print(f"Type of data: {type(data)}")
    print(f"Length of data: {len(data)}")
    print(f"First element of data: {data[0] if data else 'No data'}")
    
    row = [tr.text.strip() if hasattr(tr, 'text') else str(tr) for tr in data]
    row.insert(0, first_td)
    print(f"Extracted row: {row}")
    
    while len(row) < len(df.columns):
        row.append(None)
    
    l = len(df)
    df.loc[l] = row

print(df)


# In[24]:





# In[35]:


df_dropped = df.drop(index = range(0,20))
df_dropped


# In[36]:


df_dropped.to_csv("Auction_stats_2024.csv")


# In[ ]:




