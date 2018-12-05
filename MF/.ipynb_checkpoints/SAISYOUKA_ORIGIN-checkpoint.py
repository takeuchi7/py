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
import SAISYOUKA
import imp
imp.reload(SAISYOUKA)

def ENEGY(x,y,SENZAI_node,None_SENZAI_node,low_node,high_node,None_high_node,w0,w1,w2,c,Line):

    #エネルギー関数最小化(高精度あり)
    back =SAISYOUKA.linear_approximation(SENZAI_node,w0,w1,w2,x,y,low_node,high_node,c)
    item = back
    for i in range(len(Line)):
        if(item[0][x*y+i]>0):
            item[0][x*y+i]=100000
        else:
            item[0][x*y+i]=-100000
    item = SAISYOUKA.linear_approximation(item,w0,w1,w2,x,y,low_node,high_node,c)
    
    
    #エネルギー関数最小化(高精度なし)
    back =SAISYOUKA.linear_approximation(None_SENZAI_node,w0,w1,w2,x,y,low_node,None_high_node,c)
    None_item = back
    for i in range(len(Line)):
        if(None_item[0][x*y+i]>0):
            None_item[0][x*y+i]=100000
        else:
            None_item[0][x*y+i]=-100000
    None_item = SAISYOUKA.linear_approximation(None_item,w0,w1,w2,x,y,low_node,None_high_node,c)
    
    return item,None_item