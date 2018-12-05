# -*- coding: utf-8 -*-
#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon, Ellipse
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def MRF_PLOT(item,x,y):
    plt.figure()
    ax = plt.gca(projection='3d')
    ellipse_size=0.1
    spacex=0.8/(x-1)
    spacey=0.8/(y-1)   
    sizex=0.1
    sizey=0.1
    k=0
    l=0
    for i in range(y):
        sizex=0.1
        for j in range(x): 
            if(j!=x-1):
                p = plt.Line2D(xdata=(sizex, sizex+spacex), ydata=(sizey, sizey),zdata=(0.5,0,5) ,color='k', linewidth=1)
                ax.add_line(p)
                plt.text(sizex+spacex/2, sizey, 0.5, round(item[0][0][x*y+l],2))
                if(item[0][0][x*y+l]>0):
                    p = plt.Line3D(xdata=(sizex+spacex/2, sizex+spacex/2), ydata=(sizey-spacey/2, sizey+spacey/2),zdata=(0.5,0,5) ,color='y', linewidth=1)
                    ax.add_line(p)
                l+=1
            p = Ellipse(xy=(sizex, sizey,0.5), height=ellipse_size, width=ellipse_size,fill=False,ec='b')
            plt.text(sizex, sizey,0.5,round(item[0][0][k],2))
            ax.add_patch(p)
            
            sizex+=spacex
            k+=1
        sizey+=spacey
    sizex=0.1
    sizey=0.1
    k=0
    for i in range(x):
        sizey=0.1
        for j in range(y):         
            if(j!=y-1):
                p = plt.Line2D(xdata=(sizex, sizex), ydata=(sizey, sizey+spacey), color='k', linewidth=1)
                ax.add_line(p)
                plt.text(sizex, sizey+spacex/2, round(item[0][0][x*y+l],2))
                if(item[0][0][x*y+l]>0):
                    p = plt.Line2D(xdata=(sizex-spacex/2, sizex+spacex/2), ydata=(sizey+spacey/2, sizey+spacey/2), color='y', linewidth=1)
                    ax.add_line(p)
                l+=1
          
            sizey+=spacey
            k+=1
        sizex+=spacex
        
    #plt.tight_layout()
    plt.savefig('kyuri.png')
    plt.show()
    
