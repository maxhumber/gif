from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gif",
    version="3.0.0",
    description="The extension for matplotlib, Altair, and Plotly animations",
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
    install_requires=["Pillow>=7.1.2"],
    extras_require={
        "altair": ["altair>=4.1.0", "altair-saver>=0.5.0"],
        "matplotlib": ["matplotlib>=3.1.0"],
        "plotly": ["plotly>=4.9.0", "kaleido>=0.0.3.post1"],
        "test": [
            "altair>=4.1.0",
            "matplotlib>=3.1.0",
            "plotly>=4.9.0",
            "pytest>=5.2.0",
            "pandas>=1.0.0",
            "selenium>=3.141.0",
            "altair-saver>=0.5.0",
            "kaleido>=0.0.3.post1",
        ],
    },
    python_requires=">=3.6",
    setup_requires=["setuptools>=38.6.0"],
)
