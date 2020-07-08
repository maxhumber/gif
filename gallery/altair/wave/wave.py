import gif
import numpy as np
import matplotlib.pyplot as plt


@gif.frame
def plot(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    plt.figure(figsize=(5, 3), dpi=100)
    plt.plot(x, y, color="red")


frames = []
for i in range(100):
    frame = plot(i)
    frames.append(frame)

gif.save(frames, "gallery/matplotlib/wave/wave.gif", duration=20)
