import functools
import io

from matplotlib import pyplot as plt
from PIL import Image

def frame(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        buffer = io.BytesIO()
        func(*args, **kwargs)
        plt.savefig(buffer, format='png')
        buffer.seek(0) # https://stackoverflow.com/q/8598673/3731467
        image = Image.open(buffer)
        plt.close() # to clear the interactive plot
        return image
    return wrapper

def save(frames, filename, duration=100, loop=0):
    frames[0].save(
        filename,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=duration, # ms?
        loop=loop # what are the options here?
    )
