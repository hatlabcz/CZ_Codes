import lmfit as lmf
from lmfit import Model
import numpy as np
import h5py
from hatlab import linearfit
import matplotlib.pyplot as plt
DUMMY_VALUE = 1
filename = "C:\\Users\\HatLabUnderGrads\\Box Sync\\Data\\Cooldown_2016_08_26\\2016_09_08\\JPC0014\\automatic measurement\\05_new_code_result_Exp"

def get_data(filename = filename):
    file = h5py.File(filename)
    print(file.items())
    gain_data = file['sweep_data'].value
    frequency_data = file['measure_frequencies'].value
    file.close()
    return gain_data, frequency_data

def gain(P, Pc):
    return (Pc + P)**2 / (Pc - P)**2


def Fit(omega, Params):
    fit_params = lmf.Parameters()
    fit_params.add("P", value = DUMMY_VALUE)
    fit_params.add("Pc", value = DUMMY_VALUE)
    #f_guess = omega[]
    out = lmf.minimize(model, fit_params, args = (omega))

data = get_data()
print fit_data.shape
for i in range(data[0].shape[0]):
     for j in range(data[0].shape[1]):
        fit_data[i,j] = linearfit.fit_data(data[0][i,j,:], data[1])
        print(fit_data.shape)
print(data[1])
plt.plot(fit_data[25, 500], data[1])
plt.show()
print("Complete")
