#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 09:06:45 2020

@author: Reaz
"""

import pandas as pd 
from ast import literal_eval  
import sys,re,os

from cable_class import CABLE



def create_raw_cable_dict(datafile):  
    
        
        df=pd.read_excel(datafile)
        raw_dict=df.to_dict(orient='list') 
        
        drawing_no=raw_dict['Drawing No.'] 
        cable_dict_str=raw_dict['Cable Dictionary'] 
        cable_dict=[] 
        for i in range (len(cable_dict_str)):  
            try:
                cable_dict.append(literal_eval(cable_dict_str[i]))   
            except:
                #for troubleshooting in data entry  
                print ('warning! Something went wrong')  
                print (f'CHECK {datafile} line no {i+2}')
                sys.exit() 
        
        
        for i in range(len(cable_dict)): 
            cable_dict[i]['Drawing No.']=drawing_no[i] 
        
        drawings=[] 
        for i in range (len(drawing_no)): 
            if drawing_no[i] not in drawings: 
                drawings.append(drawing_no[i])
            
  
        return cable_dict,drawings



def dict_by_drawing(drawing_no,output_file,data_file):   
    
    
#    print ('######################') 
#    print (f'Cable/Conduit Breakdown shown below for {drawing_no} ') 
#    print ('######################')  
#    print ('\n') 
    
    appender(output_file,'\n') 
    appender(output_file,'\n')
    appender(output_file,'######################')  
    appender(output_file,'\n')         
    appender(output_file,f'Cable/Conduit Breakdown shown below for {drawing_no} ') 
    appender(output_file,'\n')
                 
    
    
    
    full_dict,all_drawings=create_raw_cable_dict(data_file) 
    focused_dict=[] 
    for i in range (len(full_dict)): 
        if full_dict[i]['Drawing No.']==drawing_no: 
            focused_dict.append(full_dict[i]) 
    
    return focused_dict



def writer (filename,content):   
        
    with open(filename,"w") as file: 
        file.write(content) 
        
    
def reader(filename): 
    
    file=open(filename,"r") 
    content=file.read() 
    file.close()
    return content
    

def appender (filename,content):  
    
    file=open(filename,'a') 
    file.write(content) 
    file.close()  
     

def generate_file_header(output_file,header_string):
    
    dashed_line='#######################------------------------#################'
    writer(output_file,dashed_line) 
    appender(output_file,'\n')
    appender(output_file,header_string) 
    appender(output_file,'\n') 
    appender(output_file,dashed_line)  
    appender(output_file,'\n')


def create_output_file(output_file,header_string,data_file):  
    
    generate_file_header(output_file,header_string)
    
    full_dict,drawings= create_raw_cable_dict(data_file)  
    classes=[]
    for i in range(len(drawings)):  
        focused_dict=dict_by_drawing(drawings[i],output_file,data_file) 
        
        a=CABLE(focused_dict,drawings[i]) 
        a.central()  
        
        appender(output_file,a.job_name) 
        appender(output_file,'\n')  
        appender(output_file,'######################') 
        appender(output_file,'\n')  
        appender(output_file,'\n')
        appender(output_file,str(a.conduit_df))  
        appender(output_file,'\n')
        appender(output_file,str(a.cable_types_df)) 
        appender(output_file,'\n')
        
        classes.append(a) 
        
        
    return classes

def main(): 
    
    ### output electrical drawings cable count ###
    output_file_electrical='Electrical.txt' 
    header_string_electrical='ALL ELECTRICAL DRAWINGS OUTPUT:'
    data_file_electrical="Electrical_Drawings.xlsx"  
    electrical_objects=create_output_file(output_file_electrical,header_string_electrical,data_file_electrical) 
    #create_output_file(output_file_electrical,header_string_electrical,data_file_electrical) 
    
    ### output FOC drawings cable count ###
    output_file_foc='FiberOptics.txt' 
    header_string_foc='ALL FIBER OPTICS DRAWINGS OUTPUT:'
    data_file_foc="FOC_Drawings.xlsx"  
    foc_objects=create_output_file(output_file_foc,header_string_foc,data_file_foc)  
    
    ### output Communication drawings cable count ###
    output_file_comm='Communications.txt' 
    header_string_comm='ALL COMMUNICATIONS DRAWINGS OUTPUT:'
    data_file_comm="Communication_Drawings.xlsx"  
    comm_objects=create_output_file(output_file_comm,header_string_comm,data_file_comm)
    
    
    return electrical_objects,foc_objects,comm_objects


if __name__ =="__main__":   
    main()


