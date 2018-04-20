#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2018  Daniele Giudice
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup

setup(
    name = 'winsyspath',
    packages = ['winsyspath'],
    version = '0.1.0',
    description = 'Definitive Python wrapper for Windows System Path',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author = 'Daniele Giudice',
    license = 'GPL v3',
    python_requires='>=2.7, <4',
    install_requires=[
        'winvers>=0.1.3'
    ]
    url = 'https://github.com/MagicGreenDragon/winsyspath',
    keywords = ['windows', 'system', 'path', 'environment', 'variable'],
    classifiers = (
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        ),
)
