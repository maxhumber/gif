import gif
from PIL import Image
import pytest


def test_frame():
    @gif.frame
    def plot(x, y):
        plt.scatter(x, y)

    frame = plot([10, 20], [30, 40])
    assert str(type(frame)) == "<class 'PIL.PngImagePlugin.PngImageFile'>"


@pytest.fixture(scope="session")
def saved_gif():
    @gif.frame
    def plot(x, y):
        plt.scatter(x, y)

    frames = [plot([10, 20], [30, 40]), plot([20, 30], [40, 50])]
    gif.save(frames, "test.gif")


def test_save(saved_gif):
    im = Image.open("test.gif")
    assert im.format == "GIF"
