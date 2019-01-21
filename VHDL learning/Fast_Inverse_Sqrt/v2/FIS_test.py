# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 14:28:37 2018

@author: Administrator
"""

import sys
sys.path.append('C:\Program Files (x86)\Keysight\SD1\Libraries\Python')
import keysightSD1
import matplotlib.pyplot as plt
import numpy as np
import time

# MODULE CONSTANTS
PRODUCT = ""
CHASSIS = 1
SLOT_AWG1 = 2   # M3202A AWG1
SLOT_AWG2 = 3   # M3202A AWG2
SLOT_DIG = 4   # M3102A Digitizer
SLOT_MARK1 = 5   # M3201A Marker1
SLOT_MARK2 = 6   # M3201A Marker1

#########################       MODULE INIT     ###############################
FPGA_Dig = keysightSD1.SD_DIO()
FPGA_Dig_ID = FPGA_Dig.openWithSlot("", CHASSIS, SLOT_DIG)

AWG1 = keysightSD1.SD_AOU()
AWG1_ID = AWG1.openWithSlot("", CHASSIS, SLOT_AWG1)
AWG1.waveformFlush()

MARK1 = keysightSD1.SD_AOU()
MARK1_ID = MARK1.openWithSlot("", CHASSIS, SLOT_MARK1)

Digitizer = keysightSD1.SD_AIN()
Digitizer_ID = Digitizer.openWithSlot("", CHASSIS, SLOT_DIG)
# channelInputConfig(self, channel, fullScale(in Volt), impedance(0 is HiZ, 1 is 50ohm), coupling(0 is DC, 1 is AC))
# 
Digitizer.channelInputConfig(1,1,1,0) 
Digitizer.channelInputConfig(2,1,1,0)
Digitizer.channelInputConfig(3,1,1,0)
Digitizer.channelInputConfig(4,1,1,0)

HVI = keysightSD1.SD_HVI()

############################# FPGA Part #######################################
if 0: #Reset FPGA_Dig
    FPGA_Dig.FPGAreset(2)  # Pulse Reset (Plz never change the variable)

if 1: #Write PCport(0), address: 0
    # FPGAwritePCport(int nPCport, int [] data, int address, int addressMode, int accessMode)
    # Address Mode: 0: Auto Increment; 1: Fixed; 
    # Access Mode: 0: Non DMA; 1: DMA
    a=0b0111100111000000
    b=0b0001110000000000   
    x=(a**2+b**2)
    if not FPGA_Dig.FPGAwritePCport(0, [x], 0, 0, 0):
        print 'Write value wave successful'
    else:
        print 'Plz check, write PC port wrong'
    time.sleep(0.1)  
############################## Digitizer Part #################################
if 1: #Digitizer read value
    plt.close('all')
    points_per_cycle =60
    cycles =1
    trigger_delay = 0
    timeout = 1000   
    data_read_selector = '0011'   

    Digitizer.DAQconfig(1, points_per_cycle, cycles, trigger_delay, 0)
    Digitizer.DAQconfig(2, points_per_cycle, cycles, trigger_delay, 0)
    Digitizer.DAQconfig(3, points_per_cycle, cycles, trigger_delay, keysightSD1.SD_TriggerModes.SWHVITRIG)
    Digitizer.DAQconfig(4, points_per_cycle, cycles, trigger_delay, keysightSD1.SD_TriggerModes.SWHVITRIG)
            

    data = np.zeros((4, points_per_cycle * cycles))
    #HVI.reset()
    #HVI.start()
    Digitizer.DAQstartMultiple(int(data_read_selector,2))
#    AWG1.AWGstartMultiple(0b1111)
    
    

    for i in range(4):
        if int(data_read_selector[-i+3]):
            data[i] = Digitizer.DAQread(i+1, points_per_cycle * cycles, timeout)
    
    exp = 1/np.sqrt(x)
    I = data[0][1]/2.0**24
    result = data[1][1]/2.0**24
    
    result_c=I*(1.5-x/2.0*I*I)
   
    print 'expected   :', exp
    print 'I          :', I
    print 'result     :',  result
    print 'result_cal :',  result_c
    
    
#    if cycles==1 :
#        plt.figure()
#        for i in range(4):
#            if int(data_read_selector[-i+3]):
#                plt.plot(data[i], label = 'DAQ'+str(i+1))


    if int(data_read_selector[2]) and int(data_read_selector[3]) and cycles >1:
        plt.figure()
        plt.title('IQ pair')
        plt.plot(data[0][points_per_cycle+2::points_per_cycle],data[1][points_per_cycle+2::points_per_cycle], '*')
        plt.xlabel('I')
        plt.ylabel('Q')
        ax=plt.gca()
        ax.set_aspect(1)
        