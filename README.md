<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/gif/master/logo/gif.png" width="300px" alt="gif">
</h3>
<p align="center">
  <a href="https://github.com/maxhumber/gif"><img alt="GitHub" src="https://img.shields.io/github/license/maxhumber/gif"></a>
  <a href="https://travis-ci.org/maxhumber/gif"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/gif.svg"></a>
  <a href="https://pypi.python.org/pypi/gif"><img alt="PyPI" src="https://img.shields.io/pypi/v/gif.svg"></a>
  <a href="https://pepy.tech/project/gif"><img alt="Downloads" src="https://pepy.tech/badge/gif"></a>
</p>
#### About

The extension for animated [matplotlib](https://matplotlib.org/) and [Altair](https://altair-viz.github.io/) animations.



#### matplotlib

Install:

```
pip install gif
```

Import:

```
import gif
from matplotlib import pyplot as plt
```

Decorate a plot function with `gif.frame`:

```python
@gif.frame
def plot(x, y):
    plt.figure(figsize=(5, 3), dpi=100)
    plt.scatter(x, y)
    plt.xlim((0, 100))
    plt.ylim((0, 100))
```

Build a bunch of "frames" with a standard for loop:

```python
from random import randint

frames = []
for _ in range(50):
    x = [randint(0, 100) for _ in range(10)]
    y = [randint(0, 100) for _ in range(10)]
    frame = plot(x, y)
    frames.append(frame)
```

Select the duration (milliseconds) between each frame and save:

```
gif.save(frames, "examples/chaos.gif", duration=100)
```





#### Gallery

matplotlib:

| ![chaos.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/chaos.gif) | ![attachment.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/attachment.gif) | ![wave.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/wave.gif) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![hop.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/hop.gif) | ![tornado.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/tornado.gif) |                                                              |



Altair:

| ![chaos.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/chaos.gif) | ![attachment.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/attachment.gif) | ![wave.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/wave.gif) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![hop.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/hop.gif) | ![tornado.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/tornado.gif) |                                                              |



```
pip install gif[altair]
```


