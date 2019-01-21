# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:12:05 2018

@author: Hat_Pinlei
"""

import qutip as qt
import numpy as np
import h5py
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib as mpl
import time


p_bar = qt.ui.TextProgressBar()
opts =  qt.Options(nsteps=1e5)
xvec = np.linspace(-5, 5, 101)
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

print "!!Urgent, N1 and N2 equal", N1, N2, "I don't know how to inherit from different files."


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
    
def master_equation(hamil_, psi0_, tlist_, plot=1, wigner=0):
    result = qt.mesolve(hamil_, psi0_, tlist_, [], [], 
                        options=opts, progress_bar=p_bar)
    num1_list = np.zeros(len(tlist_))    
    num2_list = np.zeros(len(tlist_))    

    #fock1_list = np.zeros(len(tlist_))    
    #fock2_list = np.zeros(len(tlist_))    
    wa_list = []
    wb_list = []
    for i in range(len(tlist_)):
        psi_t_temp = result.states[i]
        num1_list[i] = qt.fidelity(psi_t_temp, A_DAG * A)
        num2_list[i] = qt.fidelity(psi_t_temp, B_DAG * B)
        #fock1_list[i] = qt.fidelity(psi_t_temp, fock1)
        #fock2_list[i] = qt.fidelity(psi_t_temp, fock2)
        if wigner:
            wa_list.append(qt.wigner(psi_t_temp.ptrace(0), xvec, xvec, g=2.0))
            wb_list.append(qt.wigner(psi_t_temp.ptrace(1), xvec, xvec, g=2.0))
    if wigner:
        plot_slider(wa_list, wb_list, len(tlist_)-1)
        
    if plot: 
        plt.figure()
        plt.plot(tlist_, num1_list, label='|0>')
        plt.plot(tlist_, num2_list, label='|0>')

        #plt.plot(tlist_, fock1_list**2, label='|1>')
        #plt.plot(tlist_, fock2_list**2, label='|2>')
        plt.legend()
        plt.show()
    return result

def floquent_evolution(hamil_, psi0_, tlist_, plot=1, wigner=0, displace=IDEN):
    T = 1.
    u_prop = qt.propagator(hamil_, T, options=opts)
    f_modes_0, f_energies = qt.floquet_modes(hamil_, T, U=u_prop)
    f_coeff = qt.floquet_state_decomposition(f_modes_0, f_energies, psi0_)
    fock0_list = np.zeros(len(tlist_))    
    fock1_list = np.zeros(len(tlist_))    
    fock2_list = np.zeros(len(tlist_))    
    wa_list = []
    wb_list = []
    for i in range(len(tlist_)):
        t = tlist_[i]
        psi_t_temp = displace * qt.floquet_wavefunction_t(f_modes_0, f_energies, 
                                               f_coeff, t, hamil_, T)
        fock0_list[i] = qt.fidelity(psi_t_temp, fock0)
        fock1_list[i] = qt.fidelity(psi_t_temp, fock1)
        fock2_list[i] = qt.fidelity(psi_t_temp, fock2)
        if wigner:
            wa_list.append(qt.wigner(psi_t_temp.ptrace(0), xvec, xvec, g=2.0))
            wb_list.append(qt.wigner(psi_t_temp.ptrace(1), xvec, xvec, g=2.0))
    if wigner:
        plot_slider(wa_list, wb_list, len(tlist_)-1)
    if plot: 
        plt.figure()
        plt.plot(tlist_, fock0_list**2, label='|0>')
        plt.plot(tlist_, fock1_list**2, label='|1>')
        plt.plot(tlist_, fock2_list**2, label='|2>')
        plt.legend()
        plt.show()
    return wa_list, wb_list
    
def propagator_evolution(hamil_, psi_0, tlist_, plot=1, wigner=0, diss=0):
    T = 1.
    fock0_list = np.zeros(len(tlist_))    
    fock1_list = np.zeros(len(tlist_))    
    fock2_list = np.zeros(len(tlist_))    
    wa_list = []
    wb_list = []
    
    if int(tlist_[1] % T) is not 0:
        print tlist_[1] % T 
        raise NameError("Time not compatible")
    order = int(tlist_[1] // T)
    u_prop = qt.propagator(hamil_, T, options=opts)
    rho0 = psi_0 * psi_0.dag()
    for i in range(len(tlist_)):
        psi_t_temp = (u_prop)**order * rho0 * (u_prop.dag())**order
        fock0_list[i] = qt.fidelity(psi_t_temp, fock0)
        fock1_list[i] = qt.fidelity(psi_t_temp, fock1)
        fock2_list[i] = qt.fidelity(psi_t_temp, fock2)
        if wigner:
            wa_list.append(qt.wigner(psi_t_temp.ptrace(0), xvec, xvec, g=2.0))
            wb_list.append(qt.wigner(psi_t_temp.ptrace(1), xvec, xvec, g=2.0))
        rho0 = psi_t_temp
        if diss:
            rho0 = E2 * psi_t_temp * E2.dag() + E3 * psi_t_temp * E3.dag()
    if wigner:
        plot_slider(wa_list, wb_list, len(tlist_))
    if plot: 
        plt.figure()
        plt.plot(tlist_, fock0_list**2, label='|0>')
        plt.plot(tlist_, fock1_list**2, label='|1>')
        plt.plot(tlist_, fock2_list**2, label='|2>')
        plt.legend()
        plt.show()
    return wa_list, wb_list
    
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
        wb_list.append(qt.wigner(psi_t_temp.ptrace(1), xvec, xvec, g=2.0))
    #print qt.fidelity(psi_t_temp, A_DAG*A)
    return qt.fidelity(psi_t_temp, A_DAG*A)