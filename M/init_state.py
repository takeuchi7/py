# -*- coding: utf-8 -*-
#!/usr/bin/env python
import numpy as np
import pandas as pd
#%matplotlib inline

class Init_state(object):
    def __init__(self,PROB_MATRIX,z_1):
        self.PROB_MATRIX=PROB_MATRIX
        self.z_1=z_1
        
    def state(self):
        for num, element in enumerate(self.z_1):
            for i in range(1):
                next_state = self.get_next_state(self.PROB_MATRIX[element])
                self.z_1[num]=next_state
        A = self.z_1
        return A

    def get_next_state(self,prob_array):
        #print('prob_array',prob_array)
        normalization_factor = sum(prob_array)
        #print('normalization_factor',normalization_factor)
        rand_num = np.random.rand(1)
        #print('rand_num',rand_num)
        s = 0
        for i in range(len(prob_array)):
            s += prob_array[i]/normalization_factor
            #print('s',s)
            if rand_num < s:
                return i
        return -1