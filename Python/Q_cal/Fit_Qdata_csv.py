# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:09:04 2016

@author: HatLab_Xi Cao
"""

# Try to fit the data from HFSS simulation (apply to fit lots of csv file at the same time)

import Q_fit
import numpy as np
import matplotlib.pyplot as plt

#Gap = np.linspace(100,1000,19)
#Gap = np.linspace(50,100,6)
#Q_ext = np.empty(len(Gap))
#Q_ext[:] = np.NaN
#Q_int = np.empty(len(Gap))
#Q_int[:] = np.NaN
#F_0 = np.empty(len(Gap))
#F_0[:] = np.NaN
'''
i = 0
for val in Gap:
    name = "E:\HFSS\Q test\Large_Qext_data\Large_Qext_Gap_"+str(val)+"um.csv"
    Fitting_Params = {'Q_ext': 698.0, 'Q_int': 35488.0, 'A': 5.62e-10, 'B': 2*np.pi, 'E': -1.59/(2*np.pi*1e9), 'D':-27.0}
    result = Q_fit.Fit(0,0,0, Fitting_Params, plot = False, filename = name)
    F_0[i] = result[0]
    Q_ext[i] = result[1]
    Q_int[i] = result[2]
    i = i+1
    
plt.close('all')

plt.figure(1)
plt.plot(Gap,Q_ext)

plt.figure(2)
plt.plot(Gap,Q_int)

plt.figure(3)
plt.plot(Gap,F_0)
'''
'''
name = "E:\HFSS\Q test\Good result (do not change parameters)\Large_Qext_data\Large_Qext_Gap_"+str(195.0)+"um_9.2GHz.csv"
Fitting_Params = {'Q_ext':5000, 'Q_int': 100000, 'A': 4.2608e-10, 'B': np.pi, 'E': -0.5455/(2*np.pi*1e9), 'D':2.5}
result = Q_fit.Fit(0,0,0, Fitting_Params, plot = True, filename = name)
'''
'''
name = 'E:\HFSS\Gap_For_Flux\FluxGap on JPC\Good one (do not change parameters)\FluxGap_30um_Idl_3fingers_53um_Sig_6um_yshift_-50um_Sss.csv'
Fitting_Params = {'Q_ext':100, 'Q_int': 1000, 'A': -22.11*np.pi/(180.0*1e9), 'B': 136.548*np.pi/180.0, 'E': 0.0, 'D':0.0}
result = Q_fit.Fit(0,0,0, Fitting_Params, plot = True, filename = name)
'''

#name = 'E:\HFSS\Gap_For_Flux\FluxGap on JPC\Sigarm\FluxGap_30um_SigGap_195um_parallel.csv'
#name = 'E:\HFSS\Gap_For_Flux\FluxGap on JPC\Sigarm\FluxGap_30um_SigGap_195um_perpendicular.csv'
#name = 'E:\HFSS\Gap_For_Flux\FluxGap on JPC\Idlarm\Large_Port_arm_Gap\FluxGap_30um_PortGap_195um_parallel_Idlarm_02.csv'
#name = 'E:\HFSS\Gap_For_Flux\FluxGap on JPC\Idlarm\Large_Port_arm_Gap\FluxGap_30um_PortGap_195um_perpendicular_Idlarm_02.csv'
#name = "E:\HFSS\Gap_For_Flux\FluxGap on JPC\Idlarm\Large_Port_arm_Gap\\flux_gap_changing\FluxGap_"+str(45.0)+"um_PortGap_195um_parallel_Idlarm.csv"

#name = "E:\HFSS\Gap_For_Flux\FluxGap diagonal\Sig_arm\\FluxGap_7.5um_with_100um_centerpad.csv"
#name = "E:\HFSS\Gap_For_Flux\FluxGap diagonal\\JPC_diagonal_fluxgap_45um_centersquare_100um_Sii.csv"
#Fitting_Params = {'Q_ext':150, 'Q_int': 1e3, 'A': 0.0, 'B': 0.0, 'E': 0.0, 'D': 0.0}
#result = Q_fit.Fit(0,0,0, Fitting_Params, plot = True, filename = name)
#print name



#i = 0
#for val in Gap:
#    #name = 'E:\HFSS\Gap_For_Flux\FluxGap on JPC\Idlarm\Large_Port_arm_Gap\FluxGap_30um_PortGap_195um_parallel_Idlarm_02.csv'
#    print val
#    name = "E:\HFSS\Gap_For_Flux\FluxGap diagonal\Sig_arm\\FluxGap_7.5um_with_"+str(int(val))+ "um_centerpad.csv"
#    Fitting_Params = {'Q_ext':10000, 'Q_int': 1e5, 'A': 0.0, 'B': 0.0, 'E': 0.0, 'D':0.0}
#    result = Q_fit.Fit(0,0,0, Fitting_Params, plot = False, filename = name)
#    F_0[i] = result[0]
#    Q_ext[i] = result[1]
#    Q_int[i] = result[2]
#    i = i+1

#plt.plot(Gap, Q_idl, '*-')
#plt.xlabel('Gap(um)')
#plt.ylabel('Q')
#plt.title('Idler Q')
#plt.xlim(10,50)






