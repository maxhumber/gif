from collections import Counter
import io
import functools
import random
import time

from matplotlib import pyplot as plt
from PIL import Image

random.seed(2020)

def buffer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        buf = io.BytesIO()
        func(*args, **kwargs)
        plt.savefig(buf, format='png')
        # buf.seek(0)
        image = Image.open(buf)
        return image
    return wrapper

@buffer
def plot_arrival(count, count_last,
        xlim=(0, 10), ylim=(0, 100), figsize=(10, 5)):
    plt.figure(figsize=figsize)
    plt.bar(count.keys(), count.values())
    plt.bar(count_last.keys(), count_last.values())
    plt.xlim([xlim[0]-1, xlim[1]+1])
    plt.xticks(range(xlim[0], xlim[1]+1))
    plt.ylim(ylim)

def save_gif(images, filename):
    images[0].save(
        filename,
        save_all=True,
        append_images=images[1:],
        optimize=True,
        duration=100,
        loop=0
    )

def simulate_arrival(count, p=0.1):
    if random.uniform(0, 1) <= p:
        group = len(count)
    else:
        k = list(count.keys())
        v = list(count.values())
        group = random.choices(k, weights=v)[0]
    return group

images = []
count = Counter({0})
count_last = count.copy()
for _ in range(100):
    group = simulate_arrival(count, p=0.10)
    count.update({group})
    image = plot_arrival(count, count_last)
    images.append(image)
    count_last = count.copy()

save_gif(images, 'test.gif')
