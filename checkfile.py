#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:45:10 2019

@author: hatlab
"""

import h5py
import matplotlib.pyplot as plt
plt.close("all")
lim = 20000
path=r"/media/hatlab/DataSaving/Cooldown_20180825/20181030/PXIe/qubit/test//"
filename="test1_"+str(n)
print n
dataOpen = h5py.File(path+filename, 'r')

print dataOpen.keys()

#I_data_0 = dataOpen["I_data"].value[0::2]
#Q_data_0 = dataOpen["Q_data"].value[0::2]
#I_data_1 = dataOpen["I_data"].value[1::2]
#Q_data_1 = dataOpen["Q_data"].value[1::2]

I_data_S = dataOpen["I_data"].value
Q_data_S = dataOpen["Q_data"].value

dataOpen.close()

n+=1

path=r"/media/hatlab/DataSaving/Cooldown_20180825/20181030/PXIe/qubit/test//"
filename="test1_"+str(n)
dataOpen = h5py.File(path+filename, 'r')
print n

print dataOpen.keys()

#I_data_0 = dataOpen["I_data"].value[0::2]
#Q_data_0 = dataOpen["Q_data"].value[0::2]
#I_data_1 = dataOpen["I_data"].value[1::2]
#Q_data_1 = dataOpen["Q_data"].value[1::2]

I_data_I = dataOpen["I_data"].value
Q_data_I = dataOpen["Q_data"].value

dataOpen.close()

I_final = I_data_S + I_data_I
Q_final = Q_data_S - Q_data_I
plt.hist2d(I_final, Q_final,  bins=101, range=[[-lim, lim],[-lim, lim]])
plt.figure()
plt.hist2d(I_data_S, Q_data_S, bins=101, range=[[-lim, lim],[-lim, lim]])





#fig, (ax1,ax2) = plt.subplots(1, 2)

#ax1.hist2d(I_data_0, Q_data_0, bins=101, range=[[-lim, lim],[-lim, lim]])
#ax2.hist2d(I_data_1, Q_data_1, bins=101, range=[[-lim, lim],[-lim, lim]])
##plt.show()
#print n
#n+=1
