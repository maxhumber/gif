import pytest
from matplotlib import pyplot as plt
from PIL import Image
import gif

@gif.frame
def plot(x, y):
    plt.scatter(x, y)

def test_frame():
    frame = plot([0, 5], [0, 5])
    assert str(type(frame)) == "<class 'PIL.PngImagePlugin.PngImageFile'>"

@pytest.fixture(scope="session")
def saved_gif():
    frames = [plot([0, 5], [0, 5]), plot([0, 10], [0, 10])]
    gif.save(frames, "test-matplotlib.gif")

@pytest.fixture(scope="session")
def saved_gif_kwargs():
    gif.save_kwargs['dpi'] = 200
    frames = [plot([0, 5], [0, 5]), plot([0, 10], [0, 10])]
    gif.save(frames, "test-matplotlib2.gif")

def test_save(saved_gif):
    im = Image.open("test-matplotlib.gif")
    assert im.format == "GIF"

def test_save_kwargs(saved_gif_kwargs):
    im = Image.open("test-matplotlib2.gif")
    assert im.format == "GIF"
