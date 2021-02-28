import io
import os
import re

from setuptools import find_packages
from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="test_evocraft_py",
    version='0.1.7',
    license='MIT',

    author="Shyam Sudhakaran",
    author_email="shyamsnair@protonmail.com",

    description="Python client for Evocraft",

    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=find_packages(include=['test_evocraft_py'], exclude=('tests',)),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],

    include_package_data=True,
    entry_points={
        'console_scripts': [
            'test-evocraft-py=test_evocraft_py.cli:main',
        ],
    },
)
