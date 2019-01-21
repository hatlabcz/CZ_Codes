# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 11:33:44 2017

@author: CZ
"""

# Fit_fluxsweep_data

import h5py
import Q_fit
import numpy as np



path = 'C:\Users\HatLab_Xi Cao\Box Sync\Data\Cooldown_2016_12_31\\2017_01_16\JPC0021\Flux_sweep\\'
name = 'Idler_fluxsweep_forward_1_16_2017_14_4'

data = h5py.File(path+name, 'r')
currents = data['currents'].value
measure_frequencies = data['measure_frequencies'].value
sweep_data = data['sweep_data'].value
data.close()

## use this portion of code to check the fitting at any specific bias current
#index = 400
#print 'The index is ' + str(index) + ':'
#Fitting_data_Mag = 10**((sweep_data[index, 0, :])/20.0)
#Fitting_data_Phase = (sweep_data[index, 1, :])*np.pi/180.0
#print Fitting_data_Mag[0]
#print Fitting_data_Phase[0]
#
##plt.plot(measure_frequencies, Fitting_data_Phase)
##B_real = Background_Mag*np.cos(Background_Phase)
##B_imag = Background_Phase*np.sin(Background_Phase)
#Fitting_data_real = Fitting_data_Mag*np.cos(Fitting_data_Phase) 
#Fitting_data_imag = Fitting_data_Mag*np.sin(Fitting_data_Phase) 
#
##Fitting_Params = {'Q_ext': 20000, 'Q_int': 10000, 'A': 3.6681889378123505e-10, 'B': -19.966263980082346, 'E': -1.0370950026119112e-09, 'D': 47}
#Fitting_Params = {'Q_ext': 100.0, 'Q_int':100000.0 , 'A': 0.0, 'B': 0.0, 'E': 0.0, 'D': 0}
##plt.plot(Freq, Fitting_data_real)
#result = Q_fit.Fit(measure_frequencies,Fitting_data_real,Fitting_data_imag, Fitting_Params, plot = True, Method = 1)
#index = index + 1


def fit_loop(sweepdata, freq):

#    freq  = measure_frequencies
    Fitting_data_Mag = 10**((sweepdata[0, :])/20.0)
    Fitting_data_Phase = (sweepdata[1, :])*np.pi/180.0


    #plt.plot(measure_frequencies, Fitting_data_Phase)
    #B_real = Background_Mag*np.cos(Background_Phase)
    #B_imag = Background_Phase*np.sin(Background_Phase)
    Fitting_data_real = Fitting_data_Mag*np.cos(Fitting_data_Phase) 
    Fitting_data_imag = Fitting_data_Mag*np.sin(Fitting_data_Phase) 
    
    #Fitting_Params = {'Q_ext': 20000, 'Q_int': 10000, 'A': 3.6681889378123505e-10, 'B': -19.966263980082346, 'E': -1.0370950026119112e-09, 'D': 47}
    Fitting_Params = {'Q_ext': 100.0, 'Q_int':100000.0 , 'A': 0.0, 'B': 0.0, 'E': 0.0, 'D': 0}
    #plt.plot(Freq, Fitting_data_real)
    result = Q_fit.Fit(freq,Fitting_data_real,Fitting_data_imag, Fitting_Params, plot = False, Method = 1)
    return result
#    print '\n'

startpoint = 100
endpoint = 400
pointnum = endpoint - startpoint

f0 = np.zeros(pointnum)
Q_ext = np.zeros(pointnum)
Q_int = np.zeros(pointnum)
chi = np.zeros(pointnum)

index = startpoint

while index < endpoint:
    print 'The index is ' + str(index) + ':'
#    print measure_frequencies
    temp = fit_loop(sweep_data[index], measure_frequencies)
    f0[index - startpoint] = temp[0]
    Q_ext[index - startpoint] = temp[1]
    Q_int[index - startpoint] = temp[2]
    chi[index - startpoint] = temp[3].redchi
    index = index + 1
    measure_frequencies = measure_frequencies/(2*np.pi)

#plt.plot(f0, Q_ext)

name = name + '_fitting_result_full_range'
Data = h5py.File(path+name, 'w-')
Data.create_dataset('resonant_frequency', data = f0)
Data.create_dataset('Q_ext', data = Q_ext)
Data.create_dataset('Q_int', data = Q_int)
Data.create_dataset('chi', data = chi)
Data.close()
    
    
    
    
    
    
    
    
    
    