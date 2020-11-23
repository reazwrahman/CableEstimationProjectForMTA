#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:16:44 2020

@author: Reaz
""" 

from ast import literal_eval 
import pandas as pd

data_file="original.xlsx"   
        
df=pd.read_excel(data_file) 
raw_dict=df.to_dict(orient='list') 

drawing_no=raw_dict['Drawing No.'] 
cable_dict_str=raw_dict['Cable Dictionary']  

cable_dict=[]
for i in range (len(cable_dict_str)): 
    cable_dict.append(literal_eval(cable_dict_str[i]))

for i in range (len(cable_dict)):  
    try: 
        print (cable_dict[i]['length(ft)']) 
    except: 
        cable_dict[i]['length(ft)']=0

cable_column=[] 
for i in range (len(cable_dict)): 
    cable_column.append(str(cable_dict[i])) 

df_new=pd.DataFrame(cable_column)
df_new.to_excel("local_automation_output.xlsx",sheet_name="Sheet1")





