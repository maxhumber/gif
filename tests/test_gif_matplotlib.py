import gif

from matplotlib import pyplot as plt
from PIL import Image
from PIL.PngImagePlugin import PngImageFile

import pytest


def milliseconds(img):
    img.seek(0)
    duration = 0
    while True:
        try:
            duration += img.info["duration"]
            img.seek(img.tell() + 1)
        except EOFError:
            return duration


@gif.frame
def plot(x, y):
    plt.scatter(x, y)


@pytest.fixture(scope="session")
def default_file(tmpdir_factory):
    frames = [plot([0, 5], [0, 5]), plot([0, 10], [0, 10])]
    path = str(tmpdir_factory.mktemp("matplotlib").join("default.gif"))
    gif.save(frames, path)
    return path


@pytest.fixture(scope="session")
def hd_file(tmpdir_factory):
    gif.options.matplotlib["dpi"] = 300
    frames = [plot([0, 5], [0, 5]), plot([0, 10], [0, 10])]
    del gif.options.matplotlib["dpi"]
    path = str(tmpdir_factory.mktemp("matplotlib").join("hd.gif"))
    gif.save(frames, path)
    return path


@pytest.fixture(scope="session")
def long_file(tmpdir_factory):
    frames = [plot([0, 5], [0, 5]), plot([0, 10], [0, 10])]
    path = str(tmpdir_factory.mktemp("matplotlib").join("long.gif"))
    gif.save(frames, path, duration=5, unit="s", between="startend")
    return path


def test_frame():
    frame = plot([0, 5], [0, 5])
    assert isinstance(frame, PngImageFile)


def test_default_save(default_file):
    img = Image.open(default_file)
    assert img.format == "GIF"
    assert milliseconds(img) == 200


def test_dpi_save(hd_file):
    img = Image.open(hd_file)
    assert img.format == "GIF"
    assert milliseconds(img) == 200


def test_long_save(long_file):
    img = Image.open(long_file)
    assert img.format == "GIF"
    assert milliseconds(img) == 5000
