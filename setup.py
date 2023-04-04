from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Utils for strings in python'
LONG_DESCRIPTION = 'A package that provides useful functions for strings in python'

# Setting up
setup(
    name="string_py",
    version=VERSION,
    author="BabyEntchen",
    author_email="<baby_entchen@web.de>",
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
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)