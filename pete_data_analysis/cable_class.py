#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:28:13 2020

@author: Reaz
"""

import pandas as pd 
from ast import literal_eval  
import os,re,sys





class CABLE(object): 
    
    def __init__(self,input_dict,drawing_no=None): 
        
        self.cable_dict=input_dict
        
        self.conduit_sizes=[] 
        self.cable_types=[] 
        self.conduit_dict={} 
        self.cable_types_dict={} 
        
        self.conduit_df=None
        self.cable_types_df=None 
        
        self.drawing=drawing_no 
        self.job_name=None
    
    
    
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
        
    
    def create_conduit_combinations(self):  
        
        conduit_sizes=[]  
        
        for i in range (len(self.cable_dict)): 
            if self.cable_dict[i]['material']=='conduit':  
                if self.cable_dict[i]['type'] not in conduit_sizes:
                    conduit_sizes.append(self.cable_dict[i]['type']) 
                    
        self.conduit_sizes=conduit_sizes
                    
        #print (f' possible conduit sizes are: {conduit_sizes}') 
        #print ('\n')
        
        return self.conduit_sizes
    
    
    
    def create_cable_combinations(self):  
        

        cable_types=[]
        
        for i in range (len(self.cable_dict)): 
            if self.cable_dict[i]['material']=='cable':  
                if self.cable_dict[i]['type'] not in cable_types:
                    cable_types.append(self.cable_dict[i]['type']) 
        
        self.cable_types=cable_types
        
        #print (f' possible cable types are: {cable_types}')  
        #print ('\n')
        return self.cable_types
    
    
    
    
    
    def create_conduit_dictionary(self): 

        if len(self.conduit_sizes)==0: 
            self.create_conduit_combinations() 
        
        conduit_dict={} 
        
        #### for counting total QUANTITY ###########
        for size in self.conduit_sizes:   
            counter=0
            conduit_dict[size]=[None,None] 
            for i in range (len(self.cable_dict)): 
                if (self.cable_dict[i]['material']=='conduit') and (self.cable_dict[i]['type']==size): 
                    counter+=self.cable_dict[i]['quantity'] 
            conduit_dict[size][0]=counter
        
        
        #### for counting total LENGTH ###########

        for size in self.conduit_sizes:   
            total_length=0
            for i in range (len(self.cable_dict)): 
                if (self.cable_dict[i]['material']=='conduit') and (self.cable_dict[i]['type']==size): 
                    #total_length+=self.cable_dict[i]['length(ft)']*self.cable_dict[i]['quantity'] 
                    total_length+=self.cable_dict[i]['length(ft)']
            conduit_dict[size][1]=total_length 
        
        
        
        #print (f'Conduit Quantity by size breakdown: {conduit_dict}')   
        #print ('\n')
        self.conduit_dict=conduit_dict
        
        return self.conduit_dict
    
    
    def create_cable_types_dictionary(self):  
        
   
        if len(self.cable_types)==0: 
            self.create_cable_combinations()
        
        cable_types_dict={} 
        
        #### for measuring total QUANTITY ######
        for size in self.cable_types:   
            counter=0
            cable_types_dict[size]=[None,None]
            for i in range (len(self.cable_dict)): 
                if (self.cable_dict[i]['material']=='cable') and (self.cable_dict[i]['type']==size): 
                    counter+=self.cable_dict[i]['quantity']  
            
            cable_types_dict[size][0]=counter
        
        
        
        #### for measuring total LENGTH ######
        for size in self.cable_types:   
            total_length=0
            for i in range (len(self.cable_dict)): 
                if (self.cable_dict[i]['material']=='cable') and (self.cable_dict[i]['type']==size): 
                    total_length+=self.cable_dict[i]['length(ft)']*self.cable_dict[i]['quantity']  
            cable_types_dict[size][1]=total_length
        
        
        #print (f'Cable Type Quantity by size breakdown: {cable_types_dict}')    
        #print ('\n')
        self.cable_types_dict=cable_types_dict
        
        return self.cable_types_dict


    
    def create_conduit_df(self): 
        
        
        if len(self.conduit_dict)==0: 
            self.create_conduit_dictionary() 
            
        self.conduit_df=pd.DataFrame.from_dict(self.conduit_dict,orient='index',columns=['Quantity','total length(ft.)']) 
    
        #print (f'CONDUIT{self.conduit_df}')  
        #print ('\n')
        
    
    def create_cable_types_df(self): 
    
        if len(self.cable_types_dict)==0: 
            self.create_cable_types_dictionary() 
            
        self.cable_types_df=pd.DataFrame.from_dict(self.cable_types_dict,orient='index',columns=['Quantity','total Length(ft.)']) 
    
        #print (f'CABLE{self.cable_types_df}') 
        #print ('\n')
    
    def central(self):  
        
        self.job_name=self.assign_drawing_with_job(self.drawing) 
        
        #print (f'DRAWING NO: {self.drawing}') 
        #print (self.job_name)
        self.create_conduit_df() 
        self.create_cable_types_df() 
        