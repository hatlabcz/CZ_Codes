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
#plt.close('all')
N1 = 3
N2 = 3
N3 = 3 

p_bar = qt.ui.TextProgressBar()
opts =  qt.Options(nsteps=1e5)
xvec = np.linspace(-5, 5, 101)

DES_A = qt.destroy(N1)
CRE_A = qt.create(N1)
IDEN_A = qt.identity(N1)

DES_B = qt.destroy(N2)
CRE_B = qt.create(N2)
IDEN_B = qt.identity(N2)

DES_C = qt.destroy(N3)
CRE_C = qt.create(N3)
IDEN_C = qt.identity(N3)


A0 = qt.tensor(DES_A, IDEN_B)
A  = qt.tensor(A0, IDEN_C)
A_DAG = A.dag()

B0 = qt.tensor(IDEN_A, DES_B)
B  = qt.tensor(B0, IDEN_C)
B_DAG = B.dag()

C0 = qt.tensor(IDEN_A, IDEN_B)
C  = qt.tensor(C0, DES_C)
C_DAG = C.dag()


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
    ax1.set_title('Mode a')
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
    ax2.set_title('Mode b')
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
    
def master_equation(hamil_, psi0_, tlist_, decay_op, plot=1, wigner=0):
    result = qt.mesolve(hamil_, psi0_, tlist_, [decay_op], [], 
                        options=opts, progress_bar=p_bar)
    num1_list = np.zeros(len(tlist_))    
    num2_list = np.zeros(len(tlist_))    
#    num3_list = np.zeros(len(tlist_))     
    energy_list = np.zeros(len(tlist_))
    #fock1_list = np.zeros(len(tlist_))    
    #fock2_list = np.zeros(len(tlist_))    
    wa_list = []
    wb_list = []
    for i in range(len(tlist_)):
        psi_t_temp = result.states[i]
        num1_list[i] = qt.expect(A_DAG * A, psi_t_temp)
        num2_list[i] = qt.expect(B_DAG * B, psi_t_temp)
#        num3_list[i] = qt.expect(C_DAG * C, psi_t_temp)
#        energy_list[i] = num1_list[i] * OA + num2_list[i] * OB
        #fock1_list[i] = qt.fidelity(psi_t_temp, fock1)
        #fock2_list[i] = qt.fidelity(psi_t_temp, fock2)
        if wigner:
            wa_list.append(qt.wigner(psi_t_temp.ptrace(0), xvec, xvec, g=2.0))
            wb_list.append(qt.wigner(psi_t_temp.ptrace(1), xvec, xvec, g=2.0))
    if wigner:
        plot_slider(wa_list, wb_list, len(tlist_)-1)
        
    if plot: 
        plt.figure()
        plt.plot(tlist_, num1_list, label='JPC A')
        plt.plot(tlist_, num2_list, label='JPC B')
#        plt.plot(tlist_, num3_list, label='JPC C')
        #plt.plot(tlist_, fock1_list**2, label='|1>')
        #plt.plot(tlist_, fock2_list**2, label='|2>')
        plt.legend()
        plt.show()
#        plt.figure()
#        plt.plot(tlist_, energy_list)
    return result
#===================================================
    
#===============Parameters=============
OA = 7.0 * 2.0 * np.pi
OB = 5.0 * 2.0 * np.pi
OC = 6.0 * 2.0 * np.pi

OP_JPC = 2 * 2.0 * np.pi

phase=np.pi/4
pump_jpc_amp =  (OC**2-OP_JPC**2)/(2*OC)*np.exp(1j* phase)

g = 0.1 * 2.0 * np.pi

kappa=0.00 * 2.0 * np.pi
#===============Parameters=============

#======Time-Depedent Parameters========
def pump_c1(t, args):
    return pump_c1_amp * (np.exp(-1j * OP_C1 * t) \
           + np.exp(1j * OP_C1 * t))  

def pump_jpc(t, args):
    return pump_jpc_amp * np.exp(-1j * OP_JPC * t) \
           + pump_jpc_amp.conj() * np.exp(1j * OP_JPC * t)
#======Time-Depedent Parameters=========

#=============Hamiltonians=============
HAMIL_TI = OA * A_DAG * A + OB * B_DAG * B + OC * C_DAG * C + g * (A_DAG + A) * (B_DAG + B) * (C_DAG + C)
decay_op=np.sqrt(kappa) * C
HAMIL_DRIVE = (C + C_DAG)
#=============Hamiltonians=============


#=========Simplified-Hamiltonians======

HAMIL = [HAMIL_TI, [HAMIL_DRIVE,pump_jpc]]   # for time depedent hamiltonian 


#def g_shift_plus(t, args):
#    return np.exp(1j * (OA - OB) * t)
#def g_shift_minus(t, args):
#    return np.exp(1j * (OB - OA) * t)
#    
#HAMIL_CHAO = OA * A_DAG * A + OB * B_DAG * B + g * (A_DAG * B + A * B_DAG)
#HAMIL_SHIFT_CHAO = [[g * A_DAG * B, g_shift_plus], [g * A * B_DAG, g_shift_minus]]

PSI0 = qt.tensor(qt.fock(N1, 1), qt.fock(N2, 0))
PSI  = qt.tensor(PSI0, qt.fock(N3, 0))
TLIST = np.linspace(0, 100, 501)

master_equation(HAMIL, PSI, TLIST,decay_op, wigner=1)







