# -*- coding: utf-8 -*-
#!/usr/bin/env python
import numpy as np
import pandas as pd
#%matplotlib inline
np.random.seed(21212)
import random
from syokiti import Syokiti
from minimize_risan import Minimize_risan
from minimize_renzoku import Minimize_renzoku
from mrf_plot import Mrf_plot
from init_state import Init_state
import MRF_PLOT1
import imp
imp.reload(MRF_PLOT1)

class Times(object):
    def __init__(self,x,y,node,ob_variables,state,low_node,high_node,w0,w1,w2,c,SENZAI_node,SIN_node,Line,opt,PROB_MATRIX):
        self.x = x
        self.y = y
        self.node = node
        self.ob_variables = ob_variables
        self.state = state
        self.low_node = low_node
        self.high_node = high_node
        self.w0 = w0
        self.w1 = w1
        self.w2 = w2
        self.c = c
        self.SENZAI_node = SENZAI_node
        self.SIN_node = SIN_node
        self.Line =  Line
        self.opt = opt
        self.PROB_MATRIX = PROB_MATRIX
        
        self.z_1 = []
        
    
    def t_1(self):
        #ob_variables = random.choices(self.state,k=4)
        print('時刻１の潜在変数の状態',self.ob_variables)

        #Z_1は１時刻目の潜在変数
        senzai_risan_minimize=Minimize_risan(self.x,self.y,self.node,self.ob_variables,self.state)
        z_1 = senzai_risan_minimize.risan()
        self.z_1 = z_1

        #初期値設定(高精度あり)
        syokika = Syokiti(self.x,self.y,self.low_node,self.high_node,self.SIN_node,self.Line)
        SENZAI_node = syokika.default()

        #低精度のみの推定と，高精度を含んだ推定  
        marcov_lineprocess_minimize=Minimize_renzoku(self.x,self.y,self.SENZAI_node,self.low_node,self.high_node,self.w0,self.w1,self.w2,self.c,self.Line,self.opt,z_1)
        x_1 =marcov_lineprocess_minimize.ENEGY()
        print('x_1',x_1) 

        #描画
        PLOT = Mrf_plot(x_1,self.x,self.y)
        PLOT.MRF_PLOT()
        
    def t_2(self):
        move_state=Init_state(self.PROB_MATRIX ,self.z_1)
        z_2 = move_state.state()
        print('z_2',z_2)

        #Z_2は2時刻目の潜在変数
        senzai_risan_minimize=Minimize_risan(self.x,self.y,self.node,z_2,self.state)
        z_2 = senzai_risan_minimize.risan()

        #初期値設定(高精度あり)
        syokika = Syokiti(self.x,self.y,self.low_node,self.high_node,self.SIN_node,self.Line)
        SENZAI_node = syokika.default()

        #低精度のみの推定と，高精度を含んだ推定  
        marcov_lineprocess_minimize=Minimize_renzoku(self.x,self.y,self.SENZAI_node,self.low_node,self.high_node,self.w0,self.w1,self.w2,self.c,self.Line,self.opt,z_2)
        x_2 =marcov_lineprocess_minimize.ENEGY()
        print('x_2',x_2) 

        #描画
        PLOT = Mrf_plot(x_2,self.x,self.y)
        PLOT.MRF_PLOT()
