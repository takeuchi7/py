# -*- coding: utf-8 -*-
#!/usr/bin/env python

class Input(object):
    def __init__(self):
        #x*yのマルコフモデル
        self.x = 0
        self.y = 0
        self.z = 0
        #重み（w0:高精度、w1:低精度、w2:隣接）
        self.w0=0
        self.w1=0
        self.w2=0
        #ラインププロセスの閾値
        self.c = 0
        #状態
        self.state = []
        #状態の辞書
        self.opt = {}
        #時刻１
        self.node = []
        self.ob_variables = []
        
        self.low_node=[]
        self.high_node=[]
        self.Line = []
        self.SIN_node = []
        self.SENZAI_node = []
        self.syokiSENZAI_node = []
        self.PROB_MATRIX  = []
    
    def load(self):
        self.x = 2
        self.y = 2
        self.z = self.x*(self.y-1)+self.y*(self.x-1)
        #重み（w0:高精度、w1:低精度、w2:隣接）
        self.w0=3
        self.w1=2
        self.w2=0.5
        #ラインププロセスの閾値
        self.c = 100
        #状態
        self.state = [0,1]
        #状態の辞書
        self.opt = {self.state[0]:{'mu':0,'sigma':10},self.state[1]:{'mu':200,'sigma':10}}
        #時刻１
        self.node = [0,0,0,0]
        self.ob_variables = [0,0,1,1]

        self.low_node=[200,None,5,5]
        self.high_node=[200,None,5,5]
        self.Line = [0] * self.z
        self.SIN_node = [20,20,20,20]
        self.SENZAI_node = self.SIN_node + self.Line
        self.syokiSENZAI_node = self.SIN_node + self.Line
        
        #状態遷移
        self.PROB_MATRIX = [[0.7, 0.3],
                            [0.2, 0.8,]]

