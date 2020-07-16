# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in infinicserp/__init__.py
from infinicserp import __version__ as version

setup(
	name='infinicserp',
	version=version,
	description='Infinics ERP - Used by more than 5000 companies across the world',
	author='Infinics Limited',
	author_email='info@infinics.co.uk',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
