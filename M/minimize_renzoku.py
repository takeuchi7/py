# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals
from collections import defaultdict
import numpy as np
import pandas as pd
#%matplotlib inline
np.random.seed(21212)
import random
from scipy import integrate
np.set_printoptions(threshold=np.inf)
import math
import numpy as np
from scipy.optimize import minimize

import lineprocess_func
import imp
imp.reload(lineprocess_func)

class Minimize_renzoku(object):
    
    def __init__(self,x,y,SENZAI_node,low_node,high_node,w0,w1,w2,c,Line):
        self.x=x
        self.y=y
        self.SENZAI_node=SENZAI_node
        self.low_node=low_node
        self.high_node=high_node
        self.w0=w0
        self.w1=w1
        self.w2=w2
        self.c=c
        self.Line=Line
        

    def ENEGY(self):

        #エネルギー関数最小化(高精度あり)
        back =self.linear_approximation()
        item = back
        for i in range(len(self.Line)):
            if(item[self.x*self.y+i]>0):
                item[self.x*self.y+i]=100000
            else:
                item[self.x*self.y+i]=-100000
        item = self.linear_approximation()
        
        return item
    
    def linear_approximation(self):
        res1 = minimize(lineprocess_func.func,self.SENZAI_node,args=(self.x,self.y,self.c,self.w0,self.w1,self.w2,self.low_node,self.high_node,), method='cobyla')
        p=0
        res1.x
        A=res1.x.tolist()
        return A