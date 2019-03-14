# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:13:29 2019

@author: Chao
"""

import numpy as np
import h5py
import matplotlib.pyplot as plt
import csv

with h5py.File("H:\Users\chz78\HFSS\Wavegudie_ReactangularCavity_results\coup_vs_hole_r.hdf5", "r") as f:
    hole_r_list_o = f['hole_r_list'][:].tolist()
    couple_list = f['couple_list'][:].tolist()



#with h5py.File("H:\Users\chz78\HFSS\waveguide_cavity_simple_results\coup_vs_hole_r_300to400mil.hdf5", "r") as f:
#    hole_r_list_o_1 = f['hole_r_list'][:]
#    couple_list_1 = f['couple_list'][:]
#   
#
#hole_r_list_o = np.concatenate((np.array([0]),hole_r_list_o_0, hole_r_list_o_1))
#couple_list = np.concatenate((np.array([0]),couple_list_0, couple_list_1))

hole_r_list_o = [0] + hole_r_list_o
couple_list = [0] +couple_list


hole_r_list=np.linspace(0,0.4,101)
   
z3 = np.polyfit(hole_r_list_o, couple_list, 3)
fit_result_3 = z3[3] + z3[2] * hole_r_list + z3[1] * hole_r_list**2 + z3[0] * hole_r_list**3

z6 = np.polyfit(hole_r_list_o, couple_list, 6)
fit_result_6 = z6[6] + z6[5] * hole_r_list + z6[4] * hole_r_list**2 + z6[3] * hole_r_list**3 + z6[2] * hole_r_list**4 + z6[1] * hole_r_list**5 + z6[0] * hole_r_list**6




plt.figure()
plt.plot(hole_r_list, fit_result_3, label="3rd order fitting")
#plt.plot(hole_r_list, fit_result_6, label='6th order fitting')
plt.plot(hole_r_list_o, couple_list, "*")
plt.xlabel('hole radius (inch)')
plt.ylabel('coupling strength (MHz)')
plt.legend()



 
 
 