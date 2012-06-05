#!/usr/bin/env python

from setuptools import setup
from requests-RT import rt

def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name = "requests-RT",
    version = giantbomb.__version__,
    author = giantbomb.__author__,
    author_email = "mahmoud.h.hanafy@gmail.com",
    description = ("A Python wrapper for the Rotten Tomatoes API."),
    license = "MIT",
    keywords = "rotten tomatoes rt api wrapper",
    url = "https://github.com/mahmoudhossam/requests-RT",
    packages=['requests-RT'],
    long_description=read('README.rst'),
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)