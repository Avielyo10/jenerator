#!/usr/bin/env python3
import os

from setuptools import setup

os.environ['PBR_VERSION'] = '2.0'
setup(
    description='Jenkins Plugin Generator - creates fast templates of jenkins plugins',
    setup_requires=['pbr'],
    python_requires='~=3.6',
    include_package_data=True,
    pbr=True,
    zip_safe=False
)
