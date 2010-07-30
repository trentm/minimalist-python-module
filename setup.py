#!/usr/bin/env python

import sys
import os
from setuptools import setup


_top_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_top_dir, "lib"))
try:
    import mpm
finally:
    del sys.path[0]
README = open(os.path.join(_top_dir, 'README.txt')).read()

setup(name='mpm',
    version=mpm.__version__,
    description="a minimalist Python module project (hint: it doesn't do anything)",
    long_description=README,
    classifiers=[c.strip() for c in """
        Development Status :: 1 - Planning
        Intended Audience :: Developers
        License :: OSI Approved :: MIT License
        Operating System :: OS Independent
        Programming Language :: Python :: 2
        Programming Language :: Python :: 2.4
        Programming Language :: Python :: 2.5
        Programming Language :: Python :: 2.6
        Programming Language :: Python :: 2.7
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.1
        Topic :: Software Development :: Libraries :: Python Modules
        """.split('\n') if c.strip()],
    keywords='minimalist python module',
    author='Trent Mick',
    author_email='trentm@gmail.com',
    maintainer='Trent Mick',
    maintainer_email='trentm@gmail.com',
    url='http://github.com/trentm/minimalist-python-module',
    license='MIT',
    py_modules=["mpm"],
    package_dir={"": "lib"},
    include_package_data=True,
    zip_safe=False,
)

