#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Allow trove classifiers in previous python versions
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

from templi import __version__ as version

def requireModules(moduleNames=None):
    import re
    if moduleNames is None:
        moduleNames = []
    else:
        moduleNames = moduleNames

    commentPattern = re.compile(r'^\w*?#')
    moduleNames.extend(
        filter(lambda line: not commentPattern.match(line), 
            open('requirements.txt').readlines()))

    return moduleNames

setup(
    name    = 'templi',
    version = version,

    author       = 'Alejandro Gallo',
    author_email = 'alejandroamsg@gmail.com',
    url          = "http://github.com/alejandroamsg@gmail.com/templi",

    description      = 'Little command line template utility',
    long_description = open('README.rst').read(),
    classifiers      = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers'
    ],

    scripts          = ["tools/templi"],
    install_requires = requireModules([
        "pystache"
        ]),

    test_suite = 'templi',
    zip_sage   = False
)
