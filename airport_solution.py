#!/usr/bin/env python
# coding: utf-8

# In[53]:


import json
import math

f = open("airlines.csv", "r")
dict = {}
hed = True
for x in f:
    if hed:
        hed = False
        continue
    temp = x.split('"')
    x = temp[1]
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] += 1
# print(dict)

answer_json = json.dumps(dict, sort_keys = True, indent = "")
print(answer_json)

max_airport = ""
max_count = 0
min_airport = ""
min_count = math.inf

for i in dict:
    if (dict[i] > max_count):
        max_airport = i
        max_count = dict[i]
    if (dict[i] < min_count):
        min_airport = i
        min_count = dict[i]

print(max_airport, max_count)
print(min_airport, min_count) 


# In[ ]:




