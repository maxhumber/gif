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
    plt.figure(figsize=(5, 5))
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
gif.save(frames, 'random.gif', duration=100)
```



#### Examples

<div>
<p>Random (<a href="https://github.com/maxhumber/gif/blob/master/examples/random.py">code</a>):
<br/>
<img src="https://raw.githubusercontent.com/maxhumber/gif/master/examples/random.gif" style="zoom:67%;" />
<br/>
<p>Preferential Attachment (<a href="https://github.com/maxhumber/gif/blob/master/examples/attachment.py">code</a>, <a href="https://en.wikipedia.org/wiki/Preferential_attachment">theory</a>):</p>
<br/>
<img src="https://raw.githubusercontent.com/maxhumber/gif/master/examples/attachment.gif" style="zoom:50%;" />
<p>Wave (<a href="https://github.com/maxhumber/gif/blob/master/examples/sin.py">code</a>, <a href="http://louistiao.me/posts/notebooks/save-matplotlib-animations-as-gifs/">original</a>):</p>
<br/>
<img src="https://raw.githubusercontent.com/maxhumber/gif/master/examples/sin.gif" style="zoom:67%;" />
<br/>
</div>
