#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:02:21 2020

@author: Reaz
"""

import troubleshooter as ts 
import cable_graph as cg 

class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = []

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]




job_number=int(input('Enter job number: '))
conduit_size=input('Enter conduit size: ')
drawings=ts.troubleshooter1(job_number,conduit_size) 


for each in drawings: 
    cg.main(each) 

print (job_number)
print (conduit_size)
print (drawings)