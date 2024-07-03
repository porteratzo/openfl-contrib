# Copyright (C) 2020-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""This package includes dependencies of the openfl project."""

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='openfl_contrib',
    version='0.1',
    author='Intel Corporation',
    description='Academic and research contributions to OpenFL',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/intel/openfl-contrib',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    setup_requires=['openfl @ git+https://github.com/securefederatedai/openfl.git@develop',],
    python_requires='>=3.8, <3.12',
    project_urls={
        'Bug Tracker': 'https://github.com/intel/openfl-contrib/issues',
        'Source Code': 'https://github.com/intel/openfl-contrib',
    },
    classifiers=[
        'Environment :: Console',
        # How mature is this project? Common values are
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: System :: Distributed Computing',
        # Pick your license as you wish
        'License :: OSI Approved :: Apache Software License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',

    ],
)
