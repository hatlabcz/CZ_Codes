# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 09:31:33 2016

@author: HatLab_Xi Cao
"""

# Fit txt
import numpy as np
import Q_fit


def read_txt_data():
    filename = 'C:\\Users\\HatLab_Xi Cao\\Desktop\\s11.txt'         
    data = np.genfromtxt(filename, delimiter = '\t', skiprows = 1, missing_values = ' ')
    
    Freq = data[:,0]
    Real = data[:,1]
    Imag = data[:,2]
    
    return (Freq, Real, Imag)


(Freq, Real, Imag) = read_txt_data()
Fitting_Params = {'Q_ext': 90000, 'Q_int':5000 , 'A': 0.0, 'B': 0.0, 'E': 0.0, 'D': 0}
result = Q_fit.Fit(Freq,Real,Imag, Fitting_Params, plot = True, Method = 1)