from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gif",
    version="1.0",
    description="✨ Better animated Matplotlib gifs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Multimedia :: Graphics",
    ],
    keywords=["gif", "gifs", "animated", "animation", "matplotlib", "PIL", "Pillow"],
    url="https://github.com/maxhumber/gif",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    license="MIT",
    py_modules=["gif"],
    install_requires=["matplotlib", "Pillow"],
    # extras_require = {
    #     'display': ["IPython"] # TODO
    # },
    python_requires=">=3.6",
    setup_requires=["setuptools>=38.6.0"],
)
