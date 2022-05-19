<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/gif/master/logo/gif.png" width="250px" alt="gif">
</h3>
<p align="center">
  <a href="https://github.com/maxhumber/gif"><img alt="GitHub" src="https://img.shields.io/github/license/maxhumber/gif"></a>
  <a href="https://pypi.python.org/pypi/gif"><img alt="PyPI" src="https://img.shields.io/pypi/v/gif.svg"></a>
  <a href="https://pepy.tech/project/gif"><img alt="Downloads" src="https://pepy.tech/badge/gif/month"></a>
</p>


### About

The [matplotlib](https://matplotlib.org/) Animation Extension


### Quickstart

<u>Install</u>

```sh
pip install gif
```

<u>Usage</u>

```python
import random
from matplotlib import pyplot as plt
import gif

x = [random.randint(0, 100) for _ in range(100)]
y = [random.randint(0, 100) for _ in range(100)]

# (Optional) Set the dots per inch resolution to 300:
gif.options["dpi"] = 300

# Decorate a plot function with @gif.frame (return not required):
@gif.frame
def plot(i):
    xi = x[i*10:(i+1)*10]
    yi = y[i*10:(i+1)*10]
    plt.scatter(xi, yi)
    plt.xlim((0, 100))
    plt.ylim((0, 100))

# Build a bunch of "frames"
frames = []
for i in range(10):
    frame = plot(i)
    frames.append(frame)

# Specify the duration between frames (milliseconds) and save to file:
gif.save(frames, 'example.gif', duration=50)
```

### Examples

| [![attachment.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/attachment/attachment.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/attachment) | [![hop.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/hop/hop.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/hop) | [![phone.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/phone/phone.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/phone) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [![seinfeld.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/seinfeld/seinfeld.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/seinfeld) | [![spiral.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/spiral/spiral.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/spiral) | [![love.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/love/love.gif)](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/love) |
