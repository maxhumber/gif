import matplotlib.pyplot as plt
import numpy as np

import gif

COLOR = "#d66582"
SIZE = 3


def random_scatter(x, y, beta=0.15, seed=None):
    np.random.seed(seed)
    ratio_x = -beta * np.log(np.random.rand(x.shape[0]))
    ratio_y = -beta * np.log(np.random.rand(y.shape[0]))
    dx = ratio_x * x
    dy = ratio_y * y
    return x - dx, y - dy


def plot_random_scatter(ax, x, y, beta, c=COLOR, s=SIZE, alpha=None, seed=None):
    x, y = random_scatter(x, y, beta=beta, seed=seed)
    ax.scatter(x, y, s=3, c=c, alpha=alpha)


@gif.frame
def plot_heart(x, y, i):
    fig = plt.figure(figsize=(5, 3), dpi=100, facecolor="white")
    ax = plt.gca()
    ax.set_facecolor("white")
    x = x * np.sin(i)
    y = y * np.sin(i)
    ax.scatter(x, y, s=SIZE, c=COLOR)
    plot_random_scatter(ax, x, y, 0.15, seed=1)
    plot_random_scatter(ax, x, y, 0.15, seed=2)
    plot_random_scatter(ax, x, y, 0.15, seed=3)
    xi = x[: x.shape[0] : 2] * np.sin(i) * 0.7
    yi = y[: y.shape[0] : 2] * np.sin(i) * 0.7
    plot_random_scatter(ax, xi, yi, 0.25, seed=4)
    xo = x[: x.shape[0] : 2] * np.sin(i) * 1.2
    yo = y[: y.shape[0] : 2] * np.sin(i) * 1.2
    plot_random_scatter(ax, xo, yo, 0.1, alpha=0.8, seed=6)

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(bottom=False, labelbottom=False, left=False, labelleft=False)
    plt.xlim((-6 * np.pi, 6 * np.pi))
    plt.ylim((-6 * np.pi, 6 * np.pi))
    plt.tight_layout(pad=0)


frames = []
for i in np.linspace(np.pi / 3, 2 * np.pi / 3, 20):
    t = np.linspace(0, 2 * np.pi, 2000)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    frame = plot_heart(x, y, i)
    frames.append(frame)

gif.save(frames, "images/heart.gif", duration=100)
