from functools import wraps
from io import BytesIO as Buffer
from typing import Callable, List, TypeVar

from matplotlib import pyplot as plt
from PIL import Image as PI


Plot = TypeVar("Plot")
Frame = PI.Image
Milliseconds = float


class Options:
    """Matplotlib export options

    See: ["savefig"](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)

    Example:

    ```python
    gif.options.matplotlib["dpi"] = 300
    ```
    """

    def __init__(self):
        self.matplotlib = {}

    def reset(self) -> None:
        self.matplotlib = {}


options = Options()


def frame(plot: Callable[..., Plot]) -> Callable[..., Frame]:  # type: ignore[valid-type]
    """Prepare plot for animation

    Example:

    ```python
    @gif.frame
    def plot(i):
        plt.scatter(x[:i], y[:i])
        plt.xlim((0, 100))
        plt.ylim((0, 100))
    ```
    """

    @wraps(plot)
    def inner(*args, **kwargs) -> Frame:  # type: ignore[valid-type]
        buffer = Buffer()
        plot(*args, **kwargs)
        plt.savefig(buffer, format="png", **options.matplotlib)
        plt.close()
        buffer.seek(0)
        frame = PI.open(buffer)
        return frame  # type: ignore[no-any-return]

    return inner


def save(
    frames: List[Frame],  # type: ignore[valid-type]
    path: str,
    duration: Milliseconds = 100,
    *,
    overlapping: bool = True,
) -> None:
    """Save prepared frames to .gif file

    Example:

    ```python
    frames = [plot(i) for i in range(10)]
    gif.save(frames, "test.gif", duration=50)
    ```
    """

    if not path.endswith(".gif"):
        raise ValueError("must end with .gif")

    frames[0].save(  # type: ignore
        path,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=duration,
        disposal=0 if overlapping else 2,
        loop=0,
    )
