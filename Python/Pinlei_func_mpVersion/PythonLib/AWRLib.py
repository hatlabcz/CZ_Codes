# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:21:26 2018

@author: Hat_Pinlei
"""
import sys
sys.path.append(r'E:\Python\PythonLib')
sys.path.append(r'E:\GoogleDrive\Python\PythonLib')
import win32com.client as awr
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss
import lib
import h5py
import matplotlib
import matplotlib.colors as color
from matplotlib.widgets import Cursor
from matplotlib.widgets import Slider
import IOlib as IOL
import Plotlib as PL
import Functionlib as FL
from matplotlib.widgets import Slider

class mwSim():
    def __init__(self,**kwargs):
        self.path = kwargs['path']
        self.filename = kwargs['filename']
        self.awrde = awr.Dispatch("MWOApp.MWOffice")
        if kwargs['Open']:
            self.awrde.Open(self.path+self.filename)
        self.proj = self.awrde.Project       
        
    def change_frequency_single(self,single_freq):
        freq = self.proj.Frequencies
        freq.Clear()
        freq.Add(single_freq)
        
    def change_frequency_list(self,freqlist):
        freq = self.proj.Frequencies
        freq.Clear()
        freqlist = np.array(freqlist).flatten().tolist()
        freq.AddMultiple(freqlist)

    def export_data(self,graph,path,filename):
#        print path+filename + ' writes'
        self.proj.Graphs(graph).ExportTraceData(path+filename)
        return filename
    
    def run(self):
        self.proj.Simulator.Analyze()
        
    def run_specific(self,graph):
        self.proj.Graphs(graph).SimulateMeasurements()
        
    def change_parameter(self,item_num,para_num,value):
        self.proj.Schematics('main').Elements.Item(item_num).\
        Parameters.Item(para_num).ValueAsString = value
        
    def change_equation(self,eq_num,value):
        self.proj.Schematics('main').Equations(eq_num).Expression = value

def read_txt(path,filename, plot = True, label = None, skip = 1):
    data = np.genfromtxt(path+filename, delimiter = '\t', \
            skip_header = skip, missing_values = ' ', filling_values=np.nan)
    if plot:
        plt.plot(data[:,0],data[:,1],label = label)
        plt.xlabel('Power strength')
        plt.ylabel('Phase')
    return data

def find_resonate(xdata,ydata, silent = False):
    f_res = []    
    for i in range(len(ydata)-1):
        if ydata[i] * ydata[i+1] <= 0:
            res = (xdata[i] + xdata[i+1])/2.0            
            f_res.append(res)
            if not silent:
                print 'Resonate frequency is ', res, 'GHz'
    return f_res

def find_resonate_Lssnm(xdata,ydata):
    for i in range(len(ydata)):
        if ydata[i] * ydata[i+1] <= 0:
            break
        f_res = (xdata[i]+xdata[i+1])/2
        
    return f_res



def find_resonate_mag(xdata,ydata):
    res_index = np.where(ydata <= np.nanmin(ydata)/1000.0)[0]
    f_res = []
    for i in range(len(res_index)-1):
        if res_index[i+1] - res_index[i] > 1:
            fre1 = np.average(xdata[res_index[0:i+1]])
            fre2 = np.average(xdata[res_index[i+1:-1]])
    f_res.append(fre1)
    f_res.append(fre2)
    print 'Resonate frequency is ', fre1, 'GHz'
    print 'Resonate frequency is ', fre2, 'GHz'
    return f_res

def find_resonate_mag_trans(xdata,ydata):
    res_index = np.where(ydata >= 1.0e-7)[0]#np.nanmin(ydata)+(np.nanmax(ydata)-np.nanmin(ydata))/50)[0]
    f_res = []
    for i in range(len(res_index)-1):
        if res_index[i+1] - res_index[i] > 1:
            fre1 = np.average(xdata[res_index[0:i+1]])
            fre2 = np.average(xdata[res_index[i+1:-1]])
    f_res.append(fre1)
    f_res.append(fre2)
    print 'Resonate frequency is ', fre1, 'GHz'
    print 'Resonate frequency is ', fre2, 'GHz'
    return f_res

def check_mode_frequency(path):
    plt.close('all')
    pytest = mwSim(path = r'H:\Users\pil9\Project\FrequencyComb\AWR\\', \
                    filename = 'frequency_comb_test.emp', Open = False)
    pytest.change_frequency_list(np.linspace(2e9,7e9,5001))
    f_res = np.zeros([200,2])
    I_c = np.zeros(200)
    for i in range(200):
        i0 = 1.5e-7 + i * 1e-8
        I_c[i] = i0
        pytest.change_equation(2,'I0='+ str(i0))
        pytest.run()
        filename = pytest.export_data('Linear',path,'temp_test.txt'.format(i))
        xdata,ydata = read_txt(path,filename)        
        f_res[i,0],f_res[i,1] = find_resonate(xdata,ydata)
    plt.figure()
    plt.plot(I_c*1e6,f_res[:,0],'*')
    plt.plot(I_c*1e6,f_res[:,1],'*')
    plt.xlabel('Ic(mA)')
    plt.ylabel('Resonate Frequency(GHz)')
    
    
# I0 from 3.29106e-5 to 1.64553e-7
    
if __name__ == "__main__":
    fre_points = 200
    points = 5001
    path = r'E:\Data\FC\\'
    path = lib.create_directory(path,time = True)  
    plt.close('all')
    pytest = mwSim(path = r'H:\Users\pil9\Project\FrequencyComb\AWR\\', \
                    filename = 'frequency_comb_test.emp', Open = False)
    incre = 0
                    
#                    
#    
#    start = -140
#    stop = -40
#    stepsize = 0.01
##    incre += 1    
#    f_res = np.zeros(2)
###    i0 = 8e-7
##    pytest.change_equation(3,'pwr = -100')
##    pytest.change_frequency_list(np.linspace(4.5e9,5.5e9,10001))
##    pytest.change_equation(2,'I0='+ str(i0*1e3))
##    pytest.run_specific('Linear')
##    filename = pytest.export_data('Linear',path,'mode_frequency_1.txt')
##    data = read_txt(path,filename, plot = True)        
##    f_res[0],f_res[1] = find_resonate(data[:,0],data[:,1])
##    print 'detune', f_res[0]-f_res[1], ' GHz'
##    fdrive = f_res[0]
##    print fdrive
#    pytest.change_frequency_single(5.02723*1e9)
#    pytest.change_equation(3,'pwr = stepped('+str(start)+','+str(stop)+','+str(stepsize)+')')
#    pytest.run_specific('Lssnm')
#    filename = pytest.export_data('Lssnm',path,'forward_{}.txt'.format(incre))
#    plt.figure()
#    plt.grid()
#    data_f = read_txt(path,filename,label = 'forward',plot=True)        
# 
#    pytest.change_equation(3,'pwr = stepped('+str(stop)+','+str(start)+',-'+str(stepsize)+')')
#    pytest.run_specific('Lssnm')
#    filename = pytest.export_data('Lssnm',path,'backward_{}.txt'.format(incre))
#    data_f = read_txt(path,filename,label = 'backward',plot=True)    
#    plt.legend()
    

    
    
#########################    Phase Sweep    ###################################
#    fre_points = 41
#    pwr_points = 101
#    phi0 = 3.29106e-16
#    Cc = 0.211971e-12
#    Ll = 2.5e-9
#    
#    f_res = np.zeros([fre_points,2])
#    I_c = np.zeros(fre_points)
#    phase_sweep = np.zeros([10001,2,fre_points])
#    xdata = np.zeros(2*fre_points)
#    bar = FL.TextBar(fre_points)
#      
#    
#    for i in range(fre_points):
#        bar.update(i)
#        omegab = 5.02723 * 1e9 + i * 0.5 * 1e6        
#        i0 = (4.0 * Cc * omegab**2 * phi0 * np.pi**2) \
#            / (1.0 - 4.0 * Cc * Ll * omegab**2 * np.pi**2)
#
#        pytest.change_equation(2,'I0='+ str(i0*1e3))
#
#        pytest.change_frequency_single(5.02723*1e9)
#        pytest.change_equation(3,'pwr = stepped(-140,-40,0.01)')        
#        pytest.run_specific('Lssnm')
#        filename = pytest.export_data('Lssnm',path,'forward.txt')
#        data_f = read_txt(path,filename,label = 'forward',plot=False)        
#        phase_sweep[:,0,i] = data_f[:,1]
# 
#        pytest.change_equation(3,'pwr = stepped(-40,-140,-0.01)')        
#        pytest.run_specific('Lssnm')
#        filename = pytest.export_data('Lssnm',path,'backward.txt')
#        data_f = read_txt(path,filename,label = 'backward',plot=False)        
#        phase_sweep[:,1,i] = data_f[:,1]
#    path,filename = IOL.write_h5(path,'phase_sweep','phase',phase_sweep,key2 = 'xdata',value2 = xdata)
#    bar.finished()
        
#    plt.close('all')
#    phase_sweep = IOL.read_h5(path,filename,item = 'phase')
#    yaxis = np.arange(-120,-70,0.01)
#    xdata = IOL.read_h5(path,filename,item = 'xdata')
#    PL.hist2d(phase_sweep,xdata,'$\Delta\omega_d$(GHz)',yaxis,'Power(dBm)')    
#    
    
#    plt.close('all')
#    path = r'E:\Data\FC\2018_05_03\\'
#    filename = 'phase_sweep_(1)'
#    phase_sweep = IOL.read_h5(path,filename,item = 'phase')[:,0:100]
#    yaxis = np.arange(-120,-70,0.01)
#    xdata = IOL.read_h5(path,filename,item = 'xdata')[0:100]
#    PL.hist2d(phase_sweep,xdata,'$\Delta\omega_d$(GHz)',yaxis,'Power(dBm)')       
   
   
   
#######################    Power Spectrum     #################################
    
#    fre_points = 101
#    points = 51
#    f_res = np.zeros([fre_points,2])
#    I_c = np.zeros(fre_points)
#    phase_sweep = np.zeros([points,2*fre_points])
#    xdata = np.zeros(2*fre_points)
#    bar = FL.TextBar(fre_points)
#    power_spec = np.zeros([51,101,200,2])
#    for i in range(fre_points):
#        bar.update(i)
#        i0start = 7.0e-7
#        pytest.change_equation(3,'pwr = -100')
#        i0 = i0start + i * 5e-9
#        pytest.change_frequency_list(np.linspace(4.7e9,6.7e9,10001))
#        pytest.change_equation(2,'I0='+ str(i0*1e3))
#        pytest.run_specific('Linear')
#        filename = pytest.export_data('Linear',path,'mode_frequency_1.txt'.format(i))
#        data = read_txt(path,filename, plot = False)        
#        f_res[i,0],f_res[i,1] = find_resonate(data[:,0],data[:,1])
#        xdata[2*i] = f_res[i,0]-f_res[i,1]
#        fdrive = f_res[i,0]
#        pytest.change_frequency_single(fdrive*1e9)
#        for j in range(51):
#            power = -120 + j
#            pytest.change_equation(3,'pwr = '+str(power))        
#            pytest.run_specific('Spectrum')
#            filename = pytest.export_data('Spectrum',path,'spec')
#            data_spec = read_txt(path,filename, plot = False, skip = 2)
#            power_spec[j,i,:,:] = data_spec
#    bar.finished()
#    path,filename = IOL.write_h5(path,'power_spectrum','power',power_spec,key2 = 'xdata',value2 = xdata)




###############################################################################
    path = r'E:\Data\FC\2018_05_17\\'
    filename = 'power_spectrum_little_(1)'
    power_sweep = IOL.read_h5(path,filename,item = 'power')
    xdata = IOL.read_h5(path,filename,item = 'xdata')
    fig,ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    spec, = plt.plot(power_sweep[0,0,:,0],power_sweep[0,0,:,1])
    plt.ylim(-400,0)
    axcolor = 'lightgoldenrodyellow'
    power = plt.axes([0.15 ,0.1,0.75,0.03], facecolor = axcolor)
    freq = plt.axes([0.15 ,0.15,0.75,0.03], facecolor = axcolor)
    
    spower = Slider(power, 'Pwr(dBm)', -120, -70, valstep = 0.5)
    sfreq = Slider(freq, 'Freq(MHz)', -2000 , -0.0, valstep = 10)
    
    def update(val):
        pw = int(((spower.val)+120)*2.0)
        fr = int(abs(sfreq.val) /10.0)
        print pw,fr        
        spec.set_ydata(power_sweep[pw,fr,:,1])
        
    sfreq.on_changed(update)
    spower.on_changed(update)
###############################################################################

#    path = r'E:\Data\FC\2018_05_16\\'
#    filename = 'power_spectrum_little_(14)'
#    power_sweep1 = IOL.read_h5(path,filename,item = 'power').astype(np.float32)
#    xdata = IOL.read_h5(path,filename,item = 'xdata')
#    path = r'E:\Data\FC\2018_05_17\\'
#    filename = 'power_spectrum_little_(0)'
#    power_sweep2 = IOL.read_h5(path,filename,item = 'power').astype(np.float32)
#    xdata = IOL.read_h5(path,filename,item = 'xdata')
#    power_sweep = np.zeros([251,202,1001,2],dtype=np.float32)
#    power_sweep[:,:101,:,:] = power_sweep1
#    power_sweep[:,101:,:,:] = power_sweep2    
#    fig,ax = plt.subplots()
#    plt.subplots_adjust(bottom=0.25)
#    spec, = plt.plot(power_sweep[0,0,:,0],power_sweep[0,0,:,1])
#    plt.ylim(-400,0)
#    axcolor = 'lightgoldenrodyellow'
#    power = plt.axes([0.15 ,0.1,0.75,0.03], facecolor = axcolor)
#    freq = plt.axes([0.15 ,0.15,0.75,0.03], facecolor = axcolor)
#    
#    spower = Slider(power, 'Pwr(dBm)', -120, -70, valstep = 0.2)
#    sfreq = Slider(freq, 'Freq(MHz)', -100 , -0.0, valstep = 0.5)
#    
#    def update(val):
#        pw = int(((spower.val)+120)*5.0)
#        fr = int(abs(sfreq.val) *2.0)
#        print pw,fr        
#        spec.set_ydata(power_sweep[pw,fr,:,1])
#        
#    sfreq.on_changed(update)
#    spower.on_changed(update)



    
'''
    fre_points = 30
    points = 4001    
    f_res = np.zeros([fre_points,2])
    I_c = np.zeros(fre_points)
    phase_sweep = np.zeros([points,fre_points])
    xdata = np.zeros(fre_points)
    bar = FL.TextBar(fre_points)
        
    
    for i in range(fre_points):
        bar.update(i)    
        i0start = 6.5e-7
        pytest.change_equation(3,'pwr = -100')
        i0 = i0start + i * 2e-9
        I_c[i] = i0
        pytest.change_frequency_list(np.linspace(4.5e9,5.5e9,10001))
        pytest.change_equation(2,'I0='+ str(i0))
        pytest.run_specific('Linear')
        filename = pytest.export_data('Linear',path,'mode_frequency_1.txt'.format(i))
        data = read_txt(path,filename, plot = False)        
        f_res[i,0],f_res[i,1] = find_resonate(data[:,0],data[:,1])
        xdata[i] = f_res[i,0]-f_res[i,1]
        fdrive = f_res[i,0]
        print fdrive
        pytest.change_frequency_single(fdrive*1e9)
        pytest.change_equation(3,'pwr = stepped(-130,-90,0.01)')        
        pytest.run_specific('Lssnm')
        filename = pytest.export_data('Lssnm',path,'forward.txt')
        data_f = read_txt(path,filename,label = 'forward',plot = False)        
        phase_sweep[:,i] = data_f[:,1]
            
    path,filename = IOL.write_h5(path,'phase_sweep','phase',phase_sweep,key2 = 'xdata',value2 = xdata)
    bar.finished()
        
    plt.close('all')
    phase_sweep = IOL.read_h5(path,filename,item = 'phase')
    yaxis = np.arange(-120,-70,0.01)
    xdata = IOL.read_h5(path,filename,item = 'xdata')
    PL.hist2d(phase_sweep,xdata,'$\Delta\omega_d$(GHz)',yaxis,'Power(dBm)')
        
       
    for i in range(fre_points):
        bar.update(i)    
        i0start = 6.5e-7
        pytest.change_equation(3,'pwr = -100')
        i0 = i0start + i * 2e-9
        I_c[i] = i0
        pytest.change_frequency_list(np.linspace(4.5e9,5.5e9,10001))
        pytest.change_equation(2,'I0='+ str(i0))
        pytest.run_specific('Linear')
        filename = pytest.export_data('Linear',path,'mode_frequency_1.txt'.format(i))
        data = read_txt(path,filename, plot = False)        
        f_res[i,0],f_res[i,1] = find_resonate(data[:,0],data[:,1])
        xdata[i] = f_res[i,0]-f_res[i,1]
        fdrive = f_res[i,0]
        print fdrive
        pytest.change_frequency_single(fdrive*1e9)
        pytest.change_equation(3,'pwr = stepped(-90,-130,-0.01)')        
        pytest.run_specific('Lssnm')
        filename = pytest.export_data('Lssnm',path,'backward.txt')
        data_f = read_txt(path,filename,label = 'backward',plot = False)        
        phase_sweep[:,i] = data_f[:,1]
            
    path,filename = IOL.write_h5(path,'phase_sweep','phase',phase_sweep,key2 = 'xdata',value2 = xdata)
    bar.finished()
        
    plt.figure()
    phase_sweep = IOL.read_h5(path,filename,item = 'phase')
    yaxis = np.arange(-120,-70,0.01)
    xdata = IOL.read_h5(path,filename,item = 'xdata')
    PL.hist2d(phase_sweep,xdata,'$\Delta\omega_d$(GHz)',yaxis,'Power(dBm)')       
'''
    
    
    
#    path = r'E:\Data\FC\2018_05_09\\'
#    filename = 'power_spectrum_large_(0)'
#    power_sweep = IOL.read_h5(path,filename,item = 'power')
#    xdata = IOL.read_h5(path,filename,item = 'xdata')
#    fig,ax = plt.subplots()
#    plt.subplots_adjust(bottom=0.25)
#    spec, = plt.plot(power_sweep[0,0,:,0],power_sweep[0,0,:,1])
#    plt.ylim(-400,0)
#    axcolor = 'lightgoldenrodyellow'
#    power = plt.axes([0.15 ,0.1,0.75,0.03], facecolor = axcolor)
#    freq = plt.axes([0.15 ,0.15,0.75,0.03], facecolor = axcolor)
#    
#    spower = Slider(power, 'Pwr(dBm)', -120, -70)
#    sfreq = Slider(freq, 'Freq(GHz)', -2.5 , -1.5, valstep = 0.01)
#    
#    def update(val):
#        pw = int(spower.val)
#        if (spower.val != pw):
#            spower.set_val(pw)
#
#        fr = int(abs(sfreq.val+1.5)*10)
#        spec.set_ydata(power_sweep[pw + 120,fr,:,1])
#        
#    sfreq.on_changed(update)
#    spower.on_changed(update)

    
#        vmin = np.nanmin(phase_sweep), vmax = np.nanmax(phase_sweep)
#        pytest.change_equation(3,'pwr = stepped(-80,-200,-0.01)')
#        pytest.run_specific('Lssnm')
#        filename = pytest.export_data('Lssnm',path,'backward.txt')
#        data_b = read_txt(path,filename,label = 'backward')
#        plt.legend()           
        
    
#    pytest.change_equation(3,'pwr = stepped(-500,-80,0.001)')
##    pytest.change_equation(3,'pwr = {-141,-140,-139}')
#    pytest.run()
#    filename = pytest.export_data('Lssnm',path,'forward.txt')
#    data_f = read_txt(path,filename,label = 'forward')
#    
#    pytest.change_equation(3,'pwr = stepped(-80,-500,-0.001)')
##    pytest.change_equation(3,'pwr = {-139,-140,-141}')
#    pytest.run()
#    filename = pytest.export_data('Lssnm',path,'backward.txt')
#    data_b = read_txt(path,filename,label = 'backward')
#    plt.legend()    

###############################################################################






    
#    pytest.change_equation(4,'pwr = stepped(-200,-100,0.1)')
#    pytest.change_parameter('SWP1',3,'stepped(-200,-100,0.12)')
#    pytest.run()
#    filename = pytest.export_data('Lssnm',path,'backward.txt')
#    filename = 'phase.txt'
#    xdata,ydata = read_txt(path,filename)
#    find_resonate(xdata,ydata)
#    plt.figure()
#    filename = 'mag.txt'
#    xdata,ydata = read_txt(path,filename)
#    find_resonate_mag(xdata,ydata)    
    
#    path = r'E:\Data\FlyingQubit\2018_04_13\\'
#    filename = "forward.txt"
#    data = read_txt(path,filename)
#    plt.plot(data[:,0],data[:,1])
#
#    path = r'E:\Data\FlyingQubit\2018_04_13\\'
#    filename = "backward.txt"
#    data = read_txt(path,filename)
#    plt.plot(data[:,0],data[:,1])

#
#    pytest = mwSim(path = r'E:\LabProject\Experiment\FrequencyComb\AWR\\', \
#                    filename = 'frequency_comb_python.emp')
#    pytest.Change_Frequency([1,2,3])
