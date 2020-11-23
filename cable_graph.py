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
import accubid_class






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
        print('INVALID DRAWING NUMBER, TRY AGAIN') 
        sys.exit()


def plot_result(class_object,suppress_graph='no'): 
    
    df1=class_object.conduit_dict 
    x1=list(df1.keys())  
    y1=[] 
    for i in range(len(df1)):  
        y1.append(df1[x1[i]][1])
        
    bg=bar_graph(x1,y1,label_columns='yes',ylabel='Total Length (ft.)',title=f'{class_object.drawing} Conduit Type VS. Length')
    graph_object1=bg.plot() 
     
    df2=class_object.cable_types_dict 
    x2=list(df2.keys())  
    y2=[] 
    for i in range(len(df2)):  
        y2.append(df2[x2[i]][1])
        
    bg2=bar_graph(x2,y2,label_columns='yes',ylabel='Total Length (ft.)',title=f'{class_object.drawing} Cable Type VS. Length',suppress_plot=suppress_graph)
    graph_object2=bg2.plot() 

    return [graph_object1,graph_object2]


def plot_my_vs_accubid():




def main(): 
    global a 
    drawing_no=input('ENTER A DRAWING NUMBER TO PLOT THE RESULT:  ')
    target=find_class_from_drawing(drawing_no)  
    a,b=plot_result(target)
    
    #print (a)


if __name__=="__main__": 
    main()
    
        
