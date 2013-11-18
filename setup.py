from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name="asv",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'asv = asv.main:main'
        ]
    },

    install_requires=[
        'six>=1.4'
    ],

    package_data={
        str('asv'): [
            'www/*.html',
            'www/*.js',
            'www/*.css',
            'www/*.png',
            'www/*.ico',
            'www/jquery/*.js',
            'www/flot/*.js',
            'www/bootstrap/*.js',
            'www/bootstrap/*.css',
            'template/asv.conf.json',
            'template/benchmarks/benchmarks.py'
        ]
    },

    author="Michael Droettboom",
    author_email="mdroe@stsci.edu",
    description="Airspeed Velocity: A simple Python history benchmarking tool",
    license="BSD",
    url="http://github.com/spacetelescope/asv"
)