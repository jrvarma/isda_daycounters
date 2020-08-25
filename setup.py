#!/usr/bin/env python
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='isda_daycounters',
      version='1.0',
      maintainer='Mitchell Snaith',
      # maintainer_email='',
      description='ISDA day-count conventions with year-fractions and day-counts',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/miradulo/isda_daycounters",
      packages=['isda_daycounters'],
      install_requires=[],
      extras_require={},
      entry_points={},
      classifiers=[
          # "License :: OSI Approved :: GPL3",
          "Programming Language :: Python :: 3",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.0',
)
