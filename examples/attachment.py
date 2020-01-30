from collections import Counter
import io
import functools
import random
import time

import gif
from matplotlib import pyplot as plt
from PIL import Image

@gif.frame
def plot_arrival(count, count_last, xlim=(0, 10), ylim=(0, 100), figsize=(10, 5)):
    plt.figure(figsize=figsize)
    plt.bar(count.keys(), count.values())
    plt.bar(count_last.keys(), count_last.values())
    plt.xlim([xlim[0] - 1, xlim[1] + 1])
    plt.xticks(range(xlim[0], xlim[1] + 1))
    plt.ylim(ylim)

def simulate_arrival(count, p=0.1):
    if random.uniform(0, 1) <= p:
        group = len(count)
    else:
        k = list(count.keys())
        v = list(count.values())
        group = random.choices(k, weights=v)[0]
    return group

random.seed(2020)
count = Counter({0})
count_last = count.copy()
frames = []
for _ in range(100):
    group = simulate_arrival(count, p=0.10)
    count.update({group})
    frame = plot_arrival(count, count_last)
    frames.append(frame)
    count_last = count.copy()

gif.save(frames, "examples/attachment.gif")
