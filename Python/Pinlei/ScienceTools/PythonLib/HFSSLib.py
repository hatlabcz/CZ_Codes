# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 11:16:47 2018

@author: Hat_Pinlei
"""

import csv
import numpy as np
import math
import matplotlib.pyplot as plt
import hycohanz as hfss
import h5py


class hfssfile():
    def __init__(self,path,filename,projectname):
        [self.oAnsoftApp, self.oDesktop] = hfss.setup_interface()     
        self.oDesktop.OpenProject(path+filename)
        self.oProject = self.oDesktop.SetActiveProject(projectname)
        self.oDesign = self.oProject.SetActiveDesign("HFSSDesign1")
        self.oEditor = self.oDesign.SetActiveEditor("3D Modeler")        

    def changeParameter(self,name,value):
        self.oDesign.ChangeProperty(
        	[
        		"NAME:AllTabs",
        		[
        			"NAME:LocalVariableTab",
        			[
        				"NAME:PropServers", 
        				"LocalVariables"
        			],
        			[
        				"NAME:ChangedProps",
        				[
        					"NAME:"  + name,
        					"Value:=", value
        				]
        			]
        		]
        	])    
    
        
    
    
    
    
    def AnalyzeAll(self):
        self.oDesign.AnalyzeAll()

    def savefile(self):
        self.oProject.Save()

    def quitProgram(self):
        hfss.quit_application(self.oDesktop)            
        del self.oDesign
        del self.oProject 
        del self.oDesktop
        del self.oAnsoftApp
#        del self.oModule  

if __name__=='__main__':
    path = r'E:\LabProject\Experiment\FrequencyComb\Server\\'
    filename = 'FrequencyCombV3(Eigen).aedt'
    non = hfssfile(path,filename,'FrequencyCombV3(Eigen)')
    for i in range(101):
        Lj = i * 0.01 
        non.changeParameter("Lj",str(Lj)+'nH')
        non.AnalyzeAll()
        non.savefile()

    
    