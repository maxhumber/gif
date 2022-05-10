import gif

from PIL import Image
from PIL.PngImagePlugin import PngImageFile
import pandas as pd
import plotly.graph_objects as go

import pytest


df = pd.DataFrame({"t": [1, 2], "x": [5, 10], "y": [5, 10]})


@gif.frame
def plot(t=1):
    d = df[df["t"] == t]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=d["x"], y=d["y"], mode="markers"))
    return fig


@pytest.fixture(scope="session")
def default_file(tmpdir_factory):
    frames = [plot(1), plot(2)]
    path = str(tmpdir_factory.mktemp("plotly").join("default.gif"))
    gif.save(frames, path)
    return path


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_frame():
    frame = plot()
    assert isinstance(frame, PngImageFile)


def test_save(default_file):
    img = Image.open(default_file)
    assert img.format == "GIF"
