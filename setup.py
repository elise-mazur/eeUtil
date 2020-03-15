#!/usr/bin/env python
from setuptools import setup

with open('README.md') as f:
    desc = f.read()

setup(
    name='eeUtil',
    version='0.2.0',
    description='Python wrapper for easier data management on Google Earth Engine.',
    long_description=desc,
    license='MIT',
    author='Francis Gassert',
    url='https://github.com/fgassert/eeUtil',
    packages=['eeUtil'],
    install_requires=[
        'earthengine-api>=0.1.200,<0.2',
        'google-cloud-storage>=1.4.0,<2',
        'oauth2client>=4,<5'
    ]
)
