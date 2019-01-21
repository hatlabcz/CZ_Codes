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

filename = "C:\Users\zctid.LAPTOP-150KME16\Desktop\\test2.vcl"  


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
            temp = np.binary_repr(ord(data[-1008:-504][8*j + digit]), 8)
            double_float+=temp
        data_list[j] = bin_to_float(double_float)
    return data_list


def show_realtime_data(i):
    x=read_log(filename)[2]
    y=read_log(filename)[38]
    xar.append(x)
    yar.append(y)
    ax1.clear()
    ax1.plot(xar,yar)




#history_fig,history_length= plot_history(filename,minutes=300)


fig = plt.figure(1)
ax1 = fig.add_subplot(1,1,1)
xar = (history_data(filename,50)[:,2]).tolist()  #time
yar = (history_data(filename,50)[:,38]).tolist() # MC plate RuO2

ani = animation.FuncAnimation(fig, show_realtime_data, interval=1000)


#while i < 1000:
#y = np.random.random()
#    plt.scatter(i, y)
#    plt.pause(0.05)


#plt.figure('MC Plate RuO2 T(K)')
#plt.plot(data_history[:,2],data_history[:,38])  


#for i in range(10):
#    y = np.random.random()
#    plt.scatter(i, y)
#    plt.pause(0.05)
#
#plt.show()




