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
    
    
def hfss_simulation_snail():
    temp = tk.Toplevel()
    temp.geometry('1200x200+500+300')    
    temp.title('HFSS SNAIL simulation analysis') 
    
    
    def func_snail():
        #Lj = float(Ljentry.get())
        
        filename = tkFileDialog.askopenfilename(initialdir = "E:\\",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        
        chosenfile.delete('1.0', tk.END)
        nametodisplay = filename[len(os.getcwd())-4:]
        chosenfile.insert(tk.END, nametodisplay)
        
        with open (filename,'rb') as csvres:
            result = csv.reader(csvres)
            res = list(result)
            del res[0]
    
        xdata = []
        ydata = []
        
        for i in res:
            xdata = xdata + [float(i[0])]
            ydata = ydata + [float(i[1])]
        #plt.plot(xdata,ydata)
        
        test = []
        for i in range(len(ydata)-1):
            if ydata[i] * ydata[i+1] < 0:
                test.append(i)

        mode = []
        mode_d=[] #mode deritivate
        for index in test:
            derivative_mode = (ydata[index+1]-ydata[index])/(2.0*pi*1e9*(xdata[index+1]-xdata[index]))
            z_mode = 2.0 / (((xdata[index]+xdata[index+1])*pi*1e9) * derivative_mode)
            c_mode = 0.5 * derivative_mode
            if derivative_mode > 0 :
                mode.append([index,derivative_mode,c_mode,z_mode])
                mode_d.append(derivative_mode)
        
        qubit_mode = mode[mode_d.index(min(mode_d))]#the mode that has the minimum slope
        del mode[mode_d.index(min(mode_d))]
        cavity_modes = mode
        c_mode_num=len(cavity_modes) #number of cavity modes
            
        e = 1.6021766208e-19
        hbar = 1.0545718e-34
        phi0 = hbar/(2*e)
        coupling = [[0. for i in range(c_mode_num)] for i in range(c_mode_num)]
        c3 = 8.35*10**-23       #J, comes from mathematica solution.. this is an approximation
        
        
        for i in range(c_mode_num):
            for j in range(c_mode_num):            
                coupling[i][j] = c3*(hbar/2)**(3.0/2.0)/phi0**3*(cavity_modes[i][3]*cavity_modes[j][3]*qubit_mode[3])**(0.5)/(2.0*pi*hbar)
      
        couplist = []
        for i in range(len(coupling)):
            for j in range(i+1, len(coupling)):
                couplist.append(coupling[i][j])
        couplistnp = np.array(couplist)
        gmax = couplistnp.max()
        gmin = couplistnp.min()
        
        
        keys = ['Qubit frequency']+['' for j in range(1, c_mode_num+1)]
        units = ['GHz']+['' for j in range(1, c_mode_num+1)]
        for i in range(1, c_mode_num+1):
            keys += ['Cavity frequency']+["g"+str(i)+str(j)  for j in range(1, c_mode_num+1)]
            units += ['GHz']+['MHz' for j in range(1, c_mode_num+1)]
        keys += ['Max', 'Min', 'Max/Min'] +['' for j in range(1, c_mode_num+1-2)]
        units += ['MHz', 'MHz', '']+['' for j in range(1, c_mode_num+1-2)]
        
        entry_set = GL.input_label_func(temp,keys,units, grid = (c_mode_num+1+1,c_mode_num+1)) 


        for entry in entry_set:
            entry.delete(0,tk.END)
            
        entry_set[0].insert(0,str(xdata[qubit_mode[0]]))
        for i in range(1, c_mode_num+1):    
           entry_set[i].insert(0,'')
        
        for i in range(c_mode_num):
            entry_set[(c_mode_num+1)*(i+1)].insert(0,str(xdata[cavity_modes[i][0]]))
            for j in range(c_mode_num):
                entry_set[(c_mode_num+1)*(i+1)+j+1].insert(0,str(coupling[i][j] * 1e-6))
        
        entry_set[(c_mode_num+1)**2 + 0].insert(0,str(gmax*1e-6))
        entry_set[(c_mode_num+1)**2 + 1].insert(0,str(gmin*1e-6))
        entry_set[(c_mode_num+1)**2 + 2].insert(0,str(gmax/gmin))
        for i in range(3, c_mode_num+1):    
           entry_set[(c_mode_num+1)**2 + i].insert(0,'')
           
#    legend = tk.Text(temp, height=1, width=30)
#    legend.grid(column=1, row=8)
#    Ljentry = tk.Entry(temp)
#    Ljentry.grid(column = 2, row = 8)
#    legend.insert(tk.END, "Input Lj in nH before loading:")
    tk.Button(temp, text = 'Load file', command = func_snail).grid(column = 0, row = 8)
    chosenfile = tk.Text(temp, height=1, width=30)
    chosenfile.grid(column = 1, row = 8)
#    keys = ['Qubit frequency', 'Capacitance_Q', 'Chi_qq', 'Cavity frequency', 'Capacitance_C', 'Chi_cc', 'Chi_qc', 'Coupling strength(g)', '']
#    units = ['GHz', 'pF', 'Mhz', 'GHz', 'nF', 'MHz', 'MHz', 'MHz', '']
#    entry_set = GL.input_label_func(temp,keys,units, grid = (3,3))
    temp.mainloop()

if __name__ == '__main__':
    hfss_simulation()