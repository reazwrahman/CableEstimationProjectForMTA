#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:31:04 2020

@author: Reaz
"""

import cable_inspection as cip 

job_name_dict={
               100:'207TH STREET STATION', 
               200:'34TH HERALD SQUARE STATION 6TH AVE (IND)', 
               300:'34TH HERALD SQUARE STATION BROADWAY (BMT)', 
               400:'FLATBUSH AVE STATION',  
               500:'CHURCH AVE STATION', 
               600:'JAMAICA CENTER PARSONS/ ARCHER STATION',	
               700:'SUTPHIN BOULEVARD/ ARCHER AVE STATION'	
              }  



L,FOC,TE=cip.main() 
total=L+TE+FOC 

job_sites=list(job_name_dict.values())
job_classifier={} 
for sites in job_sites: 
    job_classifier[sites]=[]

for i in range (len(total)): 
    for j in range (len(job_sites)): 
        if total[i].job_name==job_sites[j]: 
            job_classifier[job_sites[j]].append(total[i].drawing) 


        
#print (job_classifier)  
            
a=job_classifier[job_name_dict[100]] 
b=job_classifier[job_name_dict[200]] 
c=job_classifier[job_name_dict[300]] 
d=job_classifier[job_name_dict[400]] 
e=job_classifier[job_name_dict[500]] 
f=job_classifier[job_name_dict[600]] 
g=job_classifier[job_name_dict[700]] 













