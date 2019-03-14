# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 18:23:06 2017

@author: Hat_Pinlei
"""

import Lib
import numpy as np
import matplotlib.pyplot as plt
import h5py

def inverse (x):
    return 1.0/x
    
oDesktop=None
oAnsoftApp=None
oProject=None
oDesign=None
oModule=None
oEditor=None

Lib.openProject(r"H:\Users\chz78\HFSS\Wavegudie_ReactangularCavity_HighFreq.aedt","Wavegudie_ReactangularCavity_HighFreq")

hole_a_list=[]
couple_list=[]

for m in range(1):
    hole_a = 0.2# 0.1 + m * 0.02
    print "hole_a" , hole_a , "inch"
    Lib.changeParameter("hole_a",str(hole_a)+"in")

    for n in range(21):     
        pin_h_list = map(inverse, np.linspace(1/0.3,1/0.4,num=21) )
        pin_height = pin_h_list[n]
        print "Raugh sweeping, pin_height is", pin_height  , "inch"
        Lib.changeParameter("pin_height",str(pin_height)+"in")
        Lib.AnalyzeAll()
    
    filename=r"H:\Users\chz78\HFSS\Wavegudie_ReactangularCavity_HighFreq_data\hole_a_"+ str(int(hole_a*1000))+"mil_raugh.csv"
    Lib.export(filename)
    min_point, min_def = Lib.Sweep_pin_height(filename)
    print "min_point=", min_point, "inch \nmin_def=", min_def, "MHz"
    
    for n in range(21):    
        pin_h_list = map(inverse, np.linspace(1/min_point + 0.025, 1/min_point - 0.025,num=21) )
        pin_height = pin_h_list[n]
        print "Fine sweeping, pin_height is", pin_height  , "inch"
        Lib.changeParameter("pin_height",str(pin_height)+"in")
        Lib.AnalyzeAll()
    
    filename=r"H:\Users\chz78\HFSS\Wavegudie_ReactangularCavity_HighFreq_data\hole_a_"+ str(int(hole_a*1000))+"mil_fine.csv"
    Lib.export(filename)    
    min_point, min_def = Lib.Sweep_pin_height(filename)
    print "min_point=", min_point, "inch \nmin_def=", min_def, "MHz"
    
    hole_a_list = hole_a_list + [hole_a]
    couple_list = couple_list + [min_def/2.0]
#Lib.quitProgram()

plt.plot(hole_a_list,couple_list,"*")
    

with h5py.File("H:\Users\chz78\HFSS\Wavegudie_ReactangularCavity_HighFreq_data\coup_vs_hole_r.hdf5", "w") as f:
    f.create_dataset("hole_a_list", data=hole_a_list)
    f.create_dataset("couple_list", data=couple_list)



#hole_radius=0.3
#filename=r"H:\Users\chz78\HFSS\Wavegudie_ReactangularCavity_results\hole_radisu_"+ str(int(hole_radius*1000))+"mil_fine.csv"  
#min_point, min_def = Lib.Sweep_pin_height(filename)    