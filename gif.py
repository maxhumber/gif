from functools import wraps
from io import BytesIO as Buffer
from typing import Callable, List, TypeVar, ByteString

from matplotlib import pyplot as plt
from numpy import array as numpy_array
from numpy import vsplit as numpy_vsplit
from numpy import vstack as numpy_vstack
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


def _optimize_frames(frames: List[Frame]) -> (List[PI.Image], ByteString):  # type: ignore[valid-type]
    joined_img = PI.fromarray(numpy_vstack(frames))
    joined_img = joined_img.quantize(colors=255, dither=0)
    palette = b"\xff\x00\xff" + joined_img.palette.getdata()[1]
    joined_img_arr = numpy_array(joined_img)
    joined_img_arr += 1
    arrays = numpy_vsplit(joined_img_arr, len(frames))
    prev_array = arrays[0]
    for array in arrays[1:]:
        mask = (array == prev_array)
        prev_array = array.copy()
        array[mask] = 0
    frames_out = [PI.fromarray(array) for array in arrays]
    return frames_out, palette


def save(
    frames: List[Frame],  # type: ignore[valid-type]
    path: str,
    duration: Milliseconds = 100,
    *,
    overlapping: bool = True,
    optimize: bool = False,
) -> None:
    """Save prepared frames to .gif file

    Example:

    ```python
    frames = [plot(i) for i in range(10)]
    gif.save(frames, "test.gif", duration=50)
    ```
    """

    if not path.endswith(".gif"):
        raise ValueError(f"'{path}' must end with .gif")

    kwargs = {}
    if optimize:
        frames, palette = _optimize_frames(frames)
        kwargs = {"palette": palette, "transparency": 0}

    frames[0].save(  # type: ignore
        path,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=duration,
        disposal=0 if overlapping else 2,
        loop=0,
        **kwargs,
    )
