# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:32:38 2018

@author: zctid
"""

from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import threading
import time
import numpy as np
import matplotlib.animation as animation

#list_of_datetimes=map(datetime.fromtimestamp,[10.2,300,600])
#
#
#fig, ax = plt.subplots(1,num='a')
#fig.autofmt_xdate()
#plt.plot(list_of_datetimes, [1,2,3])
#xfmt = mdates.DateFormatter('%d-%m %H:%M')
#ax.xaxis.set_major_formatter(xfmt)
#plt.title("a")
###
#plt.figure("aa")
#plt.plot(list_of_datetimes, [1,2,3])
###
#plt.figure('a')
#list_of_datetimes=map(datetime.fromtimestamp,[600,800,900])
#plt.plot(list_of_datetimes, [3,2,1])





fig = plt.figure(1)
plt.plot([1,2],[3,4],'*')


fig = plt.figure(1)
ax1 = fig.add_subplot(1,1,1)
xar = []
yar = []

def animate(i):
    x,y = np.random.rand(), np.random.rand()
    xar.append(x)
    yar.append(y)
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()







