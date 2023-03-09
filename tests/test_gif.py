import os

import pytest
from matplotlib import pyplot as plt
from PIL import Image
from PIL.PngImagePlugin import PngImageFile

import gif


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


def make_gif(tmpdir_factory, filename, dpi=None, **kwargs):
    if dpi is not None:
        gif.options.matplotlib["dpi"] = 300
    frames = [plot([0, 5], [0, 5]), plot([0, 10], [0, 10])]
    if dpi is not None:
        gif.options.reset()
    path = str(tmpdir_factory.mktemp("matplotlib").join(filename))
    gif.save(frames, path, **kwargs)
    return path


@pytest.fixture(scope="session")
def default_file(tmpdir_factory):
    return make_gif(tmpdir_factory, "default.gif")


@pytest.fixture(scope="session")
def optimized_file(tmpdir_factory):
    return make_gif(tmpdir_factory, "optimized.gif", optimize=True)


@pytest.fixture(scope="session")
def hd_file(tmpdir_factory):
    return make_gif(tmpdir_factory, "hd.gif", dpi=300)


@pytest.fixture(scope="session")
def long_file(tmpdir_factory):
    return make_gif(tmpdir_factory, "long.gif", duration=2500)


def test_frame():
    frame = plot([0, 5], [0, 5])
    assert isinstance(frame, PngImageFile)


def test_default_save(default_file):
    img = Image.open(default_file)
    assert img.format == "GIF"
    assert milliseconds(img) == 200


def test_optimization(default_file, optimized_file):
    default_size = os.stat(default_file).st_size
    optimized_size = os.stat(optimized_file).st_size
    assert optimized_size < default_size * 0.9


def test_dpi_save(hd_file):
    img = Image.open(hd_file)
    assert img.format == "GIF"
    assert milliseconds(img) == 200


def test_long_save(long_file):
    img = Image.open(long_file)
    assert img.format == "GIF"
    assert milliseconds(img) == 5000
