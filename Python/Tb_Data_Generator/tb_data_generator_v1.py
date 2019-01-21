# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:54:54 2018

@author: HatLabUnderGrads
"""

# Generated waveforms (in binary) for simulation test bench

import numpy as np
from scipy import signal
import matplotlib.pyplot as pltv
from bitstring import Bits
import random

n=2001 #number of points
maxium=1.5
prescaler=1.5
directory = 'H:\\Users\\chz78\\Python\\Tb_Data_Generator\\'
filename = 'div_in.txt'

digital_data_s =np.array(maxium/prescaler*(2**15-1) * signal.gaussian(n, std = 100) * np.sin(np.arange(0,n,1)/10.*2.*np.pi),dtype=int)
digital_data_r =np.array(maxium/prescaler*(2**15-1) * signal.gaussian(n, std = 100) * np.sin(np.arange(0,n,1)/10.*2.*np.pi),dtype=int)

digital_data_pc1 =np.array(maxium/prescaler*(2**15-1) *  np.sin(np.arange(0,n,1)/10.*2.*np.pi),dtype=int)
digital_data_pc2 =np.array(maxium/prescaler*(2**15-1) *  np.cos(np.arange(0,n,1)/10.*2.*np.pi),dtype=int)


digital_data_i =np.array(maxium/prescaler*(2**15-1) * (2* np.random.rand(n)-1),dtype=int)
digital_data_q =np.array(maxium/prescaler*(2**15-1) * (2* np.random.rand(n)-1),dtype=int)

digital_data_a = np.array(np.sqrt(digital_data_i**2+digital_data_q**2),dtype=int)




if 0:
    k=0
    with open(directory + filename, 'w') as txtfile:
        for j in range (n):
            bin_data_s=Bits(int=digital_data_s[j], length=16).bin
            bin_data_r=Bits(int=digital_data_r[j], length=16).bin
            bin_data_pc1=Bits(int=digital_data_pc1[j], length=16).bin
            bin_data_pc2=Bits(int=digital_data_pc2[j], length=16).bin
            if k<4:
                txtfile.write('    r_ch1_data'+str(k)+' <= '+'\"'+bin_data_s+'\"'+';\n')
                txtfile.write('    r_ch2_data'+str(k)+' <= '+'\"'+bin_data_r+'\"'+';\n')
                txtfile.write('    r_PC_port_1_data'+str(k)+' <= '+'\"'+bin_data_pc1+'\"'+';\n')
                txtfile.write('    r_PC_port_2_data'+str(k)+' <= '+'\"'+bin_data_pc2+'\"'+';\n')
                k+=1
            else:
                txtfile.write('    r_ch1_data'+str(k)+' <= '+'\"'+bin_data_s+'\"'+';\n')
                txtfile.write('    r_ch2_data'+str(k)+' <= '+'\"'+bin_data_r+'\"'+';\n')
                txtfile.write('    r_PC_port_1_data'+str(k)+' <= '+'\"'+bin_data_pc1+'\"'+';\n')
                txtfile.write('    r_PC_port_2_data'+str(k)+' <= '+'\"'+bin_data_pc2+'\"'+';\n')
                txtfile.write('    output_tmp := to_integer(signed(SI));\n')
                txtfile.write('    WRITE (line_out, output_tmp);\n')
                txtfile.write('    WRITELINE(file_out, line_out);\n')
                txtfile.write('    wait for 10 ns;\n')
                k=0
                
if 1:                
    j=0
    with open(directory + filename, 'w') as txtfile:
        for j in range (n):
            bin_data_i=Bits(int=digital_data_i[j], length=16).bin
            bin_data_a=bin(digital_data_a[j])[2:].zfill(16)
        
            txtfile.write('    r_N_in <= '+'\"'+bin_data_i+'\"'+';\n')
            txtfile.write('    r_D_in <= '+'\"'+bin_data_a+'\"'+';\n')
            txtfile.write('    output_tmp := to_integer(signed(w_Q_out));\n')
            txtfile.write('    WRITE (line_out, output_tmp);\n')
            txtfile.write('    WRITELINE(file_out, line_out);\n')
            txtfile.write('    wait for 10 ns;\n')
            
    with open(directory + 'div_expected.txt', 'w') as txtfile:
        for j in range (n):
            bin_data_result=str(digital_data_i[j]/(digital_data_a[j]+0.))
            txtfile.write(bin_data_result+'\n')
