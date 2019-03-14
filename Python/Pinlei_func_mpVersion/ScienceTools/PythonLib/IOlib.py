# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:58:26 2018

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
import numpy as np
import os
import csv
from scipy.signal import argrelextrema

def create_directory(directory, extra=None, with_time=False):
    '''
    Input:
        directory: The directory you want to put
        time: A boolen, if true, then the time will automatically add
              after direcyory
        extra: the file location after the time or the directory
    Output: the path the ghost creates
    '''

    now = datetime.datetime.now()
    date_string = "{}_{:02d}_{:02d}\\".format(now.year, now.month, now.day)

    if extra != None:
        if time:
            path = directory + date_string + extra
        else:
            path = directory + extra

    if with_time:
        path = directory + date_string
    else:
        path = directory

    try:
        os.makedirs(path)
        print path + ' creates.'
    except:
        print path + ' already exists.'
    return path


def write_h5(path, filename, key1, value1, key2=None, value2=None, \
             key3=None, value3=None, key4=None, value4=None, \
             key5=None, value5=None, key6=None, value6=None):
    '''
    Input:
        path, filename

        key1: the dataname you want to store
        value1: the data value you want to store
    '''

    iterator = '_(0)'
    incrementer = 1
    saved = False
    while not saved:
        try:
            data = h5py.File(path + filename + iterator, 'w-')
            data.create_dataset(key1, data=value1)
            print filename + iterator + ':' + key1 + ' saved'
            if key2 != None:
                data.create_dataset(key2, data=value2)
                print key2 + ' saved'
            if key3 != None:
                data.create_dataset(key3, data=value3)
                print key3 + ' saved'
            if key4 != None:
                data.create_dataset(key4, data=value4)
                print key4 + ' saved'
            if key5 != None:
                data.create_dataset(key5, data=value5)
                print key5 + ' saved'
            if key6 != None:
                data.create_dataset(key6, data=value6)
                print key6 + ' saved'
            data.close()
            saved = True
        except IOError:
            iterator = "_({})".format(incrementer)
            incrementer += 1
    print path, filename + iterator, ' saved'

    return path, filename + iterator


def read_h5(path, filename, read_value=False, item=None):
    '''
    Input:
        path, filename

        read_value: A boolen, if true, it will also print the value of
                    all dataset
        item: You can specific an item you want to return
    '''

    data = h5py.File(path + filename, 'r')
    print 'Open: ' + path + filename
    for name in data:
        print 'Name: ' + name + '; and file shape: ', data[name].shape
        if read_value:
            print 'Attri Value: ', data[name].value
    if item != None:
        temp = data[item].value
    else:
        temp = 0
    data.close()
    return temp


def read_hfsscsv(path, filename):
    '''
    Input:
        path, filename

    Output: resf: yvalue
            resv: xvalue

    Function: Extract data from csv value
    '''
    with open(path + filename, 'rb') as csvres:
        result = csv.reader(csvres)
        res = list(result)
        del res[0]

    temp = np.transpose(np.array(res))
    resf = temp[0].astype(np.float)
    resv = temp[1].astype(np.float)

    return resf, resv


def read_txt(path, filename, plot=True, label=None):
    '''
    Input:
        path, filename

    Output: data

    Function: Extract data from txt value
    '''

    data = np.genfromtxt(path + filename, delimiter='\t', \
                         skip_header=1, missing_values=' ', filling_values=np.nan)
    if plot:
        plt.plot(data[:, 0], data[:, 1], label=label)
        plt.xlabel('X')
        plt.ylabel('Y')
    return data

def find_mode(x,y):
    minima, = argrelextrema(y, np.less)
    maxima, = argrelextrema(y, np.greater)
    print minima
    print maxima
    for i in range(len(minima)-1):
        for j in range(len(maxima)-1):
            if (minima[i] > maxima[j] and minima[i] < maxima[j+1]):
                if (maxima[j+1] > minima[i] and maxima[j+1] < minima[i+1]):
                    print minima[i]

def phase_find_mode(x,y):
    zero_mode_index = []    
    for i in range(len(y)-1):
        if y[i] * y[i+1] < 0 :
            zero_mode_index.append(i)
    
    mode1 = np.average(x[zero_mode_index[:2]])
    mode2 = np.average(x[zero_mode_index[-2:]])
    
    mode = np.array([mode1,mode2])
    print 'mode1', mode1, 'GHz'
    print 'mode2', mode2, 'GHz'
    
    return mode
    
    
if __name__ == '__main__':
    path = r"H:\Data\Fridge Texas\Cooldown_20180825\20180907\PXIe\qubit\test\\"
    filename = "test1_18"
    read_h5(path,filename)
    
    I_data = read_h5(path,filename, item = 'I_data')[0::2]
    Q_data = read_h5(path,filename, item = 'Q_data')[0::2]
    plt.hist2d(I_data, Q_data, bins = 101,
            range=[[-10000,10000],[-10000,10000]])
    plt.show()
    
    #    read_txt(path,filename)
    #    path = r'E:\Data\FC\\'
#    path = create_directory(path, with_time = True)
#    x,y = read_hfsscsv(path, filename)
#    plt.plot(x,y, label = 'Lj = 0.01nH')
##    phase_find_mode(x,y)
#    filename = "Lj01.csv"
#    x,y = read_hfsscsv(path, filename)
#    plt.plot(x,y, label = 'Lj = 0.1nH')
##    phase_find_mode(x,y)
#    filename = "Lj025.csv"
#    x,y = read_hfsscsv(path, filename)
#    plt.plot(x,y, label = 'Lj = 0.25nH')
##    phase_find_mode(x,y)    
#    filename = "Lj05.csv"
#    x,y = read_hfsscsv(path, filename)
#    plt.plot(x,y, label = 'Lj = 0.5nH')
#    phase_find_mode(x,y)    
#    filename = "Lj075.csv"
#    x,y = read_hfsscsv(path, filename)
#    plt.plot(x,y, label = 'Lj = 0.75nH')
##    phase_find_mode(x,y) 
#    filename = "Lj1.csv"
#    x,y = read_hfsscsv(path, filename)
#    plt.plot(x,y, label = 'Lj = 1nH')
##    phase_find_mode(x,y) 
#    plt.legend()
#    plt.plot(x[argrelextrema(y, np.less)],y[argrelextrema(y, np.less)],'r+')
#    plt.plot(x[argrelextrema(y, np.greater)],y[argrelextrema(y, np.greater)],'r+')
#    find_mode(x,y)
#    plt.show()
#    plt.figure()
#    plt.hist(I,bins = 101)
#    plt.hist(Q,bins = 101)
