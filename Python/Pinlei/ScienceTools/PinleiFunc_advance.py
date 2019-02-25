# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:43:46 2018

@author: Hat_Pinlei
"""

import Tkinter as tk
import os
import re
directory = re.findall(r'(.*\\ScienceTools)',os.getcwd(),re.S)[0]
#idle = re.findall(r'(.*\\Python)',os.getcwd(),re.S)[0]
import sys
sys.path.append(directory+'\\Package')  
#sys.path.append(idle+'\\PythonLib')
import QubitFunc_MultiMode as QF

root = tk.Tk()
root.geometry('800x600+500+300')
root.title('Pinlei Function')
root.wm_iconbitmap(directory + '\\scriptL.ico')




tk.Label(root, text = '          Constants Related          ').grid(column = 0, row = 0)
tk.Label(root, text = '          Qubit Related          ').grid(column = 1, row = 0)
tk.Label(root, text = '          JPC Related          ').grid(column = 2, row = 0)
     
tk.Button(root, text = 'Calculation of JJ', width = 15,
          command = QF.cal_junction).grid(column = 1, row = 1)
tk.Button(root, text = 'BBQ Analysis', width = 15,
          command = QF.hfss_simulation).grid(column = 1, row = 2)


root.mainloop()