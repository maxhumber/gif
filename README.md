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

`gif` is a better way to build animated Matplotlib gifs.



#### Installation

```
pip install -U gif
```



#### Usage

`gif` is easy to use. Just import:

```
import gif
from matplotlib import pyplot as plt
```

Decorate a Matplotlib plot function with `gif.frame`:

```
@gif.frame
def plot(x, y):
    plt.figure(figsize=(5, 3), dpi=100)
    plt.scatter(x, y)
    plt.xlim((0, 100))
    plt.ylim((0, 100))
```

Build a bunch of "frames" with a standard for loop:

```
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



---



#### Examples

Chaos ([code](https://github.com/maxhumber/gif/blob/master/examples/chaos.py)):
![chaos.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/chaos.gif)

Preferential Attachment ([code](https://github.com/maxhumber/gif/blob/master/examples/attachment.py), [theory](https://en.wikipedia.org/wiki/Preferential_attachment)):
![attachment.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/attachment.gif)

Wave ([code](https://github.com/maxhumber/gif/blob/master/examples/wave.py), [original](http://louistiao.me/posts/notebooks/save-matplotlib-animations-as-gifs):
![wave.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/wave.gif)

Hypothetical Outcome Plot ([code](https://github.com/maxhumber/gif/blob/master/examples/hop.py), [original](https://www.r-bloggers.com/hypothetical-outcome-plots/)):
![hop.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/hop.gif)

Polar Plot ([code](https://github.com/maxhumber/gif/blob/master/examples/canada.py), [data](https://www150.statcan.gc.ca/t1/tbl1/en/cv.action?pid=2410000301#timeframe), [inspiration](https://www.dataquest.io/blog/climate-temperature-spirals-python/)):

![canada.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/canada.gif)

3D ([code](https://github.com/maxhumber/gif/blob/master/examples/3D.py), [inspiration](https://stackoverflow.com/questions/48563526/drawing-a-logarithmic-spiral-in-three-axes-in-python)):

![3D.gif](https://raw.githubusercontent.com/maxhumber/gif/master/examples/3D.gif)





