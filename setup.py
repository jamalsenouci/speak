#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup Script for Speak

You can install Speak with

python setup.py install
"""

import os
import re
import sys

from setuptools import find_packages, setup

if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")
    print()

if sys.version_info[:2] < (3, 3):
    print("Speak requires Python 3.3 or later (%d.%d detected)." %
          sys.version_info[:2])
    sys.exit(-1)

with open(os.path.join("speak", "__init__.py"), "r") as f:
    version = re.search("__version__ = \"([^\"]+)\"", f.read()).group(1)

try:
    import pypandoc
    readme = pypandoc.convert("README.md", "rst")
except ImportError:
    with open("README.md", "r") as f:
      readme = f.read()

classifiers = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Developers",
               "Intended Audience :: End Users/Desktop",
               "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Programming Language :: Python :: 3",
               "Programming Language :: Python :: 3 :: Only",
               "Programming Language :: Python :: 3.3",
               "Programming Language :: Python :: 3.4",
               "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
               "Topic :: Multimedia :: Sound/Audio :: Speech",
               "Topic :: Utilities"]

requirements = ['requests>=2.3.0,<2.6.0']
setup(name="speak",
      version=version,
      author="jamalsenouci",
      packages=find_packages(),
      entry_points={"console_scripts": ["speak = speak:cl_main"]},
      install_requires=requirements,
      description="Read text using Google voice tts service",
      long_description=readme,
      license='LICENSE.txt',
      url="https://github.com/jamalsenouci/speak",
      download_url="https://github.com/jamalsenouci/speak/archive/%s.tar.gz" % (version),
      keywords=["speech", "audio", "synthesis", "voice", "google"],
      classifiers=classifiers,
      test_suite='nose.collector',
      tests_require=['nose>=0.10.1'])
