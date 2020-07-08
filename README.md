<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/gif/master/logo/gif.png" width="300px" alt="gif">
</h3>
<p align="center">
  <a href="https://github.com/maxhumber/gif"><img alt="GitHub" src="https://img.shields.io/github/license/maxhumber/gif"></a>
  <a href="https://travis-ci.org/maxhumber/gif"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/gif.svg"></a>
  <a href="https://pypi.python.org/pypi/gif"><img alt="PyPI" src="https://img.shields.io/pypi/v/gif.svg"></a>
  <a href="https://pepy.tech/project/gif"><img alt="Downloads" src="https://pepy.tech/badge/gif"></a>
</p>


### About

The extension for [matplotlib](https://matplotlib.org/) and [Altair](https://altair-viz.github.io/) animations.



### Installation

gif is installed at the command line:

```sh
pip install gif
```

Altair gifs require [additional dependencies](https://pypi.org/project/altair-saver/). These can be installed accordingly:

```
pip install gif[altair]
```

**Note**: altair-saver uses [Selenium](https://selenium.dev/selenium/docs/api/py/), which requires a properly configured installation of either [chromedriver](https://chromedriver.chromium.org/) or [geckodriver](https://firefox-source-docs.mozilla.org/testing/geckodriver/).



### Usage (matplotlib)

Imports and data:

```python
import random
from matplotlib import pyplot as plt
import gif

x = [random.randint(0, 100) for _ in range(100)]
y = [random.randint(0, 100) for _ in range(100)]
```

Decorate a plot function with `gif.frame` (and don't return anything):

```python
@gif.frame
def plot(i):
    xi = x[i*10:(i+1)*10]
    yi = y[i*10:(i+1)*10]
    plt.scatter(xi, yi)
    plt.xlim((0, 100))
    plt.ylim((0, 100))
```

Build a bunch of "frames" with a standard `for` loop:

```python
frames = []
for i in range(10):
    frame = plot(i)
    frames.append(frame)
```

Specify the duration (in milliseconds) between each frame, and save:

```python
gif.save(frames, 'example.gif', duration=100)
```



### Usage (Altair)

Imports and data:

```python
import random
import altair as alt
import pandas as pd
import gif

df = pd.DataFrame({
    't': list(range(10)) * 10,
    'x': [random.randint(0, 100) for _ in range(100)],
    'y': [random.randint(0, 100) for _ in range(100)]
})
```

Decorate a plot function with `gif.frame` and **return an Altair object**:

```python
@gif.frame
def plot(i):
    d = df[df['t'] == i]
    chart = alt.Chart(d).encode(
        x=alt.X('x', scale=alt.Scale(domain=(0, 100))),
        y=alt.Y('y', scale=alt.Scale(domain=(0, 100)))
    ).mark_circle()
    return chart
```

Build a bunch of "frames" with a standard `for` loop:

```python
frames = []
for i in range(10):
    frame = plot(i)
    frames.append(frame)
```

Specify the duration (in milliseconds) between each frame, and save:

```python
gif.save(frames, 'example.gif', duration=100)
```



### Gallery (matplotlib)

<I>Click on any image to see the source code</I>

| [![attachment.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/attachment/attachment.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/attachment) | [![hop.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/hop/hop.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/hop) | [![phone.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/phone/phone.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/phone) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [![seinfeld.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/seinfeld/seinfeld.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/seinfeld) | [![attachment.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/tornado/tornado.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/tornado) |                                                              |



### Gallery (Altair)

<I>Click on any image to see the source code</I>

| [![covid.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/covid/covid.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/covid) | [![emoji.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/emoji/emoji.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/emoji) | [![pyramid.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/pyramid/pyramid.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/pyramid) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [![textbooks.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/textbooks/textbooks.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/textbooks) | [![wave.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/wave/wave.gif)]( https://github.com/maxhumber/gif/tree/master/gallery/altair/wave) |                                                              |




If you have a kick ass animation that you think should be in the Gallery, submit a PR!
