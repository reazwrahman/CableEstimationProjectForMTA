#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:08:50 2020

@author: Reaz
"""

import accubid_dataframe as acd  
import pandas as pd 
from ast import literal_eval
   

class ACCUBID_CLASS(object): 
    
    def __init__(self,df,drawing_no): 
        
        self.df=df 
        self.drawing=drawing_no
        self.conduit_dict=self.generate_conduit_dict() 
        self.conduit_df=self.generate_conduit_df() 
        self.job_name=self.assign_drawing_with_job(self.drawing)
        
        
        
        
    def assign_drawing_with_job(self,drawing_no): 
        
        job_name_dict={100:'207TH STREET STATION', 
                       200:'34TH HERALD SQUARE STATION 6TH AVE (IND)', 
                       300:'34TH HERALD SQUARE STATION BROADWAY (BMT)', 
                       400:'FLATBUSH AVE STATION',  
                       500:'CHURCH AVE STATION', 
                       600:'JAMAICA CENTER PARSONS/ ARCHER STATION',	
                       700:'SUTPHIN BOULEVARD/ ARCHER AVE STATION'	
                       } 
        
        for i in range (len(drawing_no)): 
            if drawing_no[i]=='-': 
                start=i+1 
        
        
        mod_number=literal_eval(drawing_no[start:start+3]) 
        mod_number=(mod_number//100)*100  
        
        job_name=job_name_dict[mod_number] 
        
        return job_name
        
        
        
        
    def generate_conduit_dict(self):  
        
        df=self.df 
        drawing_no=self.drawing
        conduit_dict={}
        
        for i in range (len(df)):   
            if df['Drawing'][i]==drawing_no: 
                conduit_size=df['Conduit_Size'][i] 
                if conduit_size not in conduit_dict: 
                    conduit_dict[conduit_size]=df['Length'][i]           
                else:  
                    conduit_dict[conduit_size]+=df['Length'][i]     
            else: 
                pass
        
        return conduit_dict 
    
    
    
    def generate_conduit_df(self):  
        
        self.conduit_df=pd.DataFrame.from_dict(self.conduit_dict,orient='index',columns=['total length(ft.)']) 
        return self.conduit_df
        
                

def main():        
    df=acd.main() 
    total=[]
    
    ##create a drawing no list
    drawing_numbers=[]   
    for i in range (len(df)): 
        if df['Drawing'][i] not in drawing_numbers: 
            drawing_numbers.append(df['Drawing'][i])  
    
    for i in range (len(drawing_numbers)): 
        a=ACCUBID_CLASS(df,drawing_numbers[i])   
        total.append(a)
          
    
    return total  

if __name__=="__main__": 
    main()
            
