#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/spikeTTL.svg
        :target: https://pypi.python.org/pypi/spikeTTL
.. image:: https://img.shields.io/travis/chongxi/spikeTTL.svg
        :target: https://travis-ci.org/chongxi/spikeTTL

Python Boilerplate contains all the boilerplate you need to create a Python package.


Links:
---------
* `Github <https://github.com/chongxi/spikeTTL>`_
"""

from setuptools import setup, find_packages

requirements = ['Click>=6.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="chongxi lai",
    author_email='chongxi.lai@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        'console_scripts': [
            'spikeTTL=spikeTTL.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=__doc__,
    include_package_data=True,
    keywords='spikeTTL',
    name='spikeTTL',
    packages=find_packages(include=['spikeTTL']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/chongxi/spikeTTL',
    version='0.1.0',
    zip_safe=False,
)
