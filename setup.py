#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
	long_description = readme.read()

name = 'hgtools'
description = 'Classes and setuptools plugin for Mercurial and Git repositories'

params = dict(
	name=name,
	use_scm_version=True,
	author="Jannis Leidel/Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description=description or name,
	long_description=long_description,
	url="https://github.com/jaraco/" + name,
	packages=setuptools.find_packages(),
	include_package_data=True,
	namespace_packages=name.split('.')[:-1],
	install_requires=[
	],
	extras_require={
	},
	setup_requires=[
		'setuptools_scm>=1.15.0',
	],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
		"Topic :: Software Development :: Version Control",
		"Framework :: Setuptools Plugin",
	],
	entry_points={
		"setuptools.file_finders": [
			"hg = hgtools.plugins:file_finder"
		],
		"distutils.setup_keywords": [
			"use_hg_version = hgtools.plugins:version_calc",
			"use_vcs_version = hgtools.plugins:version_calc",
		],
	},
)
if __name__ == '__main__':
	setuptools.setup(**params)
