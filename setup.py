from setuptools import setup, find_packages
import codecs
import os
from pathlib import Path


VERSION = '0.1.1'
DESCRIPTION = 'Utils for strings in python'
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()
URL = "https://github.com/BabyEntchen/string_py"

# Setting up
setup(
    name="string_py",
    version=VERSION,
    author="BabyEntchen",
    author_email="<baby_entchen@web.de>",
    url=URL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'string', 'strings', 'utils', 'string utils', 'random', 'random strings', 'formatting', 'formatter'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
