# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:26:52 2019

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
from matplotlib.widgets import CheckButtons
#===============Initialize============================
plt.close('all')
NA = 3
NB = 3
NC = 3
NP = 3


p_bar = qt.ui.TextProgressBar()
opts =  qt.Options(nsteps=1e5)
xvec = np.linspace(-5, 5, 101)

DES_A = qt.destroy(NA)
CRE_A = qt.create(NA)
IDEN_A = qt.identity(NA)

DES_B = qt.destroy(NB)
CRE_B = qt.create(NB)
IDEN_B = qt.identity(NB)

DES_C = qt.destroy(NC)
CRE_C = qt.create(NC)
IDEN_C = qt.identity(NC)

DES_P = qt.destroy(NP)
CRE_P = qt.create(NP)
IDEN_P = qt.identity(NP)


A0 = qt.tensor(DES_A, IDEN_B)
A1 = qt.tensor(A0, IDEN_C)
A  = qt.tensor(A1, IDEN_P)
A_DAG = A.dag()

B0 = qt.tensor(IDEN_A, DES_B)
B1 = qt.tensor(B0, IDEN_C)
B = qt.tensor(B1, IDEN_P)
B_DAG = B.dag()


C0 = qt.tensor(IDEN_A,IDEN_B)
C1 = qt.tensor(C0, DES_C)
C  = qt.tensor(C1, IDEN_P)
C_DAG = C.dag()


P0 = qt.tensor(IDEN_A,IDEN_B)
P1 = qt.tensor(P0, IDEN_C)
P  = qt.tensor(P1, DES_P)
P_DAG = P.dag()



def plot_slider(qa_list, qb_list, qc_list, qp_list, length):
    fig, (ax1,ax2,ax3,ax4) = plt.subplots(1, 4, figsize=(20,5))
    
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
    
    plt.sca(ax3)
    pc3 = ax3.pcolormesh(qc_list[0], cmap='seismic', 
                         norm=mpl.colors.Normalize(vmin=-0.5, vmax=0.5))
    ax3.set_xlabel('Re($\\alpha$)')
    ax3.set_ylabel('Im($\\alpha$)')
    x_labels = np.arange(-5,6,1)
    y_labels = np.arange(-5,6,1)
    x_loc = np.linspace(0,100,11)
    y_loc = np.linspace(0,100,11)
    plt.xticks(np.array(x_loc),x_labels)
    plt.yticks(np.array(y_loc),y_labels)
    ax3.set_title('Mode c')
    plt.grid(True)
    
    
    plt.sca(ax4)
    pc4 = ax4.pcolormesh(qp_list[0], cmap='seismic', 
                         norm=mpl.colors.Normalize(vmin=-0.5, vmax=0.5))
    ax4.set_xlabel('Re($\\alpha$)')
    ax4.set_ylabel('Im($\\alpha$)')
    x_labels = np.arange(-5,6,1)
    y_labels = np.arange(-5,6,1)
    x_loc = np.linspace(0,100,11)
    y_loc = np.linspace(0,100,11)
    plt.xticks(np.array(x_loc),x_labels)
    plt.yticks(np.array(y_loc),y_labels)
    ax4.set_title('Mode d')
    plt.grid(True)
    
    def update(val):
       int_val = int(val)
       if (slider.val != int_val):
           slider.set_val(int_val)
       pc1.set_array(qa_list[int_val].ravel())
       pc2.set_array(qb_list[int_val].ravel())
       pc3.set_array(qc_list[int_val].ravel())
       pc4.set_array(qp_list[int_val].ravel())
       
       
    slider_axes = plt.axes([0.2, 0.95, 0.65, 0.03])
    slider = Slider(slider_axes, "time", 0, length, valinit=30)
    slider.on_changed(update)
    plt.show()
    
def master_equation(hamil_, psi0_, tlist_, decay_op, plot=1, wigner=0):
    result = qt.mesolve(hamil_, psi0_, tlist_, decay_op, [], 
                        options=opts, progress_bar=p_bar)
    num1_list = np.zeros(len(tlist_))    
    num2_list = np.zeros(len(tlist_))    
    num3_list = np.zeros(len(tlist_))    
    num4_list = np.zeros(len(tlist_)) 
    wa_list = []
    wb_list = []
    wc_list = []
    wp_list = []
    for i in range(len(tlist_)):
        psi_t_temp = result.states[i]
        num1_list[i] = qt.expect( A_DAG * A, psi_t_temp)
        num2_list[i] = qt.expect( B_DAG * B, psi_t_temp)
        num3_list[i] = qt.expect( C_DAG * C, psi_t_temp)
        num4_list[i] = qt.expect( P_DAG * P, psi_t_temp)
        if wigner:
            wa_list.append(qt.wigner(psi_t_temp.ptrace(0), xvec, xvec, g=2.0))
            wb_list.append(qt.wigner(psi_t_temp.ptrace(1), xvec, xvec, g=2.0))
            wc_list.append(qt.wigner(psi_t_temp.ptrace(2), xvec, xvec, g=2.0))
            wp_list.append(qt.wigner(psi_t_temp.ptrace(3), xvec, xvec, g=2.0))
    if wigner:
        plot_slider(wa_list, wb_list,wc_list, wp_list, len(tlist_)-1)
        
    if plot:
        
        fig, ax = plt.subplots()
        l1, = ax.plot(tlist_, num1_list, label='A')
        l2, = ax.plot(tlist_, num2_list, label='B')
        l3, = ax.plot(tlist_, num3_list, label='C')
        l4, = ax.plot(tlist_, num4_list, label='P')
        ax.legend()
        plt.subplots_adjust(left=0.3)
        
        lines = [l1, l2, l3, l4]
        
#        plt.figure()
#        plt.plot(tlist_, num1_list, label='A')
#        plt.plot(tlist_, num2_list, label='B')
#        plt.plot(tlist_, num3_list, label='C')
#        plt.plot(tlist_, num4_list, label='D')
#        plt.plot(tlist_, num5_list, label='E')
#        plt.legend()
#        plt.show()

    return lines
#===================================================
    
#===============Parameters=============
OA = 7.0 * 2.0 * np.pi
OB = OA + 0.1 * 2.0 * np.pi
OC = OB +  0.2 * 2.0 * np.pi

OP = 0.2 * 2.0 * np.pi
OP2 = 0.5 * 2.0 * np.pi
pump_amp = 1 

g = 0.0005 * 2.0 * np.pi

#kappa=0.005 * 2.0 * np.pi
#===============Parameters=============

#======Time-Depedent Parameters========

def pump(t, args):
    return pump_amp * (np.exp(-1j * OP * t) \
           + np.exp(1j * OP * t))

def pump_temp1(t, args):
    return pump_amp * np.exp(-1j * 2*OP * t)
    
def pump_temp2(t, args):
    return pump_amp * np.exp(1j * 2*OP * t)
           
def pump2(t, args):
    return pump_amp * (np.exp(-1j * OP * t) \
           + np.exp(1j * OP * t))+\
           pump_amp * (np.exp(-1j * OP2 * t) \
           + np.exp(1j * OP2 * t))
           
#======Time-Depedent Parameters=========

#=============Hamiltonians=============
HAMIL_TI = OA * A_DAG * A + OB * B_DAG * B + OC * C_DAG * C 

HAMIL_COUP = g * (A + B + C + A_DAG + B_DAG + C_DAG)**2


decay_op=[]#np.sqrt(kappa) * C1
#=============Hamiltonians=============


#=========Simplified-Hamiltonians======

HAMIL = [HAMIL_TI, [HAMIL_COUP, pump]]   # for time depedent hamiltonian 


PSI0 = qt.tensor(qt.fock(NA, 1), qt.fock(NB, 0))
PSI1 = qt.tensor(PSI0, qt.fock(NC, 1))
PSI  = qt.tensor(PSI1, qt.fock(NP, 0))

TLIST = np.linspace(0, 400, 2001)

lines=master_equation(HAMIL, PSI, TLIST,decay_op, wigner=0)



rax = plt.axes([0.05, 0.4, 0.2, 0.25])
labels = [str(line.get_label()) for line in lines]
visibility = [line.get_visible() for line in lines]
check = CheckButtons(rax, labels, visibility)
def func(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()
    
check.on_clicked(func)
plt.show()




