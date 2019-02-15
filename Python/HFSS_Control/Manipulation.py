# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 18:23:06 2017

@author: Hat_Pinlei
"""

import Lib
import h5py
oDesktop=None
oAnsoftApp=None
oProject=None
oDesign=None
oModule=None
oEditor=None

Lib.openProject(r"H:\Users\chz78\HFSS\Single_Cavity.aedt","Single_Cavity")

alp = []
kappa = []
frq = []
frc = []

for n in range(30):
    
    pin_height =   0.49 + n * 0.001
    print "pin_height is", pin_height
    Lib.changeParameter("pin_height",str(pin_height)+"in")
    Lib.AnalyzeAll()

Lib.savefile()
#Lib.quitProgram()
        
    







      