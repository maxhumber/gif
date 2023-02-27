import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import gif

N = 100


@gif.frame
def plot_spiral(i):
    fig = plt.figure(figsize=(5, 3), dpi=100)
    ax = fig.add_subplot(projection="3d")
    a, b = 0.5, 0.2
    th = np.linspace(475, 500, N)
    x = a * np.exp(b * th) * np.cos(th)
    y = a * np.exp(b * th) * np.sin(th)
    z = np.linspace(0, 2, len(th))
    ax.plot(x[:i], y[:i], z[:i], lw=4, color="purple")
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))
    ax.set_zlim(min(z), max(z))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])


frames = []
for i in range(N):
    frame = plot_spiral(i)
    frames.append(frame)

gif.save(frames, "images/spiral.gif", duration=50)
