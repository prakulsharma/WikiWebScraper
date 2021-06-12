#!/usr/bin/env python
# coding: utf-8

# # Wiki Web Scraper
# ---
# A simple and efficient wiki web scraper. The sole purpose of this project was to get a hands-on and to learn about web scraping and its usage. 

# ### Step 1. Importing requisite libraries

# In[1]:


import requests
from bs4 import BeautifulSoup
import re


# ### Step 2. Getting input from user

# In[2]:


print("Enter title to search")
title_input = input()

#input preprocessing
title_raw = ' '.join(title_input.split())
title_raw = title_raw.title()
title_final = title_raw.replace(" ","_")


# ### Step 3. Processing raw data from the website

# In[3]:


url = 'https://en.wikipedia.org/wiki/' + title_final
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('p', class_=None)

description_raw = []
for result in results:
    text = result.text
    description_raw.append(text)


# ### Step 4. Displaying output

# In[4]:


print(title_raw)
print("----------------------------")

error = 'Other reasons this message may be displayed'

for desc in description_raw:
    if error in desc:
        print("Either the input is wrong or this person is not famous at all, lol")
        break
    else:
        desc_final = re.sub("\[\w+\]","",desc)
        print(desc_final)

