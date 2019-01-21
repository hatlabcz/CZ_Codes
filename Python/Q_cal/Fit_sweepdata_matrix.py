# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:34:49 2016

@author: HatLab_Xi Cao
"""

# Try to do the fitting from the Matrix kind data

import h5py 
import Q_fit
import numpy as np
import matplotlib.pyplot as plt

Data = h5py.File('C:\Users\HatLab_Xi Cao\Box Sync\Data\Cooldown_2016_08_22\JPC_0014\Flux Sweep\signal_sweep_forward_finer_Sss_8_24_2016_17_2','r')
Currents = Data.get('currents').value
Freq = Data.get('measure_frequencies').value
Sweep = Data.get('sweep_data').value
Data.close()

# Need to add a short code to find the correct index (e.g. if we only want to 
# see the data for some cerntain current). So we just need to fit t

Fitting_data_Mag = 10**((Sweep[1011,0,1107:])/20.0)
Fitting_data_Phase = (Sweep[1011,1,1107:])*np.pi/180.0

Fitting_data_real = Fitting_data_Mag*np.cos(Fitting_data_Phase) 
Fitting_data_imag = Fitting_data_Mag*np.sin(Fitting_data_Phase) 

Fitting_Params = {'Q_ext': 150, 'Q_int': 1e7, 'A': 0.0, 'B': 0.0, 'E': 0.0, 'D': 0}
result = Q_fit.Fit(Freq[1107:],Fitting_data_real,Fitting_data_imag, Fitting_Params, plot = True, Method = 1)