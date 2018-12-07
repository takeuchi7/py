# -*- coding: utf-8 -*-
#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon, Ellipse
import numpy as np
from scipy.optimize import minimize

class Mrf_plot(object):
    def __init__(self,item,x,y):
        self.item = item
        self.x = x
        self.y = y
    
    def MRF_PLOT(self):
        plt.figure(figsize=(8, 8))
        ax = plt.gca()
        ellipse_size=0.8/(self.x*self.y)
        spacex=0.8/(self.x-1)
        spacey=0.8/(self.y-1)   
        sizex=0.1
        sizey=0.1
        sizex=0.1
        sizey=0.1
        k=0
        l=0
        for i in range(self.y):
            sizex=0.1
            for j in range(self.x): 
                if(j!=self.x-1):
                    p = plt.Line2D(xdata=(sizex, sizex+spacex), ydata=(sizey, sizey), color='k', linewidth=1)
                    ax.add_line(p)
                    plt.text(sizex+spacex/2, sizey, round(self.item[self.x*self.y+l],2))
                    if(self.item[self.x*self.y+l]>0):
                        p = plt.Line2D(xdata=(sizex+spacex/2, sizex+spacex/2), ydata=(sizey-spacey/2, sizey+spacey/2), color='y', linewidth=1)
                        ax.add_line(p)
                    l+=1
                p = Ellipse(xy=(sizex, sizey), height=ellipse_size, width=ellipse_size,fill=False,ec='b')
                plt.text(sizex, sizey, round(self.item[k],2))
                ax.add_patch(p)

                sizex+=spacex
                k+=1
            sizey+=spacey
        sizex=0.1
        sizey=0.1
        k=0
        for i in range(self.x):
            sizey=0.1
            for j in range(self.y):         
                if(j!=self.y-1):
                    p = plt.Line2D(xdata=(sizex, sizex), ydata=(sizey, sizey+spacey), color='k', linewidth=1)
                    ax.add_line(p)
                    plt.text(sizex, sizey+spacey/2, round(self.item[self.x*self.y+l],2))
                    if(self.item[self.x*self.y+l]>0):
                        p = plt.Line2D(xdata=(sizex-spacex/2, sizex+spacex/2), ydata=(sizey+spacey/2, sizey+spacey/2), color='y', linewidth=1)
                        ax.add_line(p)
                    l+=1

                sizey+=spacey
                k+=1
            sizex+=spacex

        #plt.tight_layout()
        plt.savefig('kyuri.png')
        plt.show()
    
