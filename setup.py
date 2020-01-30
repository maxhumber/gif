from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gif",
    version="0.1",
    description="work in progress",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
    url="https://github.com/maxhumber/gif",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    license="MIT",
    py_modules=["gif"],
    # packages=find_packages(),
    install_requires=["matplotlib", "Pillow"],
    python_requires=">=3.6",
    setup_requires=["setuptools>=38.6.0"],
)
