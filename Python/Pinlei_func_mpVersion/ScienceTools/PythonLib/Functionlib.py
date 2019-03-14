# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:03:05 2018

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
import math
import lmfit
import IOlib as IOL
import scipy.optimize as opt
from matplotlib.patches import Circle, Wedge, Polygon

######################### Constant ############################################
const_h = 6.62607004*1e-34 # m^2 kg /s
const_e = 1.6021765*1e-19 # C
###############################################################################


def smooth(y, window_size, order, deriv=0, rate=1):
    '''    
    This function is for smoothing the data.
    
    Input:
        y: the raw data you want to smooth;
        window_size: represents the width, in samples, of a discrete-time, 
                     symmetrical window function
        order: the order of polynomial you want to fit the raw data
        
    Output:
        numpy array. The data which has been smoothed
    '''
    
    window_size = np.abs(np.int(window_size))
    order = np.abs(np.int(order))
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * math.factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')


class BaseProgressBar(object):
    """
    An abstract progress bar with some shared functionality.

    Example usage:

        n_vec = linspace(0, 10, 100)
        pbar = TextProgressBar(len(n_vec))
        for n in n_vec:
            pbar.update(n)
            compute_with_n(n)
        pbar.finished()

    """

    def __init__(self, iterations=0, chunk_size=10):
        pass

    def start(self, iterations, chunk_size=10):
        self.N = float(iterations)
        self.p_chunk_size = chunk_size
        self.p_chunk = chunk_size
        self.t_start = time.time()

    def update(self, n):
        pass

    def time_elapsed(self):
        return "%6.2fs" % (time.time() - self.t_start)

    def time_remaining_est(self, p):
        if p > 0.0:
            t_r_est = (time.time() - self.t_start) * (100.0 - p) / p
        else:
            t_r_est = 0

        dd = datetime.datetime(1, 1, 1) + datetime.timedelta(seconds=t_r_est)
        time_string = "%02d:%02d:%02d:%02d" % \
            (dd.day - 1, dd.hour, dd.minute, dd.second)

        return time_string

    def finished(self):
        pass


class TextBar(BaseProgressBar):
    """
    A simple text-based progress bar.
    """

    def __init__(self, iterations=0, chunk_size=10):
        super(TextBar, self).start(iterations, chunk_size)

    def update(self, n):
        p = (n / self.N) * 100.0
        if p >= self.p_chunk:
            print("%4.1f%%." % p +
                  " Run time: %s." % self.time_elapsed() +
                  " Est. time left: %s" % self.time_remaining_est(p))
            sys.stdout.flush()
            self.p_chunk += self.p_chunk_size

    def finished(self):
        self.t_done = time.time()
        print("Total run time: %s" % self.time_elapsed())


class FancyBar(BaseProgressBar):
    """
    An enhanced text-based progress bar.
    """

    def __init__(self, iterations=0, chunk_size=10):
        super(FancyBar, self).start(iterations, chunk_size)
        self.fill_char = '*'
        self.width = 25

    def update(self, n):
        percent_done = int(round(n / self.N * 100.0))
        all_full = self.width - 2
        num_hashes = int(round((percent_done / 100.0) * all_full))
        prog_bar = ('[' + self.fill_char * num_hashes +
                    ' ' * (all_full - num_hashes) + ']')
        pct_place = (len(prog_bar) // 2) - len(str(percent_done))
        pct_string = '%d%%' % percent_done
        prog_bar = (prog_bar[0:pct_place] +
                    (pct_string + prog_bar[pct_place + len(pct_string):]))
        prog_bar += ' Elapsed %s / Remaining %s' % (
            self.time_elapsed().strip(),
            self.time_remaining_est(percent_done))
        sys.stdout.write("\r"+prog_bar)
        sys.stdout.flush()

    def finished(self):
        self.t_done = time.time()
        print("\r", "Total run time: %s" % self.time_elapsed())



def func(params,xvalue):

    value = params.valuesdict()
    a = value['a']
    b = value['b']

    func = 1.0/(np.sqrt((a + xvalue) * 1e-9 * b * 1e-12) * 2*np.pi)
    return func


def residual(params,model,xvalue,yvalue):
    return func(params,xvalue) - yvalue

def fit(xvalue,yavlue,iniguess):
    params = lmfit.Parameters()
    params.add('a', value = iniguess['a'])
    params.add('b', value = iniguess['b'])

    result = lmfit.minimize(residual,params,args = (func, xvalue, yavlue))
    return result


def twoD_Gaussian((x, y), amplitude, xo, yo, sigma_x, sigma_y, theta, offset):
    xo = float(xo)
    yo = float(yo)    
    a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
    b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
    c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)
    g = offset + amplitude*np.exp( - (a*((x-xo)**2) + 2*b*(x-xo)*(y-yo) 
                            + c*((y-yo)**2)))
    return g.ravel()   
    
def two_blob((x,y), amp1,amp2, xo1, yo1, xo2, yo2, sigma_x_1, sigma_y_1, sigma_x_2, sigma_y_2, theta, offset):
    return twoD_Gaussian((x,y), amp1, xo1, yo1, sigma_x_1, sigma_y_1, theta, offset) \
            + twoD_Gaussian((x,y), amp2, xo2, yo2, sigma_x_2, sigma_y_2, theta, offset)




if __name__ == '__main__':
    plt.close('all')
    path = r"E:\CodeTest\\"
    filename = "data.h5py"
    #    read_txt(path,filename)
    #    path = r'E:\Data\FC\\'
    #    path = create_directory(path, with_time = True)
#    x,y = read_hfsscsv(path, filename)
#    plt.plot(x,y)
#    plt.show()
    plt.close('all')
    value = IOL.read_h5(path,filename,item = 'IQ')
    value = value# * np.exp(-1j * 0.35 * 2 * np.pi)
    I = np.real(value)[:,0]
    Q = np.imag(value)[:,0]    
    plt.figure()
    dim = 101
    value2d = plt.hist2d(I,Q,bins = dim, cmap=plt.cm.jet)
    before_fit = value2d[0].transpose().ravel()
        
#    initial_guess = (3,100,100,20,40,0,10)
#    
#    data_noisy = data + 0.2*np.random.normal(size=data.shape)
#    
#    popt, pcov = opt.curve_fit(twoD_Gaussian, (x, y), data_noisy, p0=initial_guess)    
    x = np.linspace(np.min(value2d[1]), np.max(value2d[1]), dim)
    y = np.linspace(np.min(value2d[2]), np.max(value2d[2]), dim)
    x, y = np.meshgrid(x, y)

    initial_guess = (40,15,-3,-11,-14,4,5,5,5,5,0,0)
    popt, pcov = opt.curve_fit(two_blob, (x, y), before_fit, p0=initial_guess,maxfev = 5000)
    
#    data_fitted = twoD_Gaussian((x, y), *popt)
    data_fitted  = two_blob((x,y),*popt)
    fig, ax = plt.subplots(1, 1)
    ax.imshow(before_fit.reshape(dim, dim), cmap=plt.cm.jet, origin='bottom',
        extent=(x.min(), x.max(), y.min(), y.max()))
#    ax.contour(x, y, data_fitted.reshape(dim, dim), 3, colors='w')
    wedge1 = Wedge((popt[2],popt[3]),np.sqrt(popt[6]**2+popt[7]**2)*2,0,360,width = 0.5)
    wedge2 = Wedge((popt[4],popt[5]),np.sqrt(popt[8]**2+popt[9]**2)*2,0,360,width = 0.5)
    circle1 = Circle((popt[2],popt[3]),np.sqrt(popt[6]**2+popt[7]**2)*2)
    circle2 = Circle((popt[4],popt[5]),np.sqrt(popt[8]**2+popt[9]**2)*2)
    ax.add_patch(wedge1)
    ax.add_patch(wedge2)
    plt.show()
    sum1 = np.array(0.0)
    for i in range(len(value2d[1])):
        for j in range(len(value2d[2])):
            if circle1.contains_point((value2d[1][i],value2d[2][j])):
#                plt.plot(value2d[1][i],value2d[2][j],'r+')
                sum1 += value2d[0][i,j]
                
    sum2 = np.array(0.0)
    for i in range(len(value2d[1])):
        for j in range(len(value2d[2])):
            if circle2.contains_point((value2d[1][i],value2d[2][j])):
#                plt.plot(value2d[1][i],value2d[2][j],'r+')
                sum2 += value2d[0][i,j]
                
    sum1_percent = sum1/(sum1+sum2)
    sum2_percent = sum2/(sum1+sum2)
    print '------------------one:------------------'
    print 'center: ', np.round((popt[2],popt[3]),decimals = 4)
    print 'amp: ', np.around(popt[0],decimals = 4)
    print 'sigma x: ', np.round(popt[5],decimals = 4), \
            ';sigma y: ', np.around(popt[6],decimals = 4)
    print 'count', sum1, 'percentage', \
            np.around(sum1_percent,decimals = 4) * 100.0, '%'
    
    print '------------------two:------------------'
    print 'center: ', np.round((popt[4],popt[5]),decimals = 4)
    print 'amp: ', np.around(popt[1],decimals = 4)
    print 'sigma x: ', np.round(popt[7],decimals = 4), \
            ';sigma y: ', np.around(popt[8],decimals = 4)
    print 'count', sum2, 'percentage', \
            np.around(sum2_percent,decimals = 4) * 100.0, '%'
    
                
    # Create x and y indices
#    x = np.linspace(-40, 40, 201)
#    y = np.linspace(-40, 40, 201)
#    x, y = np.meshgrid(x, y)
    
#    #create data
#    data1 = twoD_Gaussian((x, y), 20, 20, 20, 5, 5, 0, 0) 
#    data2 = twoD_Gaussian((x, y), 40, 0, 5, 5, 5, 0, 0)
#    data = data1 + data2
#    # plot twoD_Gaussian data generated above
#    plt.figure()
#    plt.imshow(data.reshape(201, 201))
#    plt.colorbar()
#    
#    
#    
#    fig, ax = plt.subplots(1, 1)
##    ax.hold(True)
#    ax.imshow(data.reshape(201, 201), cmap=plt.cm.jet, origin='bottom',
#        extent=(x.min(), x.max(), y.min(), y.max()))
#    ax.contour(x, y, data.reshape(201, 201), 3, colors='w')
#    plt.show()
#    
    # bar = TextBar(100)
    # for i in range(100):
    #     bar.update(i)
    #     time.sleep(0.1)
    # bar.finished
#    path = r"E:\Data\FC\2018_05_07\\"
#    filename = "res_fre.csv"
#    #    read_txt(path,filename)
#    #    path = r'E:\Data\FC\\'
#    #    path = create_directory(path, with_time = True)
#    x,y = IOL.read_hfsscsv(path, filename)
#    iniguess = {'a': 2.5,
#                'b': 0.2}
#    res = fit(x,y,iniguess)
#    
#    fity = func(res.params, x)
#    plt.plot(x,fity)
#    plt.plot(x,y)
#    plt.show()
#    print res.params.valuesdict()