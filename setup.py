# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ecommerce/__init__.py
from ecommerce import __version__ as version

setup(
	name='ecommerce',
	version=version,
	description='An Ecommerce Application for learning purpose',
	author='Devphilip',
	author_email='philipakpeki@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
