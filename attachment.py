# power laws

'''
Distributions of cities
Species extinction
number of links in the www
firm sizes
Youtube views
books sold
academic citiations
floods
earthquakes
terrorist attacks


In contrast to:

height (at 5.9 > someone would be over 1 empire state tall)
10,0000 people taller than girraffes
and 180 million people less than 7 inches tall

When someone buys a Harry Potter book, she induces others to buy it

When a city increases in pop. it adds amenenities and job opportunities


The Matthew effect: "for mike" more begets more


Probabilty of an event is proportional to it's size raised to a negative exoponent

1/x describes a power law

In a power law: the probability of an event is inversely related to its size

the larger the event, the less likely it is to occur

THE EQUATION:

p(x) = C * x**(-a)

a has to be > 1, and determines the tail


Zipfs Law
when a = 2
the rank of an event times it's size equals a constant

Preferential attachment:
entities grow at rates relative to their proportions

A new arrival either joins an existing entity or creates a new one
If the latter, the probability of joining an existing entity is proporational to it's size

With probability p (small)
the arrival forms a new entity
with probability (1-p) the arrival joinns a new entity

In each setting an action (buying a book) increases the likelihood others will do the same

The implications of long tails:

long tails mean a few big winners and many losers as compared to a normal distribution


A person who writes a better book, a catchier song, should garner more sales

As our world becomes more interconnected, and feedbacks increase, we should see more long tails

The music lab study

'''

####

from collections import Counter
import io
import random
import time

from matplotlib import pyplot as plt
from PIL import Image

random.seed(2020)

def simulate_arrival(count, p=0.1):
    if random.uniform(0, 1) <= p:
        group = len(count)
    else:
        k = list(count.keys())
        v = list(count.values())
        group = random.choices(k, weights=v)[0]
    return group

def plot_arrival(count, count_last,
        xlim=[0, 10], ylim=[0, 100], figsize=(10, 5)):
    plt.figure(figsize=figsize)
    plt.bar(count.keys(), count.values())
    plt.bar(count_last.keys(), count_last.values())
    plt.xlim([xlim[0]-1, xlim[1]+1])
    plt.xticks(range(xlim[0], xlim[1]+1))
    plt.ylim(ylim)

images = []
count = Counter({0})
count_last = count.copy()
for _ in range(100):
    group = simulate_arrival(count, p=0.10)
    count.update({group})
    buf = io.BytesIO()
    plt.title(f'Newest arrival joined group: {group}')
    plot_arrival(count, count_last)
    plt.savefig(buf, format='png')
    im = Image.open(buf)
    images.append(im)
    count_last = count.copy()

images[0].save(
    'attachment.gif',
    save_all=True,
    append_images=images[1:],
    optimize=True,
    duration=100,
    loop=0
)
