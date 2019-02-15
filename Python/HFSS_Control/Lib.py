# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 15:18:29 2017

@author: Hat_Pinlei
"""

import csv
import numpy as np
import math
import matplotlib.pyplot as plt
import hycohanz as hfss
import h5py

oDesktop=None
oAnsoftApp=None
oProject=None
oDesign=None
oModule=None

def ShowMe(filename):   
    with open (filename+".csv",'rb') as csvres:
        result = csv.reader(csvres)
        res = list(result)
        del res[0]
        
    a = np.array(res)
    b = np.transpose(a)
    
    Yvalue = b[1]
    Xvalue = b[0]
    
    plt.plot(Xvalue,Yvalue)
    plt.grid(b=None)    
    plt.show()

def calAlpAndXi(k):
    with open ('result{}.csv'.format(k),'rb') as csvres:
        result = csv.reader(csvres)
        res = list(result)
        del res[0]
    
    resf = []
    resv = []
    
    for i in res:
        resf = resf + [float(i[0])]
        resv = resv + [float(i[1])]
    
    test = []
    for i in range(len(resv)-1):
        if resv[i] < 0:
            if resv[i+1] > 0:
                test.append(i)
                if len(test) > 2:
                    break
					
    if len(test) == 1:
		test = justInCase()
	
    q = test[0]
    c = test[1]
    
    quyp = (resv[q+1]-resv[q])/(2.0*math.pi*10.0**9*(resf[q+1]-resf[q]))
    zqu = 2.0 / (((resf[q]+resf[q+1])*2.0*math.pi/2) * quyp)
    cavyp = (resv[c+1]-resv[c])/(2.0*math.pi*10.0**9*(resf[c+1]-resf[c]))
    zca = 2.0 / (((resf[c]+resf[c+1])*2.0*math.pi/2) * cavyp)
    
    e = 1.6021766208 * 10**(-19)
    cj = 0.5 * quyp
    ec = e*e / (2*cj)
    anh = - ec / (2 * math.pi * 1.05e-34) * 10**(-6)
    kc = - ((zca / zqu)**2) * ec / (2 * math.pi * 1.05e-34) * 10**(-6)
    kapa = -2 * math.sqrt(anh * kc)
    rfq = (resf[q]+resf[q+1])/2
    rfc = (resf[c]+resf[c+1])/2
    res = [anh,kapa,rfq,rfc,kc]
    print "resonate frequency of qubit is",(resf[q]+resf[q+1])/2, "GHz, anharmonicity is ", anh, "MHz, the resonate frequency of cavity is",(resf[c]+resf[c+1])/2, "GHz, and kapa is ", kapa, "MHz"
    return res

def justInCase():
    changeTwoSweep(next[0]-0.15, next[0]+0.15,10, next[1]-0.15, next[1]+0.15,1)
    AnalyzeAll()
    export("E:/Simulation/Qubit_0606/case.csv")
    with open ('case.csv','rb') as csvres:
        result = csv.reader(csvres)
        res = list(result)
        del res[0]
    
    resf = []
    resv = []
    
    for i in res:
        resf = resf + [float(i[0])]
        resv = resv + [float(i[1])]
    
    test = []
    for i in range(len(resv)-1):
        if resv[i] < 0:
            if resv[i+1] > 0:
                test.append(i)
                if len(test) > 2:
                    break
    return test
	
def calAlp(k):
    with open ('result{}.csv'.format(k),'rb') as csvres:
        result = csv.reader(csvres)
        res = list(result)
        del res[0]
    
    resf = []
    resv = []

    for i in res:
        resf = resf + [float(i[0])]
        resv = resv + [float(i[1])]

    test = []
    for i in range(len(resv)-1):
        if resv[i] < 0:
            if resv[i+1] > 0:
                test.append(i)
                if len(test) > 1:
                    break

    q = test[0]

    quyp = (resv[q+1]-resv[q])/(2.0*math.pi*10.0**9*(resf[q+1]-resf[q]))
    
    e = 1.6021766208 * 10**(-19)
    cj = 0.5 * quyp
    ec = e*e / (2*cj)
    anh = - ec / (2 * math.pi * 1.05 * 10**(-34)) * 10**(-6)
    res = anh
    print  "resonate frequency of qubit is",(resf[q]+resf[q+1])/2, "GHz, anharmonicity is ", anh, "MHz"
    return res    

def determineNextSweep(k):
	with open ('temp{}.csv'.format(k),'rb') as csvtemp:
		temp = csv.reader(csvtemp)
		te = list(temp)
		del te[0]
	
	tef = []
	tev = []
	
	for i in te:
		tef = tef + [float(i[0])]
		tev = tev + [float(i[1])]
		
	test = []
    
	for i in range(len(tev)-2):
         if tev[i] < 0:
             if tev[i+1] > 0:
                 test.append(i)
         if tev[i]-tev[i+1] > 0:
             if tev[i+1] - tev[i+2] < 0:
                 test.append(i)
                 test[1] = i
	q = test[0]
	c = test[1]
	sweep = [(tef[q]+tef[q+1])/2,tef[c+1]]
	return sweep
	
def openProject(projectPath, projectName):
     global oDesktop, oAnsoftApp,oProject,oDesign, oEditor
     [oAnsoftApp, oDesktop] = hfss.setup_interface()     
     oDesktop.OpenProject(projectPath)
     oProject = oDesktop.SetActiveProject(projectName)
     oDesign = oProject.SetActiveDesign("HFSSDesign1")
     oEditor = oDesign.SetActiveEditor("3D Modeler")
     
def changeParameter(name,value):
    global oDesign
    oDesign.ChangeProperty(
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
    					"NAME:"+name,
    					"Value:="		, value
    				]
    			]
    		]
    	])    

def changeOneSweep(start,over,step):
	global oDesign, oModule
	oModule = oDesign.GetModule("AnalysisSetup")
	oModule.EditFrequencySweep("Whole_Setup", "Sweep", 
		[
			"NAME:Sweep",
			"IsEnabled:="		, True,
			"RangeType:="		, "LinearStep",
			"RangeStart:="		, str(start)+"GHz",
			"RangeEnd:="		, str(over)+"GHz",
			"RangeStep:="		, str(step)+"MHz",
			"Type:="		, "Discrete",
			"SaveFields:="		, False,
			"SaveRadFields:="	, False,
			"ExtrapToDC:="		, False
		])

def changeTwoSweep(astart,aover,astep,bstart,bover,bstep):
	global oDesign, oModule
	oModule = oDesign.GetModule("AnalysisSetup")
	oModule.EditFrequencySweep("Whole_Setup", "Sweep", 
		[
			"NAME:Sweep",
			"IsEnabled:="		, True,
			"RangeType:="		, "LinearStep",
			"RangeStart:="		, str(astart)+"GHz",
			"RangeEnd:="		, str(aover)+"GHz",
			"RangeStep:="		, str(astep)+"MHz",
			[
				"NAME:SweepRanges",
				[
					"NAME:Subrange",
					"RangeType:="		, "LinearStep",
					"RangeStart:="		, str(bstart)+"GHz",
					"RangeEnd:="		, str(bover)+"GHz",
					"RangeStep:="		, str(bstep)+"MHz"
				]
			],
			"Type:="		, "Discrete",
			"SaveFields:="		, False,
			"SaveRadFields:="	, False,
			"ExtrapToDC:="		, False
		])	
		
def AnalyzeAll():
    global oDesign
    oDesign.AnalyzeAll()

def deleteAllVariable():
    global oDesign
    oDesign.DeleteFullVariation("All", False)

def deleteAllReport():
    global oDesign    
    oModule = oDesign.GetModule("ReportSetup")
    oModule.DeleteAllReports()

def exportTable(filename):
    global oDesign, oModule
    oModule = oDesign.GetModule("ReportSetup")
    oModule.ExportToFile("Data Table 1", filename)    
    
def export(filename):
    global oDesign, oModule
    oModule = oDesign.GetModule("ReportSetup")
    oModule.ExportToFile("XY Plot 1", filename)    
  
def savefile():
	global oProject
	oProject.Save()
	
def quitProgram():
    global oDesign, oProject, oDesktop, oAnsoftApp, oModule
    hfss.quit_application(oDesktop)            
    del oDesign
    del oProject 
    del oDesktop
    del oAnsoftApp
    del oModule      
    
# Other ThingS
    
def showMeDensityPlot(xmin,xmax,xstep,ymin,ymax,ystep,zarray):
    countx = int(math.floor((xmax - xmin)/xstep + 1))
    county = int(math.floor((ymax - ymin)/ystep + 1))
    z = np.transpose(np.reshape(zarray,(countx,county)))
    y, x = np.mgrid[slice(ymin, ymax + ystep, ystep),
                slice(xmin, xmax + xstep, xstep)]
#    z_min, z_max = z.max(), z.max()
    plt.pcolormesh(x, y, z)#, cmap='YlOrRd', vmin=z_min, vmax=z_max)
    plt.axis([x.min(), x.max(), y.min(), y.max()])
    plt.colorbar()

def writeFile(file,name,value):
    temp = h5py.File(file)
    temp.create_dataset(name,data=value)
    temp.close()

def readFile(file,name):
    res = h5py.File(file,"r")
    va = res[name].value
    res.close()
    return va    


if __name__=='__main__':
    calAlpAndXi(1)
                
    
    
    