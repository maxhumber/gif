import gif
import pytest
from PIL import Image

from matplotlib import pyplot as plt


def test_frame():
    @gif.frame
    def plot(x, y):
        plt.scatter(x, y)

    frame = plot([0, 5], [0, 5])
    assert str(type(frame)) == "<class 'PIL.PngImagePlugin.PngImageFile'>"


@pytest.fixture(scope="session")
def save_gif():
    @gif.frame
    def plot(x, y):
        plt.scatter(x, y)

    frames = [plot([0, 5], [0, 5]), plot([0, 10], [0, 10])]
    gif.save(frames, "test-matplotlib.gif")


def test_save(save_gif):
    im = Image.open("test-matplotlib.gif")
    assert im.format == "GIF"


@pytest.fixture(scope="session")
def save_gif_with_options():
    gif.options.matplotlib["dpi"] = 300
    @gif.frame
    def plot(x, y):
        plt.scatter(x, y)

    frames = [plot([0, 5], [0, 5]), plot([0, 10], [0, 10])]
    gif.save(frames, "test-matplotlib_2s.gif", duration=2, unit="s", between="startend")


def test_options(save_gif_with_options):
    im = Image.open("test-matplotlib_2s.gif")
    assert im.format == "GIF"
