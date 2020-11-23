#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:14:06 2020

@author: Reaz
""" 

import os,re,sys 
import pandas as pd 

from cable_inspection import job_name_dict
from station_class import MY_STATION  
from station_class import PETE_STATION  
from station_class import ACCUBID_STATION
from station_class import NICK_STATION

from graph_classes import bar_graph 
from docx_class import DOCX



class COMPARISON(object): 
    
    def __init__(self,job_number): 
        
        self.job_number=job_number 
        self.job_name=job_name_dict[job_number]
        
        self.my_object=MY_STATION(self.job_number)
        self.my_conduit=self.my_object.conduit_dict   
        
        self.pete_object=PETE_STATION(self.job_number) 
        self.pete_conduit=self.pete_object.conduit_dict 
        
        self.accubid_object=ACCUBID_STATION(self.job_number) 
        self.accubid_conduit=self.accubid_object.conduit_dict
     
        self.nick_object=NICK_STATION(self.job_number)
        self.nick_conduit=self.nick_object.conduit_dict
    
        self.labels=self.labels_generator()
        
        self.my_length=self.lengths_generator()[0] 
        self.pete_length=self.lengths_generator()[1]  
        self.accubid_length=self.lengths_generator()[2]  
        self.nick_length=self.lengths_generator()[3]  
        
        
        
    
        self.combined_dict=self.generate_combined_conduit() 
        self.combined_df=self.generate_df()
    

    def labels_generator(self): 
        
        labels=list(self.my_conduit.keys()) 
        
        p_keys=list(self.pete_conduit.keys())
        for i in range (len(p_keys)): 
            if p_keys[i] not in labels: 
                labels.append(p_keys[i])   
        
        ac_keys=list(self.accubid_conduit.keys())
        for i in range (len(ac_keys)): 
            if ac_keys[i] not in labels: 
                labels.append(ac_keys[i])  
        
        nick_keys=list(self.nick_conduit.keys())
        for i in range (len(nick_keys)): 
            if nick_keys[i] not in labels: 
                labels.append(nick_keys[i])  
             
        
        return labels
                
    
    def lengths_generator(self):  
        
        labels=self.labels 
        my_dict=self.my_conduit 
        pete_dict=self.pete_conduit  
        accubid_dict=self.accubid_conduit 
        nick_dict=self.nick_conduit
        
        my_length=[] 
        pete_length=[]  
        accubid_length=[] 
        nick_length=[]
        
        for x in labels: 
            if x in my_dict: 
                my_length.append(my_dict[x])  
            else: 
                my_length.append(0) 
                    
            if x in pete_dict: 
                pete_length.append(pete_dict[x])  
            else: 
                pete_length.append(0)  
             
            if x in accubid_dict: 
                accubid_length.append(accubid_dict[x])  
            else: 
                accubid_length.append(0) 
               
            if x in nick_dict: 
                nick_length.append(nick_dict[x])  
            else: 
                nick_length.append(0)
            
        
        return [my_length,pete_length,accubid_length,nick_length]
        
    
    def bargraph(self):
        
        bg=bar_graph(self.labels,self.my_length,self.pete_length,ylabel='Total Length (FT.)',data1name='Reaz',data2name='Pete',title=f'Conduit Estimate: {job_name_dict[self.job_number]}',label_columns='yes',suppress_plot="yes")
        handle=bg.plot() 
        return handle

    def generate_combined_conduit(self): 
        
        combined_conduit={}   
        labels=self.labels 
        my_dict=self.my_conduit 
        pete_dict=self.pete_conduit 
        accubid_dict=self.accubid_conduit 
        nick_dict=self.nick_conduit
        
        for i in range (len(labels)): 
            combined_conduit[labels[i]]=[None,None,None,None]
        
        for i in range (len(labels)):   
            key=labels[i]
            if key in my_dict: 
                combined_conduit[key][0]=my_dict[key] 
            else: 
                combined_conduit[key][0]=0 
            
            if key in pete_dict: 
                combined_conduit[key][1]=pete_dict[key] 
            else: 
                combined_conduit[key][1]=0  
            
            if key in accubid_dict: 
                combined_conduit[key][2]=accubid_dict[key] 
            else: 
                combined_conduit[key][2]=0 
            
            if key in nick_dict: 
                combined_conduit[key][3]=nick_dict[key] 
            else: 
                combined_conduit[key][3]=0
            
    
        return combined_conduit 
    
    def generate_df(self): 
        
        df=pd.DataFrame.from_dict(self.combined_dict,orient='index',columns=['Reaz (ft)','Pete (ft)','Accubid(ft.)','Nick(ft)']) 
        
        columns=df.columns  
        df['Avg']=(df[columns[0]]+df[columns[1]]+df[columns[2]])/3 
        df['Delta(RZ-AC)']=df[columns[0]]-df[columns[2]]
        
        df['Station']=self.job_name 
        df['Conduit Size']=df.index 
        df.index=df['Station'] 
        #df=df[['Conduit Size','Reaz (ft)','Accubid(ft.)','Pete (ft)','Avg']]
        df=df[['Conduit Size','Reaz (ft)','Accubid(ft.)','Pete (ft)','Nick(ft)','Avg','Delta(RZ-AC)']]    
    
        return df


def main():  
    
    document=DOCX(filename='comparative_data_analysis.docx',heading='Comparisons shown below - Reaz Rahman - 6/26/2020') 
    central_df=[]
    
    job_list=list(job_name_dict.keys())
    for job_number in job_list:
        a=COMPARISON(job_number)   
        
        ######-------- to print out all drawings relative to each station -------------###
        #print (job_name_dict[job_number])
        #print (a.my_object.drawings)
        ######-------- to print out all drawings relative to each station -------------###


        ### -----populate the dataframe with all the stations data -----###
        if len(central_df)==0: 
            central_df=a.combined_df 
        else: 
            central_df=central_df.append(a.combined_df)  
        
        print (a.combined_df)
        ###----- populate the dataframe with all the stations data -----###
        
        
        ## get the plot figure and put it in a .docx ###
        #handle=a.bargraph()  
        #document.write_graph(handle,graph_name=job_name_dict[job_number]) 
        #document.write_text(a.combined_df.to_string())
        #document.add_page_break() 
    
    central_df.to_excel("comparative_data_7stations.xlsx",sheet_name="Conduit")
    #print (central_df)
    return central_df
    
if __name__=="__main__": 
    main()  
    
    