# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:04:36 2020

@author: Pengfei Liu
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.2)
y = np.sin(x)
z = np.cos(x)
t=np.tan(x)
plt.grid()
# This operation inserts a NaN where the difference between successive points is negative
# NaN means "Not a Number" and NaNs are not plotted or connected
# I found this by doing a search for "How to plot tan(x) in matplotlib without the connecting lines between asymtotes"
t[:-1][np.diff(t) < 0] = np.nan
plt.plot(x,y,x,z)
xmin, xmax, ymin, ymax =plt. axis()
axes = plt.axes()
axes.set_xlim([xmin, xmax])
axes.set_ylim([ymin, ymax])
plt.plot(x,t,label="tanh")
plt.xlabel('x values from 0 to 2pi')
plt.ylabel('sin(x) values and cos(x) values')
plt.title('Plot of sin(x) and cos(x) from 0 to 2pi')
plt.legend(['sin(x)', 'cos(x)','tanh'])
plt.show()