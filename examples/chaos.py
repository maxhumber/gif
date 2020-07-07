import gif
from matplotlib import pyplot as plt
from random import randint


@gif.frame
def plot(x, y):
    plt.figure(figsize=(5, 3), dpi=100)
    plt.scatter(x, y)
    plt.xlim((0, 100))
    plt.ylim((0, 100))


frames = []
for _ in range(50):
    x = [randint(0, 100) for _ in range(10)]
    y = [randint(0, 100) for _ in range(10)]
    frame = plot(x, y)
    frames.append(frame)

gif.save(frames, "examples/chaos.gif")
