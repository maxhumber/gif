import pytest
from matplotlib import pyplot as plt
from PIL import Image
import gif


def test_frame():
    @gif.frame
    def plot(x, y):
        plt.scatter(x, y)

    frame = plot([0, 5], [0, 5])
    assert str(type(frame)) == "<class 'PIL.PngImagePlugin.PngImageFile'>"


@pytest.fixture(scope="session")
def saved_gif():
    @gif.frame
    def plot(x, y):
        plt.scatter(x, y)

    frames = [plot([0, 5], [0, 5]), plot([0, 10], [0, 10])]
    gif.save(frames, "test-matplotlib.gif")


def test_save(saved_gif):
    im = Image.open("test-matplotlib.gif")
    assert im.format == "GIF"
