from setuptools import setup, find_packages
import pathlib


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

VERSION = '1.0.3'
DESCRIPTION = 'An image modification package.'

# Setting up
setup(
    name="imodif",
    version=VERSION,
    author="Abiah Sylvester",
    author_email="abiahsylvester759@gmail.com",
    description=DESCRIPTION,
    long_description=README,
    license="MIT",
    long_description_content_type="text/markdown",
    packages=["imodif"],
    python_requires='>=3.8',
    install_requires=["numpy", "opencv-python"],

    keywords=['python', 'image', "modifier",
              "darkness", "brightness", "contrast"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
