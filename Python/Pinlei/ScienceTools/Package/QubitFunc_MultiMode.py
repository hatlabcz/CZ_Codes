# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 16:15:28 2018

@author: Hat_Pinlei
"""
import Tkinter as tk
import tkFileDialog
import os
import re
directory = re.findall(r'(.*\\ScienceTools)',os.getcwd(),re.S)[0]
#idle = re.findall(r'(.*\\Python)',os.getcwd(),re.S)[0]
import sys
sys.path.append(directory+'\\Package')
#sys.path.append(idle+'\\PythonLib')
import GUILib as GL
import csv
import matplotlib.pyplot as plt
import math
import numpy as np

h = 4.14e-15
Delta = 1.70e-4    #For Al
Phi0 = 2.07e-15
pi = 3.1415926

def cal_junction():
    def cal_design():
        
        Lj = float(input_value1[0].get()) * 1e-9
        A = float(input_value1[1].get()) * 1e-12
        R = 2.0 * pi **2 * Delta * Lj/ (1.12 * h)
        Ic = Phi0/ (2.0 * pi * Lj)
        Jc = Ic/A
        R_value.set(str(round(R,4)) + '  Ohm')
        Ic_value.set(str(round(Ic*1e6,4)) + '  uA')
        Jc_value.set(str(round(Jc*1e-6,4)) + '  uA/um^2')
        return (R,Ic,Jc)
        
    def cal_msmt():
        
        R = float(input_value2[0].get()) 
        A = float(input_value2[1].get()) * 1e-12
        Lj = (1.12 * h * R)/(2.0 * pi **2 * Delta)
        Ic = Phi0/ (2.0 * pi * Lj)
        Jc = Ic/A
        Lj_2_value.set(str(round(Lj*1e9,4)) + '  nH')
        Ic_2_value.set(str(round(Ic*1e6,4)) + '  uA')
        Jc_2_value.set(str(round(Jc*1e-6,4)) + '  uA/um^2')
        return (Lj,Ic,Jc)    
        
        
    temp = tk.Toplevel()
    temp.geometry('600x400+500+300')    
    temp.title('Calculation of JJ') 
    temp.wm_iconbitmap(directory + '\\scriptL.ico')
    
    
    attention = 'Generally, we want to fix the current density around '
    tk.Label(temp, text = attention).grid(column = 4, row = 0)    
    
    attention = '0.7 uA/um^2 !!!!'
    tk.Label(temp, text = attention).grid(column = 4, row = 1)        
    
    tk.Label(temp, text = 'Design Stage').grid(column = 1, row = 0)
    keys = ['Inductance of junction (Lj): ','The area of junction (A): ']
    units = ['nH', 'um^2']
    input_value1 = GL.input_label_func(temp, keys, units, row_init = 1)
    tk.Button(temp, text = 'Calculate', command = cal_design).grid(column = 1, row = 3)

    R_value = tk.StringVar()
    Ic_value = tk.StringVar() 
    Jc_value = tk.StringVar()
    
    tk.Label(temp, text = 'RT resistance(R): ').grid(column = 0, row = 4)
    tk.Label(temp, textvariable = R_value).grid(column = 1, row = 4)
    
    tk.Label(temp, text = 'Critical Current(Ic): ').grid(column = 0, row = 5)
    tk.Label(temp, textvariable = Ic_value).grid(column = 1, row = 5)
    
    tk.Label(temp, text = 'Current Density(Jc): ').grid(column = 0, row = 6)
    tk.Label(temp, textvariable = Jc_value).grid(column = 1, row = 6)
    
    
    tk.Label(temp, text = 'Msmt Stage').grid(column = 1, row = 7)
    keys = ['RT resistance of junction (R): ','The area of junction (A): ']
    units = ['Ohm', 'um^2']
    input_value2 = GL.input_label_func(temp, keys, units, row_init = 8)    
    tk.Button(temp, text = 'Calculate', command = cal_msmt).grid(column = 1, row = 10)
    
    Lj_2_value = tk.StringVar()
    Ic_2_value = tk.StringVar() 
    Jc_2_value = tk.StringVar()    
    
    tk.Label(temp, text = 'Inductance (Lj): ').grid(column = 0, row = 11)
    tk.Label(temp, textvariable = Lj_2_value).grid(column = 1, row = 11)
    
    tk.Label(temp, text = 'Critical Current(Ic): ').grid(column = 0, row = 12)
    tk.Label(temp, textvariable = Ic_2_value).grid(column = 1, row = 12)
    
    tk.Label(temp, text = 'Current Density(Jc): ').grid(column = 0, row = 13)
    tk.Label(temp, textvariable = Jc_2_value).grid(column = 1, row = 13)        
    
    return


def hfss_simulation():
    temp = tk.Toplevel()
    temp.geometry('800x200+500+300')    
    temp.title('HFSS simulation anlysis') 

    def func():
        filename = tkFileDialog.askopenfilename(initialdir = "E:\\",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        with open (filename,'rb') as csvres:
            result = csv.reader(csvres)
            res = list(result)
            del res[0]
    
        xdata = []
        ydata = []
        
        for i in res:
            xdata = xdata + [float(i[0])]
            ydata = ydata + [float(i[1])]
        plt.plot(xdata,ydata)
        
        test = []
        for i in range(len(ydata)-1):
            if ydata[i] * ydata[i+1] < 0:
                test.append(i)

        mode = []
        mode_d=[] #mode deritivate
        for index in test:
            derivative_mode = (ydata[index+1]-ydata[index])/(2.0*pi*1e9*(xdata[index+1]-xdata[index]))
            z_mode = 2.0 / (((xdata[index]+xdata[index+1])/2) * derivative_mode)
            c_mode = 0.5 * derivative_mode
            if derivative_mode > 0 :
                mode.append([index,derivative_mode,c_mode,z_mode])
                mode_d.append(derivative_mode)
        print mode, mode_d
        
        qubit_mode = mode[mode_d.index(min(mode_d))]#the mode that has the minimum slope
        del mode[mode_d.index(min(mode_d))]
        cavity_modes = mode
        c_mode_num=len(cavity_modes) #number of cavity modes
            
        e = 1.6021766208e-19
        hbar = 1.0545718e-34            
        ec = e*e / (2.0*qubit_mode[2])
        chi_qq = -ec / (2 * pi * hbar)
        chi_cc = [0.] *   c_mode_num     
        chi_qc = [0.] *   c_mode_num  
        coupling = [0.] *   c_mode_num  
        
        for i in range(c_mode_num):            
            chi_cc[i] = -ec / (2 * pi * hbar) * cavity_modes[i][3]**2/qubit_mode[3]**2
            chi_qc[i] = -2.0 * math.sqrt(chi_qq * chi_cc[i])
            coupling[i] = math.sqrt(chi_qc[i]/(4.0 * chi_qq) * abs(xdata[qubit_mode[0]]-xdata[cavity_modes[i][0]])**2)

      
      
        keys = ['Qubit frequency', 'Capacitance_Q', 'Chi_qq','','']
        units = ['GHz', 'pF', 'Mhz','','']
        for i in range(c_mode_num):
            keys += ['Cavity frequency', 'Capacitance_C', 'Chi_cc', 'Chi_qc', 'Coupling strength(g)']
            units += ['GHz', 'nF', 'MHz', 'MHz', 'MHz']
        entry_set = GL.input_label_func(temp,keys,units, grid = (c_mode_num+1,5)) 


        for entry in entry_set:
            entry.delete(0,tk.END)
            
        entry_set[0].insert(0,str(xdata[qubit_mode[0]]))
        entry_set[1].insert(0,str(qubit_mode[2] * 1e12))
        entry_set[2].insert(0,str(chi_qq * 1e-6))
        entry_set[3].insert(0,'')
        entry_set[4].insert(0,'')
        
        for i in range(c_mode_num):        
            entry_set[5*i+5].insert(0,str(xdata[cavity_modes[i][0]]))
            entry_set[5*i+6].insert(0,str(cavity_modes[i][2] * 1e9))
            entry_set[5*i+7].insert(0,str(chi_cc[i] * 1e-6))
            entry_set[5*i+8].insert(0,str(chi_qc[i] * 1e-6))
            entry_set[5*i+9].insert(0,str(coupling[i] * 1e3))
            
        

    tk.Button(temp, text = 'Load file', command = func).grid(column = 0, row = 8)
#    keys = ['Qubit frequency', 'Capacitance_Q', 'Chi_qq', 'Cavity frequency', 'Capacitance_C', 'Chi_cc', 'Chi_qc', 'Coupling strength(g)', '']
#    units = ['GHz', 'pF', 'Mhz', 'GHz', 'nF', 'MHz', 'MHz', 'MHz', '']
#    entry_set = GL.input_label_func(temp,keys,units, grid = (3,3))
    temp.mainloop()

if __name__ == '__main__':
    hfss_simulation()