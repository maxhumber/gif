import gif
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(2016)

n = 50
red = np.random.normal(loc=45, scale=3, size=n)
blue = np.random.normal(loc=48, scale=5, size=n)

@gif.frame
def plot_hop(i, margin=0.1):
    plt.figure(figsize=(5, 3), dpi=100)
    plt.hlines(y=red[i], xmin=0, xmax=1-margin, colors='r', lw=2)
    plt.hlines(y=blue[i], xmin=1+margin, xmax=2, colors='b', lw=2)
    plt.xlim(0-margin*2, 2+margin*2)
    plt.ylim(0, 100)
    plt.xticks([0.5, 1.5], ['Red Team', 'Blue Team'])
    plt.yticks([0, 25, 50, 75, 100], ['0', '25', '50', '75', '100%'])

frames = []
for i in range(n):
    frame = plot_hop(i)
    frames.append(frame)

gif.save(frames, 'examples/hop.gif', duration=200)
