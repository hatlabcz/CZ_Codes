#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:45:10 2019

@author: hatlab
"""

import h5py
import matplotlib.pyplot as plt
import numpy as np
plt.close("all")
lim = 7500
#path=r"/media/hatlab/DataSaving/Cooldown_20180825/20181030/PXIe/qubit/test//"
path=r"H:\Data\Fridge Texas\Cooldown_20190119\PXIeTest\20190125\Correlation_Relation\\"
filename="data"
#print n
dataOpen = h5py.File(path+filename, 'r')
print dataOpen.keys()

#I_data_0 = dataOpen["I_data"].value[0::2]
#Q_data_0 = dataOpen["Q_data"].value[0::2]
#I_data_1 = dataOpen["I_data"].value[1::2]
#Q_data_1 = dataOpen["Q_data"].value[1::2]

I_s = dataOpen["I_s"].value
Q_s = dataOpen["Q_s"].value
I_i = dataOpen["I_i"].value
Q_i = dataOpen["Q_i"].value
dataOpen.close()


I_m = I_s - I_i
I_p = I_s + I_i
Q_m = Q_s - Q_i
Q_p = Q_s + Q_i


plt.figure("S")
plt.hist2d(I_s, Q_s, bins=101, range=[[-lim, lim],[-lim, lim]])
plt.colorbar()
plt.axes().set_aspect('equal')
plt.figure("I")
plt.hist2d(I_i, Q_i, bins=101, range=[[-lim, lim],[-lim, lim]])
plt.colorbar()
plt.axes().set_aspect('equal')
plt.figure("I-Q+")
plt.hist2d(I_m, Q_p, bins=101, range=[[-lim, lim],[-lim, lim]])
plt.colorbar()
plt.axes().set_aspect('equal')
plt.figure("I+Q-")
plt.hist2d(I_p, Q_m, bins=101, range=[[-lim, lim],[-lim, lim]])
plt.colorbar()
plt.axes().set_aspect('equal')


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Feedback Processing<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#g_i=5530
#g_q=4000
#g_r=2000
#posi_g_0=[]
#n_g_0=0
#posi_g_1=[]
#n_g_1=0
#
#e_i=6165
#e_q=-1204
#e_r=2000
#posi_e_0=[]
#n_e_0=0
#posi_e_1=[]
#n_e_1=0
#
#f_i=3897
#f_q=-4783
#f_r=2000
#posi_f_0=[]
#n_f_0=0
#posi_f_1=[]
#n_f_1=0
#
#for i in range(len(I_data_0)):
#    if np.sqrt((I_data_0[i]-g_i)**2+ (Q_data_0[i]-g_q)**2)< g_r :
#        posi_g_0.append(i)
#        n_g_0+=1
#    elif np.sqrt((I_data_0[i]-e_i)**2+ (Q_data_0[i]-e_q)**2)< e_r :
#        posi_e_0.append(i)
#        n_e_0+=1
#    elif np.sqrt((I_data_0[i]-f_i)**2+ (Q_data_0[i]-f_q)**2)< f_r :
#        posi_f_0.append(i)
#        n_f_0+=1
#
#for i in range(len(I_data_1)):
#    if np.sqrt((I_data_1[i]-g_i)**2+ (Q_data_1[i]-g_q)**2)< g_r :
#        posi_g_1.append(i)
#        n_g_1+=1
#    elif np.sqrt((I_data_1[i]-e_i)**2+ (Q_data_1[i]-e_q)**2)< e_r :
#        posi_e_1.append(i)
#        n_e_1+=1
#    elif np.sqrt((I_data_1[i]-f_i)**2+ (Q_data_1[i]-f_q)**2)< f_r :
#        posi_f_1.append(i)
#        n_f_1+=1
#
#
#plt.figure("g sel")
#plt.hist2d(I_data_0[posi_g_0], Q_data_0[posi_g_0], bins=101, range=[[-lim, lim],[-lim, lim]])
#plt.figure("e sel")
#plt.hist2d(I_data_0[posi_e_0], Q_data_0[posi_e_0], bins=101, range=[[-lim, lim],[-lim, lim]])
#plt.figure("f sel")
#plt.hist2d(I_data_0[posi_f_0], Q_data_0[posi_f_0], bins=101, range=[[-lim, lim],[-lim, lim]])
#
#plt.figure("g sel 1")
#plt.hist2d(I_data_1[posi_g_1], Q_data_1[posi_g_1], bins=101, range=[[-lim, lim],[-lim, lim]])
#plt.figure("e sel 1")
#plt.hist2d(I_data_1[posi_e_1], Q_data_1[posi_e_1], bins=101, range=[[-lim, lim],[-lim, lim]])
#plt.figure("f sel 1")
#plt.hist2d(I_data_1[posi_f_1], Q_data_1[posi_f_1], bins=101, range=[[-lim, lim],[-lim, lim]])
#
#n_0= n_g_0+n_f_0+n_e_0
#n_1= n_g_1+n_f_1+n_e_1
#
#print 
#
#fig, (ax1,ax2) = plt.subplots(1, 2)
#ax1.hist2d(I_data_0, Q_data_0, bins=101, range=[[-lim, lim],[-lim, lim]])
#ax2.hist2d(I_data_1, Q_data_1, bins=101, range=[[-lim, lim],[-lim, lim]])
#plt.show()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
