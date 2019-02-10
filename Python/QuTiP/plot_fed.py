#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:53:58 2019

@author: hatlab
"""
import qutip
#import numpy as np

import qutip as qt
import numpy as np
import h5py
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib as mpl
import time
from matplotlib.widgets import CheckButtons

NA = 2
NB = 2
NC = 2


DES_A = qt.destroy(NA)
CRE_A = qt.create(NA)
IDEN_A = qt.identity(NA)

DES_B = qt.destroy(NB)
CRE_B = qt.create(NB)
IDEN_B = qt.identity(NB)

DES_C = qt.destroy(NC)
CRE_C = qt.create(NC)
IDEN_C = qt.identity(NC)


I0 = qt.tensor(IDEN_A,IDEN_B)
I  = qt.tensor(I0, IDEN_C)
I_DAG = I.dag()

bc11_1 = qt.tensor(qt.fock(NA, 0), qt.fock(NB, 1))
bc11 = qt.tensor(bc11_1, qt.fock(NC, 1))


bc10_1 = qt.tensor(qt.fock(NA, 0), qt.fock(NB, 1))
bc10   = qt.tensor(bc10_1, qt.fock(NC, 0))

bc01_1 = qt.tensor(qt.fock(NA, 0), qt.fock(NB, 0))
bc01 = qt.tensor(bc01_1, qt.fock(NC, 1))

bc00_1 = qt.tensor(qt.fock(NA, 0), qt.fock(NB, 0))
bc00   = qt.tensor(bc00_1, qt.fock(NC, 0))


bell_bc1=(bc00+bc11)/np.sqrt(2)
bell_bc2=(bc00-bc11)/np.sqrt(2)
bell_bc3=(bc01+bc10)/np.sqrt(2)
bell_bc4=(bc01-bc10)/np.sqrt(2)
#bell_bc5=(bc01-1j*bc10)/np.sqrt(2)

#C=

orot=0.2*2*np.pi

def plot_fed(result,TLIST):
    fed_list1 = np.zeros(len(TLIST)) 
    fed_list2 = np.zeros(len(TLIST)) 
    fed_list3 = np.zeros(len(TLIST)) 
    fed_list4 = np.zeros(len(TLIST)) 
#    fed_list5 = np.zeros(len(TLIST)) 
    for i in range(len(TLIST)):
        psi_t_temp = result.states[i]
        bell_bc3 = (bc01+np.exp(1j*orot*TLIST[i])*bc10)/np.sqrt(2)
        
        fed_list1[i] = qt.fidelity(psi_t_temp, bell_bc1*bell_bc1.dag())
        fed_list2[i] = qt.fidelity(psi_t_temp, bell_bc2*bell_bc2.dag())
        fed_list3[i] = qt.fidelity(psi_t_temp, bell_bc3*bell_bc3.dag())
        fed_list4[i] = qt.fidelity(psi_t_temp, bell_bc4*bell_bc4.dag())
#        fed_list5[i] = qt.fidelity(psi_t_temp, bell_bc5*bell_bc5.dag())
        
            
    plt.figure()
#    plt.plot(TLIST, fed_list1, label='|00>+|11>')
#    plt.plot(TLIST, fed_list2, label='|00>-|11>')
    plt.plot(TLIST, fed_list3)
#    plt.plot(TLIST, fed_list4, label='|01>-<10|')
#    plt.plot(TLIST, fed_list5, label='|01>-i<10|')
    
#    plt.legend()
    plt.show()


filename="3mode_fed_nonRot"
result = qt.qload(filename)
TLIST=result.times
plot_fed(result,TLIST)