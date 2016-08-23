#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='cloudy',
    version='0.1.0',
    description="cloudy is the python equivalnlent of mer_stamps in idl",
    long_description=readme + '\n\n' + history,
    author="Perry Vargas",
    author_email='perrybvargas@gmail.com',
    url='https://github.com/pbvarga1/cloudy',
    packages=[
        'cloudy',
    ],
    package_dir={'cloudy':
                 'cloudy'},
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas'
    ],
    license="BSD",
    zip_safe=False,
    keywords='cloudy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
