from functools import wraps
from io import BytesIO as Buffer
from PIL import Image


class Options:
    """Global **kwargs save/export options (refer to extension docs)

    Altair | Truncated list of **kwargs save/export settings:

    - scale_factor (float): The scale factor to use when exporting the figure

    matplotlib | Truncated list of **kwargs save/export settings:

    - dpi (int): The resolution in dots per inch
    - facecolor (colorspec): The facecolor of the figure
    - edgecolor (colorspec): The edgecolor of the figure
    - transparent (bool): If True, the axes patches will all be transparent

    Plotly | Truncated list **kwargs save/export settings:

    - width (int): The width of the exported image in layout pixels
    - height (int): The height of the exported image in layout pixels
    - scale (float): The scale factor to use when exporting the figure

    Examples:

    ```
    gif.options.altair["scale_factor"] = 2
    gif.options.matplotlib["dpi"] = 300
    gif.options.plotly["scale"] = 0.5
    ```
    """

    def __init__(self):
        self._extensions = {"altair": True, "matplotlib": True, "plotly": True}
        self.altair = {}
        self.matplotlib = {}
        self.plotly = {}


options = Options()


# Extension compatibility checks


try:
    from altair_saver import save as save_altair
except ModuleNotFoundError:
    options._extensions["altair"] = False


try:
    from matplotlib import pyplot as plt
except ModuleNotFoundError:
    options._extensions["matplotlib"] = False


try:
    import kaleido
except ModuleNotFoundError:
    options._extensions["plotly"] = False


# Buffer and triage functions


def buffer_altair(plot, buffer):
    kwargs = options.altair
    save_altair(plot, buffer, fmt="png", **kwargs)


def buffer_matplotlib(plot, buffer):
    kwargs = options.matplotlib
    plt.savefig(buffer, format="png", **kwargs)
    plt.close()


def buffer_plotly(plot, buffer):
    kwargs = options.plotly
    plot.write_image(buffer, format="png", **kwargs)


class MissingExtension(Exception):
    pass


def triage(plot, buffer):
    if "altair" in str(type(plot)):
        if not options._extensions["altair"]:
            raise MissingExtension("pip install gif[altair]")
        buffer_altair(plot, buffer)
    elif "plotly" in str(type(plot)):
        if not options._extensions["plotly"]:
            raise MissingExtension("pip install gif[plotly]")
        buffer_plotly(plot, buffer)
    else:
        if not options._extensions["matplotlib"]:
            raise MissingExtension("pip install gif[matplotlib]")
        buffer_matplotlib(plot, buffer)


# Main API


def frame(func):
    """Plot function decorator.

    Usage (Altair):
    ```
    @gif.frame
    def plot(i):
        d = df[df['i'] <= i]
        chart = alt.Chart(d).mark_circle().encode(
            x=alt.X('x', scale=alt.Scale(domain=(0, 100))),
            y=alt.Y('y', scale=alt.Scale(domain=(0, 100)))
        )
        return chart
    ```

    Usage (matplotlib):
    ```
    @gif.frame
    def plot(i):
        plt.scatter(x[:i], y[:i])
        plt.xlim((0, 100))
        plt.ylim((0, 100))
    ```

    Usage (Plotly):
    ```
    @frame
    def plot(i):
        layout = go.Layout(
            xaxis = {'range': [0, 100]},
            yaxis = {'range': [0, 100]}
        )
        fig = go.Figure(layout=layout)
        fig.add_trace(go.Scatter(x=x[:i], y=y[:i], mode="markers"))
        return fig
    ```
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        buffer = Buffer()
        plot = func(*args, **kwargs)
        triage(plot, buffer)
        buffer.seek(0)
        image = Image.open(buffer)
        return image

    return wrapper


def save(frames, path, duration=100, unit="milliseconds", between="frames", loop=True):
    """Save decorated frames to an animated gif.

    - frames (list): collection of frames built with the gif.frame decorator
    - path (str): filename with relative/absolute path
    - duration (int/float): time (with reference to unit and between)
    - unit {"ms" or "milliseconds", "s" or "seconds"}: time unit value
    - between {"frames", "startend"}: duration between "frames" or the entire gif ("startend")
    - loop (bool): infinitely loop the animation

    Example:
    ```
    frames = []
    for i in range(10):
        frame = plot(i)
        frames.append(frame)

    gif.save(frames, "test.gif", duration=100)
    ```
    """

    if unit in ["ms", "milliseconds"]:
        pass
    elif unit in ["s", "seconds"]:
        duration *= 1000
    else:
        raise ValueError(unit)

    if between == "frames":
        pass
    elif between == "startend":
        duration /= len(frames)
    else:
        raise ValueError(between)

    kwargs = {}

    if loop:
        kwargs["loop"] = 0

    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=duration,
        **kwargs
    )
