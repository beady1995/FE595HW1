#!/usr/bin/env python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,2*np.pi,0.2)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 2pi')
plt.ylabel('sin(x) values and cos(x) values')
plt.title('Plot of sin(x) and cos(x) from 0 to 2pi')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()