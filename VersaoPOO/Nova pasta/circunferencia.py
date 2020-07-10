import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def init():
    ax.set_xlim(-raio - 2, raio + 2)
    ax.set_ylim(-raio - 2, raio + 2)
    return ln


def update(frame):
    xdata.append(raio * np.cos(frame))
    ydata.append(raio * np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln


fig, ax = plt.subplots()
xdata, ydata = [], []
plt.axis('equal')
ln, = plt.plot([], [], 'ko')
raio = 4.0
ani = FuncAnimation(fig, update, frames=np.linspace(0.01, 2 * np.pi, 100), init_func=init)
plt.show()