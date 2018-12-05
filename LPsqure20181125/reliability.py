# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals
from collections import defaultdict
import numpy as np
#%matplotlib inline

def create_reliability(x,y,low_node,item,None_item):
    trust=[0]*(x*y)
    for i in range(len(trust)):
        if(low_node[i]!=None):
            trust[i]=abs(None_item[0][0][i]-low_node[i])-abs(item[0][0][i]-low_node[i])
            trust[i]=round(trust[i],3)
        else:
            trust[i]=None
    return trust
