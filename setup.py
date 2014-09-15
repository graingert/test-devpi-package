#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


from setuptools import setup, find_packages

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='ingest-test-files',
    version='0.1.1.dev0',
    description='Test files for ingest',
    long_description=readme + '\n\n' + history,
    author='Hogarth Worldwide',
    author_email='umbrella@hogarthww.com',
    url='https://github.hogarthww.prv/umbrella/ingest-test-files',
    packages=find_packages('src', exclude=('tests',)),
    package_dir={'': 'src'},
    include_package_data=True,
    license="PROPRIETARY",
    keywords='test files ingest'
)
