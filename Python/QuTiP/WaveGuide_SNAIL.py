# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:26:51 2019

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
ND = 3
NE = 3


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

DES_D = qt.destroy(ND)
CRE_D = qt.create(ND)
IDEN_D = qt.identity(ND)

DES_E = qt.destroy(NE)
CRE_E = qt.create(NE)
IDEN_E = qt.identity(NE)


A0 = qt.tensor(DES_A, IDEN_B)
A1 = qt.tensor(A0, IDEN_C)
A2 = qt.tensor(A1, IDEN_D)
A = qt.tensor(A2, IDEN_E)
A_DAG = A.dag()

B0 = qt.tensor(IDEN_A, DES_B)
B1 = qt.tensor(B0, IDEN_C)
B2 = qt.tensor(B1, IDEN_D)
B = qt.tensor(B2, IDEN_E)
B_DAG = B.dag()


C0 = qt.tensor(IDEN_A,IDEN_B)
C1 = qt.tensor(C0, DES_C)
C2 = qt.tensor(C1, IDEN_D)
C = qt.tensor(C2, IDEN_E)
C_DAG = C.dag()


D0 = qt.tensor(IDEN_A,IDEN_B)
D1 = qt.tensor(D0, IDEN_C)
D2 = qt.tensor(D1, DES_D)
D = qt.tensor(D2, IDEN_E)
D_DAG = D.dag()


E0 = qt.tensor(IDEN_A,IDEN_B)
E1 = qt.tensor(E0, IDEN_C)
E2 = qt.tensor(E1, IDEN_D)
E = qt.tensor(E2, DES_E)
E_DAG = E.dag()





def plot_slider(qa_list, qb_list, qc_list, qd_list, qe_list, length):
    fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(1, 5, figsize=(25,5))
    
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
    pc4 = ax4.pcolormesh(qd_list[0], cmap='seismic', 
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

    plt.sca(ax5)
    pc5 = ax5.pcolormesh(qe_list[0], cmap='seismic', 
                         norm=mpl.colors.Normalize(vmin=-0.5, vmax=0.5))
    ax5.set_xlabel('Re($\\alpha$)')
    ax5.set_ylabel('Im($\\alpha$)')
    x_labels = np.arange(-5,6,1)
    y_labels = np.arange(-5,6,1)
    x_loc = np.linspace(0,100,11)
    y_loc = np.linspace(0,100,11)
    plt.xticks(np.array(x_loc),x_labels)
    plt.yticks(np.array(y_loc),y_labels)
    ax5.set_title('Mode e')
    plt.grid(True)    

    
    fig.colorbar(pc1,ax=ax1)
    fig.colorbar(pc2,ax=ax2)
    fig.colorbar(pc3,ax=ax3)
    fig.colorbar(pc4,ax=ax4)
    fig.colorbar(pc5,ax=ax5)
    
    def update(val):
       int_val = int(val)
       if (slider.val != int_val):
           slider.set_val(int_val)
       pc1.set_array(qa_list[int_val].ravel())
       pc2.set_array(qb_list[int_val].ravel())
       pc3.set_array(qc_list[int_val].ravel())
       pc4.set_array(qd_list[int_val].ravel())
       pc5.set_array(qe_list[int_val].ravel())
       
       
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
    num5_list = np.zeros(len(tlist_))    
    wa_list = []
    wb_list = []
    wc_list = []
    wd_list = []
    we_list = []
    for i in range(len(tlist_)):
        psi_t_temp = result.states[i]
        num1_list[i] = qt.expect( A_DAG * A, psi_t_temp)
        num2_list[i] = qt.expect( B_DAG * B, psi_t_temp)
        num3_list[i] = qt.expect( C_DAG * C, psi_t_temp)
        num4_list[i] = qt.expect( D_DAG * D, psi_t_temp)
        num5_list[i] = qt.expect( E_DAG * E, psi_t_temp)
        if wigner:
            wa_list.append(qt.wigner(psi_t_temp.ptrace(0), xvec, xvec, g=2.0))
            wb_list.append(qt.wigner(psi_t_temp.ptrace(1), xvec, xvec, g=2.0))
            wc_list.append(qt.wigner(psi_t_temp.ptrace(2), xvec, xvec, g=2.0))
            wd_list.append(qt.wigner(psi_t_temp.ptrace(3), xvec, xvec, g=2.0))
            we_list.append(qt.wigner(psi_t_temp.ptrace(4), xvec, xvec, g=2.0))
    if wigner:
        plot_slider(wa_list, wb_list,wc_list, wd_list,we_list,len(tlist_)-1)
        
    if plot:
        
        fig, ax = plt.subplots()
        l1, = ax.plot(tlist_, num1_list, label='A')
        l2, = ax.plot(tlist_, num2_list, label='B')
        l3, = ax.plot(tlist_, num3_list, label='C')
        l4, = ax.plot(tlist_, num4_list, label='D')
        l5, = ax.plot(tlist_, num5_list, label='E')
        ax.legend()
        plt.subplots_adjust(left=0.3)
        
        lines = [l1, l2, l3, l4, l5]
        
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
OB = OA+  0.1 * 2.0 * np.pi
OC = OB+  0.2 * 2.0 * np.pi
OD = OC+  0.4 * 2.0 * np.pi
OE = OD+  0.5 * 2.0 * np.pi

OP =0.2 * 2.0 * np.pi
OP2 =0.5 * 2.0 * np.pi
pump_amp = 0.02 * 2.0 * np.pi

g = 0.01 * 2.0 * np.pi

#kappa=0.005 * 2.0 * np.pi
#===============Parameters=============

#======Time-Depedent Parameters========

def pump(t, args):
    return pump_amp * (np.exp(-1j * OP * t) \
           + np.exp(1j * OP * t))
           
def pump2(t, args):
    return pump_amp * (np.exp(-1j * OP * t) \
           + np.exp(1j * OP * t))+\
           pump_amp * (np.exp(-1j * OP2 * t) \
           + np.exp(1j * OP2 * t))        
#======Time-Depedent Parameters=========

#=============Hamiltonians=============
HAMIL_TI = OA * A_DAG * A + OB * B_DAG * B + OC * C_DAG * C + OD * D_DAG * D + OE * E_DAG * E 
            
HAMIL_COUP = g * (  A * B_DAG  + A_DAG * B  +\
                    A * C_DAG  + A_DAG * C  +\
                    A * D_DAG  + A_DAG * D  +\
                    A * E_DAG  + A_DAG * E  +\
                    B * C_DAG  + B_DAG * C  +\
                    B * D_DAG  + B_DAG * D  +\
                    B * E_DAG  + B_DAG * E  +\
                    C * D_DAG  + C_DAG * D  +\
                    C * E_DAG  + C_DAG * E  +\
                    D * E_DAG  + D_DAG * E   \
                ) 
                

decay_op=[]#np.sqrt(kappa) * C1
#=============Hamiltonians=============


#=========Simplified-Hamiltonians======

HAMIL = [HAMIL_TI, [HAMIL_COUP, pump2]]   # for time depedent hamiltonian 


PSI0 = qt.tensor(qt.fock(NA, 0), qt.fock(NB, 0))
PSI1 = qt.tensor(PSI0, qt.fock(NC, 1))
PSI2 = qt.tensor(PSI1, qt.fock(ND, 0))
PSI = qt.tensor(PSI2, qt.fock(NE, 1))

TLIST = np.linspace(0, 400, 201)

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




