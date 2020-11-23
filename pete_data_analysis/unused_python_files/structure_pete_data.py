#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:18:00 2020

@author: Reaz
"""

import pandas as pd 
import os,re,sys 
from ast import literal_eval


df=pd.read_excel('pete_200.xlsx')  
df=df.dropna()
columns=df.columns 
conduits=list(df[columns[1]]) 
refined=[] 


for i in range (len(conduits)):  
    if ('CONDUIT' not in conduits[i]) and ('PRINT' not in conduits[i]) and ('L-' not in conduits[i]): 
        refined.append(conduits[i]) 

#for i in range (len(conduits)): 
#    if ('"' in conduits[i]) or ('FT' in conduits[i]): 
#        refined.append(conduits[i])






pkeys=[] 
pval=[] 
rdict={}  
rejects=[]
for i in range (len(refined)):   
    if '-' in refined[i]: 
        #print (refined[i])
        for j in range (len(refined[i])): 
            if refined[i][j]=='-':  
                dash=j 
                if refined[i][:dash] not in rdict:  
                    rdict[refined[i][:dash]]=refined[i][dash+1:] 
                elif refined[i][:dash] in rdict: 
                    rdict[refined[i][:dash]]+=f'+{refined[i][dash+1:]}' 
                
    else: 
        rejects.append(refined[i])
            
                    
    
                