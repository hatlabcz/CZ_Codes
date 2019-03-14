# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 18:23:06 2017

@author: Hat_Pinlei
"""

import Lib
import numpy as np
oDesktop=None
oAnsoftApp=None
oProject=None
oDesign=None
oModule=None
oEditor=None

Lib.openProject(r"H:\Users\chz78\HFSS\Reactangular_Cavity.aedt","Reactangular_Cavity")

def inverse (x):
    return 1.0/x
    
pin_h_list = map(inverse, np.linspace(1/0.35,1/0.8,num=31) )

for n in range(len(pin_h_list)):
    pin_height =  pin_h_list[n]
    print "pin_height is", pin_height, "in"
    Lib.changeParameter("pin_height",str(pin_height)+"in")
    Lib.AnalyzeAll()

Lib.savefile()
#Lib.quitProgram()
        
    







      