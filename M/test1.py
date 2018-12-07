# -*- coding: utf-8 -*-
#!/usr/bin/env python
import numpy as np
import pandas as pd
#%matplotlib inline

class Times1(object):
    def __init__(self,CG):
        self.x=CG.x
        
    
    def default(self):
        self.x = 10
        
        
