# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:10:21 2017

@author: HatLabUnderGrad2
"""

# Transmission fitting

# -*- coding: utf-8 -*-
"""
Created on Thu May 11 00:04:18 2017

@author: CaoXi
"""

# Fit transmission data
# Dear Alex, this is the method we need to add to the library.
import numpy as np
import lmfit as lmf
import matplotlib.pyplot as plt


def transmission_fit(params, f, do_float = True):
    '''
    This is the model will be used for the fitting.
    
    Input:
        params (dict type), include all the initial guess for the fitting
        f (np.array), the frequency
        do_float (boolean), control if we want the output to be float number or complex number
    Output:
        value of S21, float or complex number
    Raises:
        None
    '''
    value = params.valuesdict() 
    f0 = value['f0']
    Q1 = value['Q1']
    Q2 = value['Q2']
    A = value['A']
    B = value['B']
    C = value['C']
    
    omega = f
    omega0 = f0    
    q1 = np.sqrt(1.0/Q1)
    q2 = np.sqrt(1.0/Q2)
    delta = - omega + omega0
    k1 = (q1**2)*omega
    k2 = (q2**2)*omega
    T0 = np.sqrt(k1*k2)/((k1+k2)/2.0)
    S21 = C*T0/(1-1j*delta/((k1+k2)/2.0))*np.exp(1j*(A*omega + B))

    if not do_float:
        return S21
    return S21.view(np.float)

    
def residuals(params, real, imag, f):
    '''
    The difference between the data value and our fitting model value.
    The lmfit tries to minize this to get the best fit.
    
    Input:
        params (dict type), include all the initial guess for the fitting
        real (np.array), the real part of the data
        imag (np.array), the imag part of the data
        f (np.array), the frequency     
    Output:
        A np.array gives the difference between the fit and the data
    Raises:
        None
    '''
    S11_fit = transmission_fit(params, f)
    data = real + 1j*imag 
    return S11_fit - np.array(data).view(np.float)
    
   
def Fit(f, real, imag, Params):
    '''
    This function does the fit of the data. 
    
    Input:
        f (np.array), the frequency 
        real (np.array), the real part of the data
        imag (np.array), the imag part of the data        
        Params (dict type), include all the initial guess for the fitting
    Output:
        the result of this fitting
    Raises:
        None
    '''
    fit_params = lmf.Parameters()
    fit_params.add('f0', value = Params['f0guess'], vary=True)
    fit_params.add('Q1',value = Params['Q1'], min = 0.0,  vary = True)
    fit_params.add('Q2',value = Params['Q2'], min = 0.0,  vary = True)
    fit_params.add('A',value = Params['A'], min = -10, max = 10, vary = True)
    fit_params.add('B',value = Params['B'], min = 0.0, max = 2*np.pi, vary = True)
    fit_params.add('C',value = Params['C'], min = 0.0, vary = False)   # Parameter C is fixed for now
    
    out=lmf.minimize(residuals, fit_params, args=(real, imag, f))

    return out

def read_data(filename):
    '''
    Read the data from the file.
    TODO: this only works for the txt file from microwave office. Need add more read_data function for hdf5, csv, etc. 
    
    Input:
        filename (string), the name of the data file include the path
    Output:
        (frequency, real part of the data, imag part of the data)
    '''
    rawdata = np.genfromtxt(filename, delimiter='\t', skip_header=1)
    return (rawdata[:,0], rawdata[:,1], rawdata[:,2])


def plot(out, f, data_real, data_imag):
    '''
    Plot the result of the fit.
    
    Input :
        out (class 'lmfit.minimizer.Minimizer'), the result class from lmfit for the fitting
        f (np.array), the frequency 
        data_real (np.array), the real part of the data
        data_imag (np.array), the imag part of the data  
    Output:
        None
    Raises:
        None        
    '''
    
    data_mag = np.sqrt(data_real**2 + data_imag**2)
    data_phase = np.arctan2(data_imag, data_real)
    
    fit_result = transmission_fit(out.params, f)    
    fit_real = fit_result[0:len(fit_result):2]
    fit_imag = fit_result[1:len(fit_result):2]
    fit_mag = np.sqrt(fit_real**2 + fit_imag**2)
    fit_phase = np.arctan2(fit_imag, fit_real)
    
    plt.close('all')
    plt.figure(1)
    plt.plot(f, data_mag, 'b')
    plt.plot(f, fit_mag, 'r')
    plt.title('Mag')
    plt.legend(['data', 'fit'])
    
    plt.figure(2)
    plt.plot(f, data_phase, 'b')
    plt.plot(f, fit_phase, 'r')
    plt.title('Phase')
    plt.legend(['data', 'fit'])

    plt.figure(3)
    plt.plot(data_real, data_imag, 'b')
    plt.plot(fit_real, fit_imag, 'r')
    plt.xlim([-1,1])
    plt.ylim([-1,1])
    plt.title('Smith Chart')
    plt.legend(['data', 'fit'])

    plt.figure(4)
    plt.plot(f, data_real, 'b')
    plt.plot(f, fit_real, 'r')
    plt.title('Real')
    plt.legend(['data', 'fit'])

    plt.figure(5)
    plt.plot(f, data_imag, 'b')
    plt.plot(f, fit_imag, 'r')
    plt.title('Imag')
    plt.legend(['data', 'fit'])

def param_guessing(data_real, data_imag):
    '''
    Read the raw data and gives the initial guess for the fitting. 
    
    Input:
        data_real (np.array), the real part of the data
        data_imag (np.array), the imag part of the data  
    Output:
        f0 (float number), the resonant frequency
        Q1 (float number), the quanlity factor of coupling capacitor 1
        Q2 (float number), the quanlity factor of coupling capacitor 2
        A (float number), the slope for the phase correction 
        B (float number), the intersection for the phase correction
    Raises:
        None
    '''
    mag = np.sqrt(data_real**2 + data_imag**2)
    data_phase = np.arctan2(data_imag, data_real)
    
    A = (data_phase[10]-data_phase[0])/(f[10]-f[0])/(2*np.pi)
    B = -A*f[0] + data_phase[0]
        
    f0 = f[mag.tolist().index(max(mag))]
    mag_max = mag.max()
    left_bw = f[np.where(mag>mag.max()/2)[0][0]]
    right_bw = f[np.where(mag>mag.max()/2)[0][-1]]
    Q_tot = 2*f0/(right_bw - left_bw)
    Q1 = 4*Q_tot*(1 - np.sqrt(1-mag_max**2))/(2*mag_max**2)
    Q2 = 4*Q_tot*(1 + np.sqrt(1-mag_max**2))/(2*mag_max**2)
    return (f0, Q1, Q2, A, -B)
    

    
if __name__ == '__main__':
    datafile = 'E:\\Box Sync\\XC\\Theory project\\2017_05_11_Fitting Function\\test8.txt'
    (f, data_real, data_imag) = read_data(datafile)  
    (f0guess, Q1_guess, Q2_guess, A_guess, B_guess) = param_guessing(data_real, data_imag)     
    print (f0guess, Q1_guess, Q2_guess, A_guess, B_guess)
    fitting_params = {'f0guess': f0guess, 'Q1':Q1_guess, 'Q2':Q2_guess, 'A':A_guess, 'B':B_guess, 'C':1.0}
    result = Fit(f, data_real, data_imag, fitting_params)
    print lmf.fit_report(result)
    plot(result, f, data_real, data_imag)    
    
    
    
    
    