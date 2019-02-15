# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:18:25 2018

@author: Hat_Pinlei
"""

import Tkinter as tk
import os
import re
#from PIL import Image, ImageTk
current_path = os.getcwd()
#directory = re.findall(r'(.*\\HatCode)',current_path,re.S)[0]


def wrong_window(Output):
    temp = tk.Toplevel()
    temp.title("Something Wrong, mortal!!!")
    temp.geometry('300x100+500+300')

    def trick_window():
        temp = tk.Toplevel()
        temp.title("Something Wrong, mortal!!!")
        temp.geometry('300x100+500+300')
        label = tk.Label(temp, text = "You're so bad!")
        label.grid(row = 0)        
        button2 = tk.Button(temp, text = "Close", command = temp.destroy)
        button2.grid(row = 1)
    label = tk.Label(temp, text = Output, wraplength = 300)
    label.grid(row = 0)
    button1 = tk.Button(temp, text = "Ha?", command = trick_window)
    button1.grid(row = 1)
    button2 = tk.Button(temp, text = "Fine, I got it", command = temp.destroy)
    button2.grid(row = 2)
    return

def simple_window(title,content):
    temp = tk.Toplevel()
    temp.title(title)
    temp.geometry('300x100+500+300')    
    label = tk.Label(temp, text = content, wraplength = 300)
    label.grid(row = 0)
    button1 = tk.Button(temp, text = "Close", command = temp.destroy)
    button1.grid(row = 1)    

def input_label_func(window_name, keys, units, row_init = 0, column_init = 0, grid = None, entry_init = None, width = 20):
    '''
    window_name: Tk window name
    keys: list of all the input entry name
    units: the units of the input
    '''
    label_set = []
    entry_set = []
    unit_set = []
    if grid == None:
        for i in range(len(keys)):
            '''
            There are three parts you need to combine:
            1. name of parameter (list)
            2. input entry of parameter
            3. units (list)
            '''
            label_temp = tk.Label(window_name,text=keys[i])
            label_temp.grid(row = i + row_init, column = column_init)
            label_set.append(label_temp)
            entry_temp = tk.Entry(window_name, width = width)
            entry_temp.grid(row = i + row_init, column = column_init + 1)
            if entry_init != None:
                entry_temp.insert(0,str(entry_init[i]))
            entry_set.append(entry_temp)
            unit_temp = tk.Label(window_name,text=units[i])
            unit_temp.grid(row = i + row_init, column = column_init + 2)
            unit_set.append(unit_temp)
    else:
        num = 0
        for row in range(int(grid[0])):
            for column in range(int(grid[1])):
                label_temp = tk.Label(window_name,text=keys[num])
                label_temp.grid(row = row + row_init, column = 3*column + column_init)
                label_set.append(label_temp)
                entry_temp = tk.Entry(window_name, width = width)
                entry_temp.grid(row = row + row_init, column = 3*column + column_init + 1)
                if entry_init != None:
                    entry_temp.insert(0,str(entry_init[num]))
                entry_set.append(entry_temp)
                unit_temp = tk.Label(window_name,text=units[num])
                unit_temp.grid(row = row + row_init, column = 3*column + column_init + 2)
                unit_set.append(unit_temp)                
                num += 1
    return entry_set

def advanced_input_label(window_name, keys, units, row_init = 0, column_init = 0, grid = None, entry_init = None, width = 20):
    '''
    window_name: Tk window name
    keys: list of all the input entry name
    units: the units of the input
    '''
    label_set = []
    entry_set = []
    unit_set = []
    if grid == None:
        for i in range(len(keys)):
            '''
            There are three parts you need to combine:
            1. name of parameter (list)
            2. input entry of parameter
            3. units (list)
            '''
            label_temp = tk.Label(window_name,text=keys[i])
            label_temp.grid(row = i + row_init, column = column_init)
            label_set.append(label_temp)
            entry_temp = tk.Entry(window_name, width = width)
            entry_temp.grid(row = i + row_init, column = column_init + 1)
            if entry_init != None:
                entry_temp.insert(0,str(entry_init[i]))
            entry_set.append(entry_temp)
            unit_temp = tk.Label(window_name,text=units[i])
            unit_temp.grid(row = i + row_init, column = column_init + 2)
            unit_set.append(unit_temp)
    else:
        num = 0
        for row in range(int(grid[0])):
            for column in range(int(grid[1])):
                label_temp = tk.Label(window_name,text=keys[num])
                label_temp.grid(row = row + row_init, column = 3*column + column_init)
                label_set.append(label_temp)
                entry_temp = tk.Entry(window_name, width = width)
                entry_temp.grid(row = row + row_init, column = 3*column + column_init + 1)
                if entry_init != None:
                    entry_temp.insert(0,str(entry_init[num]))
                entry_set.append(entry_temp)
                unit_temp = tk.Label(window_name,text=units[num])
                unit_temp.grid(row = row + row_init, column = 3*column + column_init + 2)
                unit_set.append(unit_temp)                
                num += 1
    return label_set, entry_set, unit_set

def text_show(window_name, keys, text, units, row_init = 0, column_init = 0, grid = None):
    label_set = []
    text_set = []
    unit_set = []
    if grid == None:
        for i in range(len(keys)):
            '''
            There are three parts you need to combine:
            1. name of parameter (list)
            2. input entry of parameter
            3. units (list)
            '''
            label_temp = tk.Label(window_name,text=keys[i])
            label_temp.grid(row = i + row_init, column = column_init)
            label_set.append(label_temp)
            text_temp = tk.Text(window_name)
            text_temp.grid(row = i + row_init, column = column_init + 1)
#            text_temp.insert(tk.END,str(text[i]))
            text_set.append(text_temp)
            unit_temp = tk.Label(window_name,text=units[i])
            unit_temp.grid(row = i + row_init, column = column_init + 2)
            unit_set.append(unit_temp)
    else:
        num = 0
        for row in range(int(grid[0])):
            for column in range(int(grid[1])):
                label_temp = tk.Label(window_name,text=keys[num])
                label_temp.grid(row = row + row_init, column = 3*column + column_init)
                label_set.append(label_temp)
                text_temp = tk.Text(window_name)
                text_temp.grid(row = i + row_init, column = column_init + 1)
                text_temp.insert(tk.END,str(text[i]))
                text_set.append(text_temp)
                unit_temp = tk.Label(window_name,text=units[num])
                unit_temp.grid(row = row + row_init, column = 3*column + column_init + 2)
                unit_set.append(unit_temp)                
                num += 1
    return text_set
   

if __name__ == '__main__':
    print 'Hello, Pinlei'