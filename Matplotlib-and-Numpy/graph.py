import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1) 
r = 2*np.sin(2*theta) *np.cos(2*theta)

ax.plot(theta, r, color='r', linewidth=1.5)
ax.set_rmax(1)
ax.grid(True)

ax.set_title("Polar Graph")
plt.show()
