import random
from matplotlib import pyplot as plt

import gif

@gif.frame
def plot(x, y):
    plt.figure(figsize=(5, 5))
    plt.scatter(x, y)
    plt.xlim((0, 100))
    plt.ylim((0, 100))

frames = []
for _ in range(50):
    n = 10
    x = [random.randint(0, 100) for _ in range(10)]
    y = [random.randint(0, 100) for _ in range(10)]
    frame = plot(x, y)
    frames.append(frame)

gif.save(frames, 'test4.gif')
