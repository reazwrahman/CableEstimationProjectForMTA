#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:16:17 2020

@author: Reaz
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np




class bar_graph(object): 
    
    def __init__ (self,x,y1,y2=None,xlabel='Data Labels',ylabel='Datasets', 
                  title='Bar Graph',data1name='Data1',data2name='Data2', 
                  label_columns="no",suppress_plot="no"):
         
      
        self.xval=x 
        self.y1val=y1 
        
        if y2==None: 
            self.y2val=y1 
            self.how_many=1 
        else:  
            self.y2val=y2
            self.how_many=2
            
        
        self.xlabel=xlabel 
        self.ylabel=ylabel 
        self.title=title 
        
        self.data1name=data1name 
        self.data2name=data2name 
        
        self.label_columns=label_columns 
        
        
        if suppress_plot=="yes":  
            self.suppress="yes"
            matplotlib.use('Agg') 
        else: 
            self.suppress="no"
         
        
            
    def plot(self):    
                 
        x = np.arange(len(self.xval))  # the label locations
        width = 0.35  # the width of the bars
        
        fig, ax = plt.subplots() 
        
        if self.how_many==2: 
            rects1 = ax.bar(x - width/2, self.y1val, width, label=self.data1name)
            rects2 = ax.bar(x + width/2, self.y2val, width, label=self.data2name)
        
        elif self.how_many==1: 
            rects1 = ax.bar(x - width/(width*100), self.y1val, width, label=self.data1name)
        
        
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(self.ylabel)
        ax.set_title(self.title)
        ax.set_xticks(x)
        ax.set_xticklabels(self.xval)
        ax.legend()
        
        
        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0,1),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')
        
        if self.label_columns=="yes" and self.how_many==2: 
            autolabel(rects1)
            autolabel(rects2) 
        
        if self.label_columns=="yes" and self.how_many==1: 
            autolabel(rects1)
        
        
        ax.plot()
        fig.tight_layout()  
        
        if self.suppress=="no": 
            plt.show()    
        else: 
            pass 
        
        return ax
        
  



def test(): 
    global a 
    labels = ['BA', 'MSFT', 'XOM','BA']
    men_means = [100,2,3,10]
    women_means = [1,2,3,100]
    bg=bar_graph(labels,women_means,label_columns="no",suppress_plot="yes") 
    a=bg.plot()  
    
    
    
if __name__=="__main__": 
    test()