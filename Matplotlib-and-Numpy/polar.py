"""
David Li
January 07 2016
polar.py
Plot polar function 2sin(theta)*cos(theta)
"""

import numpy as np
import matplotlib.pyplot as plt

# set up equation
theta = np.linspace(-2*np.pi, 2*np.pi, 360) 
r = 2*np.sin(2*theta) *np.cos(2*theta)

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, color='r', linewidth=1.5)
ax.set_rmax(1)  # limit size of graph to radius 1
ax.grid(True)

ax.set_title("$r=2*cos(\\theta)*sin(\\theta)$") #display math equation using tex
plt.show()  #show plot