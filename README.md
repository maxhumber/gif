<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/gif/master/logo/gif.png" width="300px" alt="gif">
</h3>
<p align="center">
  <a href="https://github.com/maxhumber/gif/blob/master/setup.py"><img alt="Dependencies" src="https://img.shields.io/badge/dependencies-zero-brightgreen"></a>
  <a href="https://travis-ci.org/maxhumber/gif"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/gif.svg"></a>
  <a href="https://pypi.python.org/pypi/gif"><img alt="PyPI" src="https://img.shields.io/pypi/v/gif.svg"></a>
  <a href="https://pepy.tech/project/gif"><img alt="Downloads" src="https://pepy.tech/badge/gif"></a>
</p>

#### Installation

```
pip install gif
```



#### Usage

```
import random
from matplotlib import pyplot as plt

import gif
```

Decorate your plotting function with `gif.frame`:

```
@gif.frame
def plot(x, y):
    plt.figure(figsize=(5, 5))
    plt.scatter(x, y)
    plt.xlim((0, 100))
    plt.ylim((0, 100))
```

Build a bunch of frames:

```
frames = []
for _ in range(50):
    n = 10
    x = [random.randint(0, 100) for _ in range(10)]
    y = [random.randint(0, 100) for _ in range(10)]
    frame = plot(x, y)
    frames.append(frame)
```

Finally, save the gif:

```
gif.save(frames, 'yay.gif')
```
