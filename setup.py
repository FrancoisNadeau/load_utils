#!usr/bin/env/python3

import setuptools
from setuptools import setup

setup(
    name='loadutils',
    version=attr: loadutils.__version__,
    author='francois.nadeau.1',
    author_email='francois.nadeau.1@umontreal.ca',
    description="Helpful functions to list, iterate through and classify files and directories",
    long_description="https://docs.google.com/presentation/d/1BI7jIQGiV0lK_qb9qyL6B5GP4v5QLX9ubBFBavoe3ws/edit?usp=sharing",
    long_description_content_type='text/x-rst',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    url='https://github.com/FrancoisNadeau/loadutils.git',
    python_requires=">=3.6",
)


