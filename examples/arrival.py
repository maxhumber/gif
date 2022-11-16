import random
from collections import Counter

from matplotlib import pyplot as plt
from PIL import Image

import gif

random.seed(2020)


@gif.frame
def plot_arrival(count, count_last):
    plt.figure(figsize=(5, 3), dpi=100)
    plt.bar(count.keys(), count.values())
    plt.bar(count_last.keys(), count_last.values())
    plt.xlim(-1, 11)
    plt.xticks(range(0, 10 + 1))
    plt.ylim(0, 100)


def simulate_arrival(count, p=0.10):
    if random.uniform(0, 1) <= p:
        group = len(count)
    else:
        k = list(count.keys())
        v = list(count.values())
        group = random.choices(k, weights=v)[0]
    return group


count = Counter({0})
count_last = count.copy()
frames = []
for _ in range(100):
    group = simulate_arrival(count)
    count.update({group})
    frame = plot_arrival(count, count_last)
    frames.append(frame)
    count_last = count.copy()

gif.save(frames, "images/arrival.gif")
