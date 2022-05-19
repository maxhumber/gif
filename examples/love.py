import gif

from matplotlib import pyplot as plt
import numpy as np


# formula: https://www.wolframalpha.com/share/clip?f=d41d8cd98f00b204e9800998ecf8427edn0q2vrnts
t = np.linspace(0, 6, 100)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)


@gif.frame
def plot_love(x, y):
    plt.figure(figsize=(5, 3), dpi=100)
    plt.scatter(x, y, 60, c="r", alpha=0.7, marker=r"$\heartsuit$")
    plt.axis("off")


frames = []
for i in range(1, len(x)):
    of = plot_love(x[:i], y[:i])
    frames.append(of)

gif.save(frames, "images/matplotlib-love.gif", duration=80)
