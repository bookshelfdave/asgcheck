# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='asgcheck',
    version='0.1.0',
    description='Ensures ELBs attached to an ASG exist',
    long_description=readme,
    author='Dave Parfitt',
    author_email='dparfitt@mozilla.com',
    url='https://github.com/metadave/asgcheck',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

