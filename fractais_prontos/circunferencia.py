import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
plt.axis('equal')
ln, = plt.plot([],[], 'ko')
r = 4.0

def init():
    ax.set_xlim(-r-2, r+2)
    ax.set_ylim(-r-2, r+2)
    return ln,

def update(frame):
    xdata.append(r*np.cos(frame))
    ydata.append(r*np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,


ani = FuncAnimation(fig, update, frames=np.linspace(0.01, 2*np.pi, 100),
                    init_func=init)

plt.show()
