#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" nirodents setup script """
import sys
from setuptools import setup
import versioneer

# Give setuptools a hint to complain if it's too old a version
# 30.3.0 allows us to put most metadata in setup.cfg
# 30.4.0 gives us options.packages.find
# Should match pyproject.toml
SETUP_REQUIRES = ['setuptools >= 30.4.0']
# This enables setuptools to install wheel on-the-fly
SETUP_REQUIRES += ['wheel'] if 'bdist_wheel' in sys.argv else []

if __name__ == '__main__':
    setup(name='nirodents',
          version=versioneer.get_version(),
          cmdclass=versioneer.get_cmdclass(),
          setup_requires=SETUP_REQUIRES,
          )