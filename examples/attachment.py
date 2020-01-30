from collections import Counter
import random
import time

from matplotlib import pyplot as plt

import gif

random.seed(2020)

@gif.frame
def plot(count, xlim=(0, 10), ylim=(0, 100), figsize=(10, 5)):
    plt.figure(figsize=figsize)
    plt.bar(count.keys(), count.values())
    plt.xlim([xlim[0]-1, xlim[1]+1])
    plt.xticks(range(xlim[0], xlim[1]+1))
    plt.ylim(ylim)

def simulate(count, p=0.1):
    if random.uniform(0, 1) <= p:
        group = len(count)
    else:
        k = list(count.keys())
        v = list(count.values())
        group = random.choices(k, weights=v)[0]
    return group

frames = []
count = Counter({0})
for _ in range(100):
    group = simulate(count, p=0.10)
    count.update({group})
    frame = plot(count)
    frames.append(frame)

gif.save(frames, 'test3.gif')
