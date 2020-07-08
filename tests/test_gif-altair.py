import pytest
import altair as alt
import pandas as pd
from PIL import Image
import gif


def test_frame():
    df = pd.DataFrame({"t": [1, 2], "x": [5, 10], "y": [5, 10]})

    @gif.frame
    def plot():
        return alt.Chart(df).encode(x="x", y="y").mark_circle()

    frame = plot()
    assert str(type(frame)) == "<class 'PIL.PngImagePlugin.PngImageFile'>"


@pytest.fixture(scope="session")
def saved_gif():
    df = pd.DataFrame({"t": [1, 2], "x": [5, 10], "y": [5, 10]})

    @gif.frame
    def plot(t):
        d = df[df["t"] == t]
        return alt.Chart(d).encode(x="x", y="y").mark_circle()

    frames = [plot(1), plot(2)]
    gif.save(frames, "test-altair.gif")


def test_save(saved_gif):
    im = Image.open("test-altair.gif")
    assert im.format == "GIF"
