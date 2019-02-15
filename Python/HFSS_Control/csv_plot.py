# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:54:11 2019

@author: Chao
"""

import csv
import numpy as np
import matplotlib.pyplot as plt




plt.close("all")
def read_csv(filename):    
    with open (filename,'rb') as csvres:
        result = csv.reader(csvres)
        res = list(result)
        del res[0]
    xdata = []
    ydata = []
    for i in res:
        xdata = xdata + [float(i[0])]
        ydata = ydata + [float(i[1])]  
        
    return xdata, ydata
    
    
filepath= r"H:\Users\chz78\HFSS\waveguide_eigenmode_E\\"
y=[]
for i in range(5):
    filename= filepath + "mode" + str(i+1) + ".csv"
    x,y= read_csv(filename)
    plt.plot(x,y,label='mode'+str(i+1))
    if i==0:
        E_mag=np.array(y)
    else:
        E_mag=E_mag + np.array(y)

plt.plot(x,E_mag/5.0,label='sum')
plt.legend()
plt.xlabel("x/mm")
plt.ylabel("E/(V/m)")