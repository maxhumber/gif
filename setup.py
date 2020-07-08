from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gif",
    version="2.0.0",
    description="✨ The extension for matplotlib and Altair animations",
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
        "matplotlib",
        "altair",
        "PIL",
        "Pillow",
    ],
    url="https://github.com/maxhumber/gif",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    license="MIT",
    py_modules=["gif"],
    install_requires=["matplotlib>=3.1.0", "Pillow>=5.2.0,!=7.1.0,!=7.1.1"],
    extras_require={
        "altair": ["altair-saver>=0.5.0"],
        "test": [
            "pytest>=5.2.0",
            "pandas>=1.0.0",
            "selenium>=3.141.0",
            "altair-saver>=0.5.0",
        ],
    },
    python_requires=">=3.6",
    setup_requires=["setuptools>=38.6.0"],
)
