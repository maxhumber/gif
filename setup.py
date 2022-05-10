from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gif",
    version="4.0",
    description="The animation extension for matplotlib, Altair, and Plotly graphs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Multimedia :: Graphics",
    ],
    keywords=[
        "gif",
        "gifs",
        "animated",
        "animation",
        "pil",
        "pillow",
        "matplotlib",
        "altair",
        "plotly",
    ],
    url="https://github.com/maxhumber/gif",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    license="MIT",
    py_modules=["gif"],
    install_requires=["Pillow>=9.1.0"],
    extras_require={
        "altair": ["altair>=4.2.0", "altair-saver>=0.5.0"],
        "matplotlib": ["matplotlib>=3.5.2"],
        "plotly": ["plotly>=5.7.0", "kaleido>=0.2.1"],
        "test": [
            "altair>=4.2.0",
            "matplotlib>=3.5.2",
            "plotly>=5.7.0",
            "pytest>=7.1.2",
            "pandas>=1.4.2",
            "selenium>=4.1.5",
            "altair-saver>=0.5.0",
            "kaleido>=0.2.1",
            "black>=22.3.0",
        ],
    },
    python_requires=">=3.7",
    setup_requires=["setuptools>=62.1.0"],
)
