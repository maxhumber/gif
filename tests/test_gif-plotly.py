import gif
import pytest
from PIL import Image

import pandas as pd
import plotly.graph_objects as go

def test_frame():
    df = pd.DataFrame({"t": [1, 2], "x": [5, 10], "y": [5, 10]})

    @gif.frame
    def plot():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["x"], y=df["y"], mode="markers"))
        return fig

    frame = plot()
    assert str(type(frame)) == "<class 'PIL.PngImagePlugin.PngImageFile'>"


@pytest.fixture(scope="session")
def save_gif():
    df = pd.DataFrame({"t": [1, 2], "x": [5, 10], "y": [5, 10]})

    @gif.frame
    def plot(t):
        d = df[df["t"] == t]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=d["x"], y=d["y"], mode="markers"))
        return fig

    frames = [plot(1), plot(2)]
    gif.save(frames, "test-plotly.gif")


def test_save(save_gif):
    im = Image.open("test-plotly.gif")
    assert im.format == "GIF"
