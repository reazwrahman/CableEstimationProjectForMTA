#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:18:24 2020

@author: Reaz
""" 

import threading
import os,re,sys 

from docx_class import DOCX  
import cable_inspection 
import cable_graph as tc  


 

def electrical(L):  
    
    electrical_report=DOCX(filename='Electrical_Drawings_TC.docx', 
                heading='11 Elevator Project: Electrical Drawings')  
    
    for i in range (len(L)): 
        graph_objects=tc.plot_result(L[i],suppress_graph='yes')  
        graph1=graph_objects[0] 
        graph2=graph_objects[1]
        electrical_report.write_graph(graph1,graph_name=f'{L[i].drawing} : {L[i].job_name} below:',image_width=4.25)
        electrical_report.write_graph(graph2,graph_name=f'{L[i].drawing} : {L[i].job_name} below:',image_width=4.25)
        electrical_report.add_page_break()

def communication(TE):  
    
    comm_report=DOCX(filename='Communication_Drawings_TC.docx', 
                heading='11 Elevator Project: Communication/Fire Alarms Drawings')  
    
    for i in range (len(TE)): 
        graph_objects=tc.plot_result(TE[i],suppress_graph='yes')  
        graph1=graph_objects[0] 
        graph2=graph_objects[1]
        comm_report.write_graph(graph1,graph_name=f'{TE[i].drawing} : {TE[i].job_name} below:',image_width=4.25)
        comm_report.write_graph(graph2,graph_name=f'{TE[i].drawing} : {TE[i].job_name} below:',image_width=4.25)
        comm_report.add_page_break()

def foc(FOC): 
    
    foc_report=DOCX(filename='FOC_Drawings_TC.docx', 
                heading='11 Elevator Project: Fiber Optics Drawings')  
    
    for i in range (len(FOC)): 
        graph_objects=tc.plot_result(FOC[i],suppress_graph='yes')  
        graph1=graph_objects[0] 
        graph2=graph_objects[1]
        foc_report.write_graph(graph1,graph_name=f'{FOC[i].drawing} : {FOC[i].job_name} below:',image_width=4.25)
        foc_report.write_graph(graph2,graph_name=f'{FOC[i].drawing} : {FOC[i].job_name} below:',image_width=4.25)
        foc_report.add_page_break()

def main(): 

    L,FOC,TE=cable_inspection.main() 
    
   
#    t1 = threading.Thread(target=electrical, args=(L,)) 
#    t2 = threading.Thread(target=communication, args=(TE,))   
#    t3 = threading.Thread(target=foc, args=(FOC,))  
#     
#    t1.start() 
#    t2.start()  
#    t3.start() 
#  
#    t1.join() 
#    t2.join()  
#    t3.join()  
    
    electrical(L) 
    communication(TE) 
    foc(FOC)
    
    print ('all thread completed')
    print ('Three docx created') 
    

if __name__=="__main__": 
    main()
    
    
  