# -*- coding: utf-8 -*-
"""
Created on Wed May 16 09:52:58 2018

@author: Hat_Pinlei
"""

import qutip as qt
import numpy as np

b = qt.Bloch()
vec = [0,1,0]
b.add_vectors(vec)
xz = np.zeros(20)
yz = [np.sin(th) for th in np.linspace(0, np.pi, 20)]
zz = [np.cos(th) for th in np.linspace(0, np.pi, 20)]
b.add_points([xz,yz,zz])
b.show()
