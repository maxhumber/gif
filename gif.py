from functools import wraps
from io import BytesIO as Buffer
from matplotlib import pyplot as plt
from PIL import Image


class Options:
    """Matplotlib image and export options

    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html

    Example:
    ```python
    gif.options.matplotlib["dpi"] = 300
    ```
    """

    def __init__(self):
        self.matplotlib = {}

    def reset(self):
        self.matplotlib = {}


options = Options()


def frame(func):
    """Plot function decorator

    Example:
    ```python
    @gif.frame
    def plot(i):
        plt.scatter(x[:i], y[:i])
        plt.xlim((0, 100))
        plt.ylim((0, 100))
    ```
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        buffer = Buffer()
        func(*args, **kwargs)
        plt.savefig(buffer, format="png", **options.matplotlib)
        plt.close()
        buffer.seek(0)
        img = Image.open(buffer)
        return img

    return wrapper


def save(frames, path, duration=100):
    """Save a collection of frames to a gif

    Arguments:
    - frames (list): Collection of frames built with the @gif.frame decorator
    - path (str): Filename with relative/absolute path (must end with .gif)
    - duration (float): Milliseconds between frames

    Example:
    ```python
    frames = []
    for i in range(10):
        frame = plot(i)
        frames.append(frame)

    gif.save(frames, "test.gif", duration=50)
    ```
    """
    if not path.endswith(".gif"):
        raise ValueError("Path/filename must end with .gif")
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=duration,
        loop=0,
    )
