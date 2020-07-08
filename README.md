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





#### matplotlib

| [![attachment.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/attachment/attachment.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/attachment) | [![hop.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/hop/hop.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/hop) | [![phone.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/phone/phone.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/phone) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [![seinfeld.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/seinfeld/seinfeld.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/seinfeld) | [![attachment.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/tornado/tornado.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/tornado) |                                                              |



#### Altair 

| [![covid.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/covid/covid.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/covid) | [![emoji.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/emoji/emoji.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/emoji) | [![pyramid.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/pyramid/pyramid.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/pyramid) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [![textbooks.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/textbooks/textbooks.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/textbooks) | [![wave.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/wave/wave.gif)]( https://github.com/maxhumber/gif/tree/master/gallery/altair/wave) |                                                              |



```
pip install gif[altair]
```


