#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:34:10 2020

@author: Reaz
"""

import pandas as pd 
import os,re,sys 
from ast import literal_eval 

import cable_inspection as cip 


def nick_and_estimating():
    file_name='nick_and_estimating_data.xlsx'
    
    job_name_dict=cip.job_name_dict 
    
    df=pd.read_excel(file_name) 
    df=df.dropna() 
    job_number=[]  
    keys=list(job_name_dict.keys())
    values=list(job_name_dict.values())  
    columns=df.columns 
    for i in range (len(df)): 
        for j in range (len(values)):
            if list(df[columns[0]])[i]==values[j]: 
                job_number.append(keys[j]) 
    
    df['job_number']=job_number 
    df.index=df['job_number'] 
    


def assign_drawing_number(df):

    drawings_database=[]  
    L,FOC,TE=cip.main() 
    total=L+FOC+TE 
    for i in range (len(total)): 
        if total[i].drawing not in drawings_database: 
            drawings_database.append(total[i].drawing.strip(' ')) 
    
    
    
    accubid_drawings=[None]*len(df) 
    
    for i in range (len(drawings_database)):
        for j in range (len(df)):  
            
            if drawings_database[i] in str(df['Drawing'][j]):
                accubid_drawings[j]=drawings_database[i]  
               
    
    df['Drawing_No']=accubid_drawings  
    columns=df.columns
    rdf=pd.DataFrame(data=None,columns=['Drawing','Description','Length'])
    
    rdf_drawing=[] 
    rdf_conduit=[] 
    rdf_length=[]
    for i in range (len(df)): 
        if df['Drawing_No'][i]!=None: 
            rdf_drawing.append(df['Drawing_No'][i])   
            rdf_conduit.append(df['Description'][i]) 
            rdf_length.append(df['Quantity'][i]) 
    
    rdf['Drawing']=rdf_drawing 
    rdf['Description']=rdf_conduit 
    rdf['Length']=rdf_length  
    
    return rdf



### def identify the lines that has conduit in it #### 

def isolate_the_conduit_rows(rdf):

    rdf2=pd.DataFrame(data=None,columns=['Drawing','Description','Length'])
    rdf2_drawing=[] 
    rdf2_conduit=[] 
    rdf2_length=[] 
    
    
    
    for i in range (len(rdf)):   
            if 'CONDUIT' in rdf['Description'][i]:  
                #print (rdf['Description'][i])
                
                rdf2_drawing.append(rdf['Drawing'][i])   
                rdf2_conduit.append(rdf['Description'][i]) 
                rdf2_length.append(rdf['Length'][i])  
               
    rdf2['Drawing']=rdf2_drawing 
    rdf2['Description']=rdf2_conduit 
    rdf2['Length']=rdf2_length
    
    return rdf2  




def add_conduit_size(df): 
    conduit_hash={'3/4"':'0.75inch','1/2"':'0.5inch', 
           '1 1/2"':'1.5inch','1-1/2"':'1.5inch','2 1/2"':'2.5inch',
           '1"':'1inch','2-1/2"':'2.5inch','2"':'2inch',
           '3"':'3inch','4"':'4inch'}
           
    
    conduit_sizes=[] 
     
    for i in range (len(df)): 
        a=df.iloc[i]['Description'] 
        for i in range (len(a)):  
            start=0
            if a[i]=='"': 
                end=i 
                size=a[start:end].strip(' ')  
                size+='"'
                conduit_sizes.append(conduit_hash[size]) 
    
    df['Conduit_Size']=conduit_sizes
    
    return df 


def main():
    df=pd.read_excel('accubid_data.xlsx')  
    df=assign_drawing_number(df)   
    df=isolate_the_conduit_rows(df) 
    return df 

if __name__=="__main__": 
    main()
        


