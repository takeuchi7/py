# -*- coding: utf-8 -*-
#!/usr/bin/env python
import numpy as np
import pandas as pd
#%matplotlib inline

def default(x,y,low_node,high_node,SIN_node,Line):
    ave=0
    count=0
    SENZAI_node = SIN_node + Line
    
    for i in range(x*y):
        if(low_node[i]!=None):
            ave+=low_node[i]
            count+=1
        if(high_node[i]!=None):
            ave+=high_node[i]
            count+=1
    ave=ave/count
    print('ave',ave)
    for i in range(x*y):
        SENZAI_node[i]=ave
    return SENZAI_node
