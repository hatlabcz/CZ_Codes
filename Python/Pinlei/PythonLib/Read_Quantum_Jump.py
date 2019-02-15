# -*- coding: utf-8 -*-
"""
Created on Fri Mar 02 10:31:00 2018

@author: HatLab_Xi Cao
"""

import h5py
import matplotlib.pyplot as plt
import numpy as np
import math

def read_data(filename):
    data = h5py.File(filename,'r')
    I = data["I_data"].value
    Q = data["Q_data"].value
    data.close()
    return I,Q
    
def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    window_size = np.abs(np.int(window_size))
    order = np.abs(np.int(order))
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * math.factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid') 

def analyze(ydata):
    num = 0
    for i in range(len(ydata)-1):
        if ydata[i]*ydata[i+1] < 0:
            num +=1
            if ydata[i] < -
    return num
path = r'H:\Data\Fridge Texas\Cooldown_20180222\20180302\WJPC0032\Qubit\quantum_jump_200\\'
name = 'quantum_jump_phase_360ns_per_point_2V_cavity_drive'


t = np.linspace(0,99.36,277)
I,Q = read_data(path+name)
IQ = I + 1j*Q
theta = np.pi*1.3
IQ_new = IQ*np.exp(1j*theta)    
yaxis = IQ_new.real
plt.plot(t,yaxis)

yaxis = savitzky_golay(IQ_new.real,31,0)
print analyze(yaxis)

#num = 0
#count = np.zeros(199)
#for i in range(199):
#    print i
#    name = 'quantum_jump_phase_360ns_per_point_2V_cavity_drive' + '_({})'.format(num)
#    I,Q = read_data(path+name)
#    IQ = I + 1j*Q
#    theta = np.pi*1.3
#    IQ_new = IQ*np.exp(1j*theta)
#    _count = analyze(savitzky_golay(IQ_new.real,31,0))
#    count[i] = _count
#    num += 1
#
#print 'Average Jump: ', np.average(count)
    









