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

def func(X,x,y,c,w0,w1,w2,low_node,high_node):
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
            w=1 / (1 + e**((-1)*(w0[i])*0.1))
            E+=w*(X[i]-low_node[i])**2
    for i in range(x*y):
        if(high_node[i]!=None):
            E+=w1*(X[i]-high_node[i])**2

#   p=x*y
#    for i in range(x-1):
#        for j in range(y-1):
#            E+=(X[i+p+(j*(x-1))]-X[i+p+(j*(x-1))+(x-1)])**2
#
#    p=x*y+(x-1)*y
#    for i in range(x-1):
#        for j in range(y-1):
#            E+=(X[i+p+(j*(y-1))]-X[i+p+(j*(y-1))+(y-1)])**2

    return E

def linear_approximation(SENZAI_node,w0,w1,w2,x,y,low_node,high_node,c):
    w0 = w0
    w1 = w1
    w2 = w2
    low_node=low_node
    res1 = minimize(func,[SENZAI_node],args=(x,y,c,w0,w1,w2,low_node,high_node,), method='cobyla')
    p=0
    res1.x
    A=res1.x.tolist()
    return A
