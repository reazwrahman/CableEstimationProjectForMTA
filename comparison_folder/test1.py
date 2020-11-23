#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:22:12 2020

@author: Reaz
"""

import pandas as pd   
import os,re,sys
import cable_inspection 


os.chdir(r'/Users/Reaz/Desktop/TC ELECTRIC LLC/CABLE INSPECTION PROJECT')
L,TE,FOC=cable_inspection.main()

#df=pd.read_excel('test_data.xlsx')  
#conduit=list(df['Conduit'] )


