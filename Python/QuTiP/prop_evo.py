# -*- coding: utf-8 -*-
"""
Created on Fri Jan 04 14:26:51 2019

@author: zc
"""
import qutip
import numpy as np

import qutip as qt
import numpy as np
import h5py
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib as mpl
import time

#===============Initialize============================
start_t=time.time()
plt.close('all')
N1 = 10
N2 = 10
NC1 = 10
NC2 = 10

p_bar = qt.ui.TextProgressBar()
opts =  qt.Options(nsteps=1e5)
xvec = np.linspace(-5, 5, 101)

DES_A = qt.destroy(N1)
CRE_A = qt.create(N1)
IDEN_A = qt.identity(N1)

DES_B = qt.destroy(N2)
CRE_B = qt.create(N2)
IDEN_B = qt.identity(N2)

DES_C1 = qt.destroy(NC1)
CRE_C1 = qt.create(NC1)
IDEN_C1 = qt.identity(NC1)

DES_C2 = qt.destroy(NC2)
CRE_C2 = qt.create(NC2)
IDEN_C2 = qt.identity(NC2)

A0 = qt.tensor(IDEN_C1, DES_A)
A1 = qt.tensor(A0, IDEN_B)
A  = qt.tensor(A1, IDEN_C2)
A_DAG = A.dag()

B0 = qt.tensor(IDEN_C1, IDEN_A)
B1 = qt.tensor(B0, DES_B)
B  = qt.tensor(B1, IDEN_C2)
B_DAG = B.dag()

C10 = qt.tensor(DES_C1, IDEN_A)
C11 = qt.tensor(C10, IDEN_B)
C1  = qt.tensor(C11, IDEN_C2)
C1_DAG = C1.dag()

C20 = qt.tensor(IDEN_C1, IDEN_A)
C21 = qt.tensor(C20, IDEN_B)
C2  = qt.tensor(C21, DES_C2)
C2_DAG = C2.dag()


def plot_slider(qa_list, qb_list, length):
    fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(12,5))
    pc1 = ax1.pcolormesh(qa_list[0], cmap='seismic', 
                         norm=mpl.colors.Normalize(vmin=-0.5, vmax=0.5))
    plt.sca(ax1)
    ax1.set_xlabel('Re($\\alpha$)')
    ax1.set_ylabel('Im($\\alpha$)')
    x_labels = np.arange(-5,6,1)
    y_labels = np.arange(-5,6,1)
    x_loc = np.linspace(0,100,11)
    y_loc = np.linspace(0,100,11)
    plt.xticks(np.array(x_loc),x_labels)
    plt.yticks(np.array(y_loc),y_labels)
    ax1.set_title('Cavity 1')
    plt.grid(True)

    plt.sca(ax2)
    pc2 = ax2.pcolormesh(qb_list[0], cmap='seismic', 
                         norm=mpl.colors.Normalize(vmin=-0.5, vmax=0.5))
    ax2.set_xlabel('Re($\\alpha$)')
    ax2.set_ylabel('Im($\\alpha$)')
    x_labels = np.arange(-5,6,1)
    y_labels = np.arange(-5,6,1)
    x_loc = np.linspace(0,100,11)
    y_loc = np.linspace(0,100,11)
    plt.xticks(np.array(x_loc),x_labels)
    plt.yticks(np.array(y_loc),y_labels)
    ax2.set_title('Cavity 2')
    plt.grid(True)
    fig.colorbar(pc1,ax=ax1)
    fig.colorbar(pc2,ax=ax2)

    def update(val):
       int_val = int(val)
       if (slider.val != int_val):
           slider.set_val(int_val)
       pc1.set_array(qa_list[int_val].ravel())
       pc2.set_array(qb_list[int_val].ravel())

    slider_axes = plt.axes([0.2, 0.95, 0.65, 0.03])
    slider = Slider(slider_axes, "time", 0, length, valinit=30)
    slider.on_changed(update)
    plt.show()
    
def propagator_evolution_one_time(hamil_, psi_0, time_, wigner=0):
    T = 1.
    wa_list = []
    wb_list = []
    
    if int(time_ % T) is not 0:
        print time_ % T 
        raise NameError("Time not compatible")
    order = int(time_ // T)
    u_prop = qt.propagator(hamil_, T, options=opts)
    rho0 = psi_0 * psi_0.dag()
    psi_t_temp = (u_prop)**order * rho0 * (u_prop.dag())**order
    if wigner:
        wa_list.append(qt.wigner(psi_t_temp.ptrace(0), xvec, xvec, g=2.0))
        wb_list.append(qt.wigner(psi_t_temp.ptrace(3), xvec, xvec, g=2.0))
    #print qt.fidelity(psi_t_temp, A_DAG*A)
    return wa_list,wb_list
#===================================================
    
#===============Parameters=============
OA = 7.0 * 2.0 * np.pi
OC1 = OA
OB = 5.0 * 2.0 * np.pi
OC2 = OB

OP_JPC_1 =OA - OB
OP_JPC_2 =OA + OB


OP_C1=OC1
pump_c1_amp = 1/3.
pump_jpc_amp_1 = 1/3.
pump_jpc_amp_2 = 1/3.
gCJ1 = 0.1 * 2.0 * np.pi
gCJ2 = 0.1* 2.0 * np.pi


theta=3*np.pi/4.
g_1 = 0.1 * 2.0 * np.pi * np.exp(1j * theta)

g_2 = 0.1 * 2.0 * np.pi * np.exp(1j * 0)

kappa=0.000 * 2.0 * np.pi
decay_op=np.sqrt(kappa) * C1
#===============Parameters=============

#======Time-Depedent Parameters========
def pump_c1(t, args):
    return pump_c1_amp * (np.exp(-1j * OP_C1 * t) \
           + np.exp(1j * OP_C1 * t))  

def pump_jpc_1(t, args):
#    return (np.heaviside(t,1) + np.heaviside(24.25-t,1)-1) * pump_jpc_amp_1 * (np.exp(-1j * OP_JPC_1 * t) \
#           + np.exp(1j * OP_JPC_1 * t))
    return pump_jpc_amp_1 * (np.exp(-1j * OP_JPC_1 * t) \
           + np.exp(1j * OP_JPC_1 * t))

def pump_jpc_2(t, args):
    return pump_jpc_amp_2 * (np.exp(-1j * OP_JPC_2 * t) \
           + np.exp(1j * OP_JPC_2 * t))
#======Time-Depedent Parameters=========

#=============Hamiltonians=============
HAMIL_TI = OA * A_DAG * A + OB * B_DAG * B + OC1 * C1_DAG * C1 + OC2 * C2_DAG * C2 + gCJ1 * (C1_DAG * A + C1 * A_DAG) + gCJ2 * (C2_DAG * B + C2 * B_DAG)
HAMIL_JPC_1 = g_1 * A_DAG * B + g_1.conj() * A * B_DAG
HAMIL_JPC_2 = g_2 * A * B + g_2.conj() * A_DAG * B_DAG
decay_op = [np.sqrt(kappa) * C1 , np.sqrt(kappa) * C2]
#HAMIL_DRIVE = (C1 + C1_DAG)
#HAMIL_USE = g * (A+A_DAG)**2 * (B+B_DAG)
#HAMIL_KERR =  HAMIL_TI + g/10. * ((A_DAG * A)**2 + (B_DAG * B)**2 + A_DAG  * A * B_DAG * B)
#=============Hamiltonians=============


#=========Simplified-Hamiltonians======

#HAMIL = [HAMIL_TI, [HAMIL_JPC_1, pump_jpc_1],[HAMIL_JPC_2, pump_jpc_2]]   # for time depedent hamiltonian 
HAMIL = [HAMIL_TI, [HAMIL_JPC_1, pump_jpc_1]]   # for time depedent hamiltonian 
#HAMIL = [HAMIL_TI, [HAMIL_OSC, pump_jpc],[HAMIL_DRIVE,pump_c1]]   # for time depedent hamiltonian 





def g_shift_plus(t, args):
    return np.exp(1j * (OA - OB) * t)
def g_shift_minus(t, args):
    return np.exp(1j * (OB - OA) * t)
    
    
#HAMIL_CHAO = OA * A_DAG * A + OB * B_DAG * B + g * (A_DAG * B + A * B_DAG)
#HAMIL_SHIFT_CHAO = [[g * A_DAG * B, g_shift_plus], [g * A * B_DAG, g_shift_minus]]

PSI0 = qt.tensor(qt.coherent(N1, 2), qt.coherent(N1, 0))
PSI1 = qt.tensor(PSI0, qt.coherent(N2, 0))
PSI = qt.tensor(PSI1, qt.coherent(NC2, 0))
TLIST = np.linspace(0, 30, 301)

wa_list,wb_list=propagator_evolution_one_time(HAMIL, PSI, 15, wigner=1)
plot_slider(wa_list, wb_list, 1)
print time.time()-start_t



