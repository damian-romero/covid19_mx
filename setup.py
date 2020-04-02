# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='covid19_mx',
    version='0.1.0',
    description='Un repositorio muy sencillo para explorar los datos de infección por covid-19...',
    long_description=readme,
    author='Damian Romero',
    author_email='NA',
    url='https://github.com/damian-romero/covid19_mx/pull/1',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
