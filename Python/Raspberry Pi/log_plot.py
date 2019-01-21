# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 15:38:41 2018

@author: zctid
"""


#data = read[12288:]
#j=0
#double_float = ""
#for i in range(8):
#    digit = 7-i
#    temp = np.binary_repr(ord(data[-1008:-504][8*j + digit]), 8)
#    double_float+=temp

import threading
import time
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
import struct
import smtplib
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.animation as animation

filename = r"\\OI-PC\Hatridge\\log 181215 165937.vcl"


def bin_to_float(b):
    """ Convert binary string to a float. """
    bf = int_to_bytes(int(b, 2), 8)  # 8 bytes needed for IEEE 754 binary64.
    return struct.unpack('>d', bf)[0]

def int_to_bytes(n, minlen=0):  # Helper function
    nbits = n.bit_length() + (1 if n < 0 else 0)  # +1 for any sign bit.
    nbytes = (nbits+7) // 8  # Number of whole bytes.
    b = bytearray()
    for _ in range(nbytes):
        b.append(n & 0xff)
        n >>= 8
    if minlen and len(b) < minlen: 
        b.extend([0] * (minlen-len(b)))
    return bytearray(reversed(b))  # High bytes first.

def plot_history(filename,minutes):
    """
    Polt the history
    """

    file_ = open(filename, "rb")
    read = file_.read()
    data = read[12288:]
    
    lines=int(minutes)
    offset=len(data)-504*lines
    
    data_history = np.zeros((lines,63))
    for k in range(lines):
        for j in range(63):
            double_float = ""
            for i in range(8):
                digit = 7-i
                temp = np.binary_repr(ord(data[k*504+offset:(k+1)*504+offset][8*j + digit]), 8)
                double_float+=temp
            data_history[k,j] = bin_to_float(double_float)
    
    history_time=map(datetime.fromtimestamp,data_history[:,2]) #set time axis format
    
    
    MCRuO2fig, ax = plt.subplots(1,num='MC Plate RuO2 T(K)')
    MCRuO2fig.autofmt_xdate()
    plt.plot(history_time, data_history[:,38])
    xfmt = mdates.DateFormatter('%m-%d %H:%M')
    ax.xaxis.set_major_formatter(xfmt)
       
    return MCRuO2fig,len(data)
    

def history_data(filename,minutes):
    """
    Return the history data
    """

    file_ = open(filename, "rb")
    read = file_.read()
    data = read[12288:]
    
    lines=int(minutes)
    offset=len(data)-504*lines
    
    data_history = np.zeros((lines,63))
    for k in range(lines):
        for j in range(63):
            double_float = ""
            for i in range(8):
                digit = 7-i
                temp = np.binary_repr(ord(data[k*504+offset:(k+1)*504+offset][8*j + digit]), 8)
                double_float+=temp
            data_history[k,j] = bin_to_float(double_float)
               
    return data_history

    
def read_log(filename):
    """
    Return the lastest value of log file
    """
    file_ = open(filename, "rb")
    read = file_.read()
    data = read[12288:]
    data_list = np.zeros(63)
    for j in range(63):
        double_float = ""
        for i in range(8):
            digit = 7-i
            temp = np.binary_repr(ord(data[-504:][8*j + digit]), 8)
            double_float+=temp
        data_list[j] = bin_to_float(double_float)
    return data_list


def show_realtime_data(i):
    t=datetime.fromtimestamp(read_log(filename)[2])     #time
    tem=read_log(filename)[38] #temperature
    t_list.append(t)
    tem_list.append(tem)
    real_time_plot.clear()  
    real_time_plot.plot(t_list, tem_list)
    xfmt = mdates.DateFormatter('%m-%d %H:%M')
    real_time_plot.xaxis.set_major_formatter(xfmt)
    print 1
    fig.savefig('plot.png')



#history_fig,history_length= plot_history(filename,minutes=300)



time_back=30
fig = plt.figure('MC Plate RuO2 T(K) Real-time')
real_time_plot = fig.add_subplot(1,1,1)  
t_list = map(datetime.fromtimestamp,history_data(filename,time_back)[:,2])  #time
tem_list = (history_data(filename,time_back)[:,38]).tolist() # MC plate RuO2

ani = animation.FuncAnimation(fig, show_realtime_data, interval=30)







