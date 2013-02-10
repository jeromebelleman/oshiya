#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='oshiya',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Push LSF jobs through the scheduler",
    long_description="Manually push LSF jobs through the scheduler by running brun if they get inexplicably stuck.",
    scripts=['oshiya'],
    data_files=[('share/man/man1', ['oshiya.1'])],
)
