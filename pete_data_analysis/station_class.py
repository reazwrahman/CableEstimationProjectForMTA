#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 17:53:38 2020

@author: Reaz
"""

import pandas as pd 
import os,re,sys

import cable_inspection as cip   
import accubid_class as acc 
import accubid_dataframe as acd


class ACCUBID_STATION(object): 
    
    def __init__(self,job_number): 
        
        self.total=acc.main() 
        self.job_number=job_number 
        
        self.job_dict={100:'207TH STREET STATION', 
                       200:'34TH HERALD SQUARE STATION 6TH AVE (IND)', 
                       300:'34TH HERALD SQUARE STATION BROADWAY (BMT)', 
                       400:'FLATBUSH AVE STATION',  
                       500:'CHURCH AVE STATION', 
                       600:'JAMAICA CENTER PARSONS/ ARCHER STATION',	
                       700:'SUTPHIN BOULEVARD/ ARCHER AVE STATION'	
                       } 
        self.drawings=self.collect_drawings()
        self.classes=self.collect_classes()  
        self.conduit_dict=self.generate_conduit_dict() 
        self.conduit_df=self.generate_conduit_df() 
        
        
        
#############------------METHODS----------------#######################        
        
    def collect_drawings(self):  
        
        target_job=self.job_dict[self.job_number]  
        drawings=[]
        
        for i in range (len(self.total)): 
            if self.total[i].job_name==target_job: 
                drawings.append(self.total[i].drawing) 
        
        return drawings  
    
    
    def collect_classes(self): 
        
        target_job=self.job_dict[self.job_number]  
        classes=[]
        
        for i in range (len(self.total)): 
            if self.total[i].job_name==target_job: 
                classes.append(self.total[i]) 
        
        return classes 
    
    
    
    def generate_conduit_dict(self):  
        
        global_keys=[]  
        a=self.classes  
        
        ### step 1: collect all the different conduit sizes 
        ### and put them in the global_keys list
        
        
        for i in range (len(a)):  
            local_keys=list(a[i].conduit_dict.keys()) 
            for j in range (len(local_keys)): 
                if local_keys[j] not in global_keys: 
                    global_keys.append(local_keys[j])  
        
        
        self.conduit_sizes=global_keys 
        ### step 2: create a dictionary called global dict 
        ### using the keys from global keys and set all 
        ### values to zero 
        
        global_dict={} 
        for i in range (len(global_keys)):   
            global_dict[global_keys[i]]=0 
            
        
        ### step 3: read the length value from the classes 
        ### and increment in the global dict 
        
        for each in global_keys: 
            for i in range (len(a)): 
                if each in a[i].conduit_dict: 
                    length=a[i].conduit_dict[each]  
                    global_dict[each]+=length 
                    
        
        
        return global_dict 
    
    
    def generate_conduit_df(self): 
        
        self.conduit_df=pd.DataFrame.from_dict(self.conduit_dict,orient='index',columns=['total length(ft.)']) 
        return self.conduit_df


class MY_STATION(object): 
    
    def __init__(self,job_number): 
        
        L,FOC,TE=cip.main()  
        self.total=L+FOC+TE  
        
        self.job_number=job_number 
        
        
        self.job_dict={100:'207TH STREET STATION', 
                       200:'34TH HERALD SQUARE STATION 6TH AVE (IND)', 
                       300:'34TH HERALD SQUARE STATION BROADWAY (BMT)', 
                       400:'FLATBUSH AVE STATION',  
                       500:'CHURCH AVE STATION', 
                       600:'JAMAICA CENTER PARSONS/ ARCHER STATION',	
                       700:'SUTPHIN BOULEVARD/ ARCHER AVE STATION'	
                       } 
        
        self.drawings=self.collect_drawings() 
        self.classes=self.collect_classes() 
        
        ### read job_name from the job_dict dictionary ###
        self.job_name=self.job_dict[self.job_number] 
        
        self.conduit_dict=self.generate_conduit_dict() 
        self.cable_types_dict=self.generate_cable_types_dict()
        
        
        self.conduit_df=self.generate_conduit_df() 
        self.cable_types_df=self.generate_cable_types_df() 
        
        
####-----------------------METHODS----------------------------################        
    
    def collect_drawings(self):  
        
        target_job=self.job_dict[self.job_number]  
        drawings=[]
        
        for i in range (len(self.total)): 
            if self.total[i].job_name==target_job: 
                drawings.append(self.total[i].drawing) 
        
        return drawings 
    
    
    def collect_classes(self): 
        
        target_job=self.job_dict[self.job_number]  
        classes=[]
        
        for i in range (len(self.total)): 
            if self.total[i].job_name==target_job: 
                classes.append(self.total[i]) 
        
        return classes 
    
    
    def generate_conduit_dict(self):  
        
        global_keys=[]  
        a=self.classes  
        
        ### step 1: collect all the different conduit sizes 
        ### and put them in the global_keys list
        
        
        for i in range (len(a)):  
            local_keys=list(a[i].conduit_dict.keys()) 
            for j in range (len(local_keys)): 
                if local_keys[j] not in global_keys: 
                    global_keys.append(local_keys[j])  
        
        
        self.conduit_sizes=global_keys 
        ### step 2: create a dictionary called global dict 
        ### using the keys from global keys and set all 
        ### values to zero 
        
        global_dict={} 
        for i in range (len(global_keys)):   
            global_dict[global_keys[i]]=0 
            
        
        ### step 3: read the length value from the classes 
        ### and increment in the global dict 
        
        for each in global_keys: 
            for i in range (len(a)): 
                if each in a[i].conduit_dict: 
                    length=a[i].conduit_dict[each][1]  
                    global_dict[each]+=length 
                    
        
        
        return global_dict
    
    
   
    def generate_cable_types_dict(self):  
            
            global_keys=[]  
            a=self.classes  
          
            ## follow the explanation from the  
            ### generate_conduit_method above
            
            for i in range (len(a)):  
                local_keys=list(a[i].cable_types_dict.keys()) 
                for j in range (len(local_keys)): 
                    if local_keys[j] not in global_keys: 
                        global_keys.append(local_keys[j])  
            
            
            ### populate possible cable types
            self.cable_types=global_keys 
            ###------------------------
            
            global_dict={} 
            for i in range (len(global_keys)):   
                global_dict[global_keys[i]]=0 
                
           
            for each in global_keys: 
                for i in range (len(a)): 
                    if each in a[i].cable_types_dict: 
                        length=a[i].cable_types_dict[each][1]  
                        global_dict[each]+=length 
                        
            
            
            return global_dict         
        
        
        
        
    def generate_conduit_df(self): 
        
        self.conduit_df=pd.DataFrame.from_dict(self.conduit_dict,orient='index',columns=['total length(ft.)']) 
        return self.conduit_df
        
    
    def generate_cable_types_df(self): 
            
        self.cable_types_df=pd.DataFrame.from_dict(self.cable_types_dict,orient='index',columns=['total length(ft.)']) 
        return self.cable_types_df

###############-------------------------------------------##############
        #################################################
###############-------------------------------------------##############
  
    
    ####----'NICK' ------------------        

class NICK_STATION(object): 
    
    def __init__(self,job_number): 
        
        self.job_dict={100:'207TH STREET STATION', 
                       200:'34TH HERALD SQUARE STATION 6TH AVE (IND)', 
                       300:'34TH HERALD SQUARE STATION BROADWAY (BMT)', 
                       400:'FLATBUSH AVE STATION',  
                       500:'CHURCH AVE STATION', 
                       600:'JAMAICA CENTER PARSONS/ ARCHER STATION',	
                       700:'SUTPHIN BOULEVARD/ ARCHER AVE STATION'	
                       }  
        
        
        self.source=acd.nick_and_estimating()
        self.job_number=job_number 
        self.conduit_dict=self.generate_conduit_dict() 
        
        
        
        
    def generate_conduit_dict(self): 
        
        df=self.source 
        conduit_dict={}
        for i  in range (len(df)): 
            if df['job_number'][i]==self.job_number: 
                conduit_dict[df['Conduit Size'][i]]=df['NICHOLAS'][i]
            else: 
                pass   
        
        return conduit_dict 
    
    def generate_conduit_df(self): 
        
        self.conduit_df=pd.DataFrame.from_dict(self.conduit_dict,orient='index',columns=['total length(ft.)']) 
        return self.conduit_df
                
        
        
####----'PETE' ------------------        
class PETE_STATION(object): 
    
    def __init__(self,job_number): 
        
        self.job_dict={100:'207TH STREET STATION', 
                       200:'34TH HERALD SQUARE STATION 6TH AVE (IND)', 
                       300:'34TH HERALD SQUARE STATION BROADWAY (BMT)', 
                       400:'FLATBUSH AVE STATION',  
                       500:'CHURCH AVE STATION', 
                       600:'JAMAICA CENTER PARSONS/ ARCHER STATION',	
                       700:'SUTPHIN BOULEVARD/ ARCHER AVE STATION'	
                       } 
        
        
        self.sheet_schema={100:0,200:1,300:2,400:3,500:4,600:5,700:6}
        
        
        self.job_number=job_number 
        self.filename='pete_all_mytake.xlsx' 
        self.sheet=self.sheet_schema[self.job_number] 
        
        self.conduit_dict=self.generate_pete_dict()[0] 
        self.conduit_by_drawing=self.generate_pete_dict()[1]
        

    def generate_pete_dict(self):  
        
        df=pd.read_excel(self.filename,sheet_name=self.sheet) 
        columns=df.columns
        sizes=df[columns[2]] 
        length=df[columns[3]] 
        drawings=df[columns[0]]    
        
        conduit_dict={}
        for i in range (len(sizes)):  
            if sizes[i] not in conduit_dict: 
                conduit_dict[sizes[i]]=length[i] 
            else: 
                conduit_dict[sizes[i]]+=length[i]  
        
        drawing_dict={}  
        for i in range (len(sizes)): 
            if sizes[i] not in drawing_dict:  
                drawing_dict[sizes[i]]=[drawings[i]] 
            else:  
                if drawings[i] not in drawing_dict[sizes[i]]:
                    drawing_dict[sizes[i]].append(drawings[i]) 
        
        
        return [conduit_dict,drawing_dict] 



def test(): 
    
    a=MY_STATION(200) 
    #print (a.conduit_df) 
    #print (a.cable_types_df)  
    pete_object=PETE_STATION(600) 
    pete_conduit=pete_object.conduit_dict 
    print (pete_conduit)
    
if __name__=="__main__": 
    test()    