# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:25:51 2018

Hamiltonian Evolution 
@author: Hat_Pinlei
"""

import qutip as qt
import numpy as np
import h5py
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib as mpl
import time
import HamiltonianEvolution_module as HM

#===============Constant===============
plt.close('all')
N1 = 8
N2 = 8
p_bar = qt.ui.TextProgressBar()
opts =  qt.Options(nsteps=1e5)
xvec = np.linspace(-5, 5, 101)

DES_A = qt.destroy(N1)
CRE_A = qt.create(N1)
IDEN_A = qt.identity(N1)

DES_B = qt.destroy(N2)
CRE_B = qt.create(N2)
IDEN_B = qt.identity(N2)

A = qt.tensor(DES_A, IDEN_B)
A_DAG = qt.tensor(CRE_A, IDEN_B)
B = qt.tensor(IDEN_A, DES_B)
B_DAG = qt.tensor(IDEN_A, CRE_B)
IDEN = qt.tensor(IDEN_A, IDEN_B)

fock0 = qt.tensor(qt.fock(N1, 0), qt.coherent(N2,0))
fock1 = qt.tensor(qt.fock(N1, 1), qt.coherent(N2,0))
fock2 = qt.tensor(qt.fock(N1, 2), qt.coherent(N2,0))
#===============Constant===============

#===============Parameters=============
OA = 7.0 * 2.0 * np.pi
OD = OA #9.0 * 2.0  * np.pi
OB = 5.0 * 2.0 * np.pi
OPA = 2 * 2.0 * np.pi
OPC = 17 * 2.0 * np.pi
drive_a_amp = 1 * 1e-3 * 2.0 * np.pi
eta = (OPA**2/4. - OA**2) / (2*OA) / (2*np.pi)
z = eta * (2*OA) / (OPA**2 - OA**2)
pump_a_amp = eta #(OA**2 - OPA**2) / (2*OA)
pump_c_amp = 1/3.
g = 0.01 * 2.0 * np.pi
g3 = 200 * 1e-3 * 2.0 * np.pi
kappa_a = 0.05 * 1e-3 * 2.0 * np.pi
kappa_b = 50 * 1e-3 * 2.0 * np.pi
#===============Parameters=============

#======Time-Depedent Parameters========
def drive_a(t, args):
    return drive_a_amp * (np.exp(-1j * OD * t) \
           + np.exp(1j * OD * t))

def pump_a(t, args):
    return pump_a_amp * (np.exp(-1j * OPA * t) \
           + np.exp(1j * OPA * t))  

def pump_c(t, args):
    return pump_c_amp * (np.exp(-1j * OPC * t) \
           + np.exp(1j * OPC * t))
#======Time-Depedent Parameters=========

#z = pump_a_amp/(OPA - OA) + pump_a_amp/(- OPA - OA)
DISPLACE = qt.tensor(qt.displace(N1, z), IDEN_B) #Displacement
E0 = (1 - kappa_a * A_DAG * A).sqrtm()
E1 = np.sqrt(kappa_a) * A
E2 = (1 - kappa_b * B_DAG * B).sqrtm()
E3 = np.sqrt(kappa_b) * B

#=============Hamiltonians=============
HAMIL_TI = OA * A_DAG * A + OB * B_DAG * B
HAMIL_T = g * (A + A_DAG)**3 * (B + B_DAG)
HAMIL_BAD = 24 * g * (A + A_DAG) * (B + B_DAG)
HAMIL_DRIVE = (A + A_DAG)
HAMIL_USE = g * (A+A_DAG)**2 * (B+B_DAG)
HAMIL_KERR =  HAMIL_TI + g/10. * ((A_DAG * A)**2 + (B_DAG * B)**2 + A_DAG * A * B_DAG * B)
#=============Hamiltonians=============

#===========SHIFT-Hamiltonians=========
def shift_pump(t, args):
    return drive_a_amp * (np.exp(-1j * OPA * t) + np.exp(1j * OPA * t)) \
            * (np.exp(-1j * OPC * t) + np.exp(1j * OPC * t))

def shift_pump_1(t,args):
    return 1/3. * (np.exp(-1j * OPC * t) + np.exp(1j * OPC * t))
def shift_pump_2(t,args):
    return (np.exp(-1j * OPA * t) + np.exp(1j * OPA * t)) * \
           1/3. * (np.exp(-1j * OPC * t) + np.exp(1j * OPC * t))
def shift_pump_3(t,args):
    return (np.exp(-1j * OPA * t) + np.exp(1j * OPA * t))**2 * \
           1/3. * (np.exp(-1j * OPC * t) + np.exp(1j * OPC * t))
def shift_pump_4(t,args):
    return (np.exp(-1j * OPA * t) + np.exp(1j * OPA * t))**3 * \
           1/3. * (np.exp(-1j * OPC * t) + np.exp(1j * OPC * t))
               
SHIFT_HAMIL_T_1 = g * (A + A_DAG)**3 * (B + B_DAG) # PUMP[C] 
SHIFT_HAMIL_T_2 = g * 3 * (A + A_DAG)**2 * (B + B_DAG) # PUMP[A] * PUMP[C]
SHIFT_HAMIL_T_3 = g * 3 * (A + A_DAG) * (B + B_DAG) # PUMP[A]^2 * PUMP[C]
SHIFT_HAMIL_T_4 = g * (B + B_DAG) # PUMP[A]^3 * PUMP[C]
#===========SHIFT-Hamiltonians=========

#=========Simplified-Hamiltonians======
HAMIL_EASY = g * (A_DAG * A_DAG * B + A * A * B_DAG) + drive_a_amp * (A + A_DAG)
#=========Simplified-Hamiltonians======

HAMIL = [HAMIL_KERR, 
         [HAMIL_T, pump_c],
         [HAMIL_DRIVE, drive_a],
         [HAMIL_DRIVE, pump_a],
         [HAMIL_BAD, pump_c]]

SHIFT_HAMIL = [HAMIL_TI, 
               [SHIFT_HAMIL_T_1, shift_pump_1],
               [SHIFT_HAMIL_T_2, shift_pump_2],
               [SHIFT_HAMIL_T_3, shift_pump_3],
               [SHIFT_HAMIL_T_4, shift_pump_4],
               [HAMIL_DRIVE, drive_a]]

SIM_HAMIL = HAMIL_EASY

def g_shift_plus(t, args):
    return np.exp(1j * (OA - OB) * t)
def g_shift_minus(t, args):
    return np.exp(1j * (OB - OA) * t)
    
    
HAMIL_CHAO = OA * A_DAG * A + OB * B_DAG * B + g * (A_DAG * B + A * B_DAG)
HAMIL_SHIFT_CHAO = [[g * A_DAG * B, g_shift_plus], [g * A * B_DAG, g_shift_minus]]

PSI0 = qt.tensor(qt.coherent(N1, 2), qt.coherent(N2, 0))
TLIST = np.linspace(0, 100, 101)


HM.master_equation(HAMIL_CHAO, PSI0, TLIST, wigner=1)
#HM.floquent_evolution(HAMIL, PSI0, TLIST, wigner=1, displace=DISPLACE.dag())
#HM.floquent_evolution(SIM_HAMIL, PSI0, TLIST, wigner=0)


#result = HM.master_equation(HAMIL, PSI0, TLIST)
#wa_list, wb_list = HM.floquent_evolution(HAMIL, PSI0, TLIST, wigner=0)
#wa_list, wb_list = propagator_evolution(HAMIL, PSI0, TLIST, wigner=0, diss=0)
#plot_slider(wa_list, wb_list, len(TLIST))

#delta = np.linspace(-500, 500, 101)
#fid_list = np.zeros(len(delta))
#for i in range(len(delta)):
#    delta_fre = delta[i] * 1e-3 * 2.0 * np.pi
#    OD = OA + delta_fre
#    print OD/(2.0*np.pi)
#    def drive_a(t, args):
#        return drive_a_amp * (np.exp(-1j * OD * t) \
#               + np.exp(1j * OD * t))
#    HAMIL = [HAMIL_TI, 
#             [HAMIL_T, pump_c],
#             [HAMIL_DRIVE, drive_a],
#             [HAMIL_DRIVE, pump_a]]
#    fid = propagator_evolution_one_time(HAMIL, PSI0, 40)
#    fid_list[i] = fid











