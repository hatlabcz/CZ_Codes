# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:04:49 2018

@author: Hat_Pinlei
"""

import sys
sys.path.append(r'E:\Python\PythonLib')
sys.path.append(r'E:\GoogleDrive\Python\PythonLib')
import time
import datetime
import h5py
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as color
from matplotlib.widgets import Cursor
import numpy as np
import os
import csv
import math
import matplotlib
import IOlib as IOL

def hist2d(dddata,xaxis = None,xname = None,yaxis = None,yname = None, xnum = 6, ynum = 11, colorbarname = 'Colorbar', title = 'Runing Sweep'):
    dddata = np.ma.masked_invalid(dddata)    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.ion()
#    levels=[180, 90, 0, -90, -180]
#    colors=[color.hex2color('#000000'), color.hex2color('#FF0000'), 
#            color.hex2color('#FFFF00'), color.hex2color('#00FF00'),
#            color.hex2color('#000000')]
#    levels=levels[::-1]
#    colors=colors[::-1]
#    
#    _cmap=color.LinearSegmentedColormap.from_list('my_cmap', colors)
#    _norm=color.Normalize(vmin=-180, vmax=180)
    IMAGE = ax.imshow(dddata, interpolation='nearest', 
                      aspect='auto', origin = 'lower')
    ax.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(numticks = ynum))
    ax.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(numticks = 6))
    plt.title('Running Sweep')
    xaxis = np.around(np.linspace(min(xaxis),max(xaxis),xnum),decimals =2)
    yaxis = np.around(np.linspace(min(yaxis),max(yaxis), ynum),decimals = 2)
    ax.set_xticklabels(xaxis)
    ax.set_xlabel(xname)
    ax.set_yticklabels(yaxis)
    ax.set_ylabel(yname)
    cbar = fig.colorbar(IMAGE)
#    cbar.set_ticks(levels)
    cbar.set_label(colorbarname)
    def format_coord(x,y):
        '''
        Changes the corner text to give the data behind the point the 
        cursor is hovering over
            Args:
                x (float) : the x coordinate
                y (float) : the y coordinate
        '''
        
        ar_xdata = np.linspace(-100,0,num = 101) 
        ar_ydata = np.linspace(-120,-70, num = 251)
        ar_phase = dddata
        x_index = int(x+.5)
        if x_index >= len(ar_xdata):
            x_index = len(ar_xdata) - 1
        y_index = int(y + .5)
        if y_index >= len(ar_ydata):
            y_index = len(ar_ydata) - 1
        xco = ar_xdata[x_index]
        yco = ar_ydata[y_index]
        phase = ar_phase[y_index][x_index]
        return ('Detuning = {} MHz, Power = {} dBm, Interval = {} MHz'.format(xco, yco, phase))
    ax.format_coord = format_coord
#    ax.patch.set(hatch='x', edgecolor='black')
    plt.tight_layout()
    
    
    
def phase2d(dddata,xaxis = None,xname = None,yaxis = None,yname = None, xnum = 6, ynum = 11, title = 'Runing Sweep'):
    dddata = np.ma.masked_invalid(dddata)    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.ion()
    levels=[180, 90, 0, -90, -180]
    colors=[color.hex2color('#000000'), color.hex2color('#FF0000'), 
            color.hex2color('#FFFF00'), color.hex2color('#00FF00'),
            color.hex2color('#000000')]
    levels=levels[::-1]
    colors=colors[::-1]
    
    _cmap=color.LinearSegmentedColormap.from_list('my_cmap', colors)
    _norm=color.Normalize(vmin=-180, vmax=180)
    IMAGE = ax.imshow(dddata[:,::-1], interpolation='nearest', 
                      aspect='auto', origin = 'lower', cmap=_cmap, norm=_norm,)
    ax.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(numticks = ynum))
    ax.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(numticks = 6))
    plt.title('Running Sweep')
    
    xaxis = np.around(np.linspace(min(xaxis),max(xaxis),xnum),decimals =2)
    yaxis = np.around(np.linspace(min(yaxis),max(yaxis), ynum),decimals = 2)
    ax.set_xticklabels(xaxis)
    ax.set_xlabel(xname)
    ax.set_yticklabels(yaxis)
    ax.set_ylabel(yname)
    cbar = fig.colorbar(IMAGE)
    cbar.set_ticks(levels)
    cbar.set_label('phase(degrees)')
    ax.patch.set(hatch='x', edgecolor='black')
    plt.tight_layout()

if __name__=='__main__' :
    plt.close('all')
    path = r'E:\Data\FC\2018_04_26\\'
    phase_sweep = IOL.read_h5(path,'phase_sweep_(2)',item = 'phase')
    yaxis = np.arange(-130,-30,0.01)
    xdata = IOL.read_h5(path,'phase_sweep_(2)',item = 'xdata')
    shadow_p = np.ma.masked_invalid(phase_sweep)
    hist2d(shadow_p,xdata,'$\Delta\omega_d$(GHz)',yaxis,'Power(dBm)')
    
    