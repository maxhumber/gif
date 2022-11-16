import matplotlib.pyplot as plt
import numpy as np

import gif

N = 50
red = np.random.normal(loc=45, scale=3, size=N)
blue = np.random.normal(loc=48, scale=5, size=N)


@gif.frame
def plot_hop(i, margin=0.1):
    plt.figure(figsize=(5, 3), dpi=100)
    plt.hlines(y=red[i], xmin=0, xmax=1 - margin, colors="r", lw=2)
    plt.hlines(y=blue[i], xmin=1 + margin, xmax=2, colors="b", lw=2)
    plt.xlim(0 - margin * 2, 2 + margin * 2)
    plt.ylim(0, 100)
    plt.xticks([0.5, 1.5], ["Red Team", "Blue Team"])
    plt.yticks([0, 25, 50, 75, 100], ["0", "25", "50", "75", "100%"])


frames = []
for i in range(N):
    frame = plot_hop(i)
    frames.append(frame)

gif.save(frames, "images/hop.gif", duration=200)
