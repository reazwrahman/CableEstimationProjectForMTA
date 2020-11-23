#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:22:12 2020

@author: Reaz
"""

import pandas as pd   
import os,re,sys
import cable_inspection 
from graph_classes import bar_graph  
import accubid_class as accubid


def find_class_from_drawing(drawing_no): 
    
    L,FOC,TE=cable_inspection.main() 
    total=L+FOC+TE  
    
    target=0 
    
    for i in range (len(total)): 
        if total[i].drawing.strip(' ')==drawing_no.strip(' '): 
            target=total[i] 
        
    
    if target!=0: 
        return target 
    
    if target==0: 
        print("This drawing number doesnt exist in REAZ's dataset") 
        #sys.exit()



def find_class_from_drawing_accubid(drawing_no): 
    
    total=accubid.main()  
    
    target=0 
    
    for i in range (len(total)): 
        if total[i].drawing.strip(' ')==drawing_no.strip(' '): 
            target=total[i] 
        
    
    if target!=0: 
        return target 
    
    if target==0: 
        print("This drawing number doesnt exist in ACCUBID's dataset")  
        pass
        

def plot_result(class_object,suppress_graph='no'): 
    
    df1=class_object.conduit_dict 
    
    print ('\n')
    print ("REAZ'S DATASET BELOW:")
    print (class_object.conduit_df)
    
    
    
    x1=list(df1.keys())  
    y1=[] 
    for i in range(len(df1)):  
        y1.append(df1[x1[i]][1])
        
    bg=bar_graph(x1,y1,label_columns='yes',ylabel='Total Length (ft.)',title=f'REAZ {class_object.drawing} Conduit Type VS. Length')
    graph_object1=bg.plot() 
     
    df2=class_object.cable_types_dict 
    x2=list(df2.keys())  
    y2=[] 
    for i in range(len(df2)):  
        y2.append(df2[x2[i]][1])
        
    bg2=bar_graph(x2,y2,label_columns='yes',ylabel='Total Length (ft.)',title=f'REAZ {class_object.drawing} Cable Type VS. Length',suppress_plot=suppress_graph)
    graph_object2=bg2.plot() 

    return [graph_object1,graph_object2]



def plot_result_accubid(class_object,suppress_graph='no'): 
    
    df1=class_object.conduit_dict  
    
    print ('\n')
    print ("ACCUBID'S DATASET BELOW")
    print (class_object.conduit_df)
    
    x1=list(df1.keys())  
    y1=[] 
    for i in range(len(df1)):  
        y1.append(df1[x1[i]])
        
    bg=bar_graph(x1,y1,label_columns='yes',ylabel='Total Length (ft.)',title=f'ACCUBID: {class_object.drawing} Conduit Type VS. Length')
    graph_object1=bg.plot()      

    return graph_object1



### THIS FUNCTION IS IN PROGRESS, NOT FINISHED YET
def plot_my_vs_accubid(class_object,drawing_no,suppress_graph='no'): 
    
    
    pass
    
    
      
  



def main(drawing_no): 
    
    #drawing_no=input('ENTER A DRAWING NUMBER TO PLOT THE RESULT:  ')
    target1=find_class_from_drawing(drawing_no)  
    try:
        a,b=plot_result(target1)  
    except: 
        print("Couldn't genereate a plot for Reaz's dataset")
    
    
    target2=find_class_from_drawing_accubid(drawing_no)   
    try: 
        c=plot_result_accubid(target2)
    except: 
        print("Couldn't genereate a plot for Accubid's dataset")
    


if __name__=="__main__":  
    drawing_no=input('ENTER A DRAWING NUMBER TO PLOT THE RESULT: ')
    main(drawing_no)
    
        
