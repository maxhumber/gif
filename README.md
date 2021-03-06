<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/gif/master/logo/gif.png" width="300px" alt="gif">
</h3>
<p align="center">
  <a href="https://github.com/maxhumber/gif"><img alt="GitHub" src="https://img.shields.io/github/license/maxhumber/gif"></a>
  <a href="https://travis-ci.org/maxhumber/gif"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/gif.svg"></a>
  <a href="https://pypi.python.org/pypi/gif"><img alt="PyPI" src="https://img.shields.io/pypi/v/gif.svg"></a>
  <a href="https://pepy.tech/project/gif"><img alt="Downloads" src="https://pepy.tech/badge/gif/month"></a>
</p>



### About

The extension for [Altair](https://altair-viz.github.io/), [matplotlib](https://matplotlib.org/), and [Plotly](https://plotly.com/python/) animations.



### Installation

gif is installed at the command line:

```sh
pip install -U gif
```

Depending on which flavour of gif you plan to use you'll likely need some additional dependencies:

```sh
pip install "gif[altair]"     
pip install "gif[matplotlib]"
pip install "gif[plotly]"
```

**Note**: gif[altair] uses [Selenium](https://selenium.dev/selenium/docs/api/py/), which requires a properly configured [chromedriver](https://chromedriver.chromium.org/) or [geckodriver](https://firefox-source-docs.mozilla.org/testing/geckodriver/).



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

Specify the duration between each frame and save:

```python
gif.save(frames, 'example.gif', duration=100, unit="ms", between="frames")
```



### Usage (matplotlib)

Imports and data:

```python
import random
from matplotlib import pyplot as plt
import gif

x = [random.randint(0, 100) for _ in range(100)]
y = [random.randint(0, 100) for _ in range(100)]
```

(Optional) Set the dots per inch resolution to 300:

```python
gif.options.matplotlib["dpi"] = 300
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

Specify the duration of the entire gif:

```python
gif.save(frames, 'example.gif', duration=3.5, unit="s", between="startend")
```



### Usage (Plotly)

Imports and data:

```python
import random
import plotly.graph_objects as go
import pandas as pd
import gif

df = pd.DataFrame({
    't': list(range(10)) * 10,
    'x': [random.randint(0, 100) for _ in range(100)],
    'y': [random.randint(0, 100) for _ in range(100)]
})
```

Decorate a plot function with `gif.frame` and **return a Plotly figure**:

```python
@gif.frame
def plot(i):
    d = df[df['t'] == i]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=d["x"],
        y=d["y"],
        mode="markers"
    ))
    fig.update_layout(width=500, height=300)
    return fig
```

Build a bunch of "frames" with a standard `for` loop:

```python
frames = []
for i in range(10):
    frame = plot(i)
    frames.append(frame)
```

Specify the duration (milliseconds) between each frame and save:

```python
gif.save(frames, 'example.gif', duration=100)
```



### Gallery (Altair)

<I>Click on any image to see the source code</I>

| [![covid.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/covid/covid.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/covid) | [![emoji.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/emoji/emoji.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/emoji) | [![pyramid.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/pyramid/pyramid.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/pyramid) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [![textbooks.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/textbooks/textbooks.gif)](https://github.com/maxhumber/gif/tree/master/gallery/altair/textbooks) | [![wave.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/altair/wave/wave.gif)]( https://github.com/maxhumber/gif/tree/master/gallery/altair/wave) |                                                              |



### Gallery (matplotlib)

<I>Click on any image to see the source code</I>

| [![attachment.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/attachment/attachment.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/attachment) | [![hop.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/hop/hop.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/hop) | [![phone.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/phone/phone.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/phone) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [![seinfeld.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/seinfeld/seinfeld.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/seinfeld) | [![attachment.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/tornado/tornado.gif)](https://github.com/maxhumber/gif/tree/master/gallery/matplotlib/tornado) | [![love.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/love/love.gif)](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/matplotlib/love) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [![subplots.gif](https://github.com/sivakar94/gif-1/blob/master/gallery/matplotlib/subplots/subplots.gif)](https://github.com/sivakar94/gif-1/blob/master/gallery/matplotlib/subplots) 

| [![compare_2_features.gif](https://github.com/sivakar94/gif-1/blob/master/gallery/matplotlib/compare_features/compare_2_features.gif)](https://github.com/sivakar94/gif-1/blob/master/gallery/matplotlib/compare_features) 

| [![train_test_split.gif](https://github.com/sivakar94/gif-1/blob/master/gallery/matplotlib/train_test_split/train_test_split.gif)](https://github.com/sivakar94/gif-1/blob/master/gallery/matplotlib/train_test_split/train_test_split) |




### Gallery (Plotly)

<I>Click on any image to see the source code</I>

| [![bubble.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/plotly/bubble/bubble.gif)](https://github.com/maxhumber/gif/tree/master/gallery/plotly/bubble) | [![swirl.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/plotly/swirl/swirl.gif)](https://github.com/maxhumber/gif/tree/master/gallery/plotly/swirl) | [![waterfall.gif](https://raw.githubusercontent.com/maxhumber/gif/master/gallery/plotly/waterfall/waterfall.gif)](https://github.com/maxhumber/gif/tree/master/gallery/plotly/waterfall) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |




If you have a dope ass animation that you think should be in the Gallery, submit a PR!
