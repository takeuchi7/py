# -*- coding: utf-8 -*-
#!/usr/bin/env python
import numpy as np
import pandas as pd
#%matplotlib inline

class Syokiti(object):
    def __init__(self,x,y,low_node,high_node,SIN_node,Line):
        self.x=x
        self.y=y
        self.low_node=low_node
        self.high_node=high_node
        self.SIN_node=SIN_node
        self.Line=Line
        
    
    def default(self):
        ave=0
        count=0
        SENZAI_node = self.SIN_node + self.Line

        for i in range(self.x*self.y):
            if(self.low_node[i]!=None):
                ave+=self.low_node[i]
                count+=1
            if(self.high_node[i]!=None):
                ave+=self.high_node[i]
                count+=1
        ave=ave/count
        print('ave',ave)
        for i in range(self.x*self.y):
            SENZAI_node[i]=ave
        return SENZAI_node
