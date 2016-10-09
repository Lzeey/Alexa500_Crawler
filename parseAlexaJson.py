# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:44:33 2016

@author: Zeyi
"""

import json
import pandas as pd

with open('alexaSG.json') as data_file:
    data = json.load(data_file)

fullList = []
for pageItems in data:
    pageList = pageItems['Name']
    fullList += pageList
    
pd.DataFrame(fullList).to_csv('alexaSG500.csv',header=False)