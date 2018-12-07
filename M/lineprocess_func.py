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

#最小化：隣接同士と、入力の遷移を観測値と捉えていく
def func(X,x,y,c,w0,w1,w2,low_node,high_node,opt,z_1):
    e = math.e
    E=0
    p=x*y
    for i in range(x*y):
        if(i%x!=(x-1)):
            E+=w2*((X[i]-X[i+1])**2)*(1-(1 / (1 + e**(-X[p]))))+c * (1 / (1 + e**(-X[p])))+(1 / (1 + e**(-X[p])))*(1-(1 / (1 + e**(-X[p]))))
            p+=1
    for i in range(x):
        for j in range(y-1):
            E+=w2*((X[i+(j*x)]-X[i+(j*x)+x])**2) * (1-(1 / (1 + e**(-X[p]))))+c * (1 / (1 + e**(-X[p])))+(1 / (1 + e**(-X[p])))*(1-(1 / (1 + e**(-X[p]))))
            p+=1
    for i in range(x*y):
        if(low_node[i]!=None):
            #w=1 / (1 + e**((-1)*(w0)*0.1))
            E+=w0*(X[i]-low_node[i])**2
        if(high_node[i]!=None):
            E+=w1*(X[i]-high_node[i])**2
            
    for i in range(x*y):
        N = np.random.normal(opt[z_1[i]]['mu'],opt[z_1[i]]['sigma'])
        #print('{0}番目のガウス：{1}'.format(i,N))
        E+=0.01*(X[i]-N)**2

    return E