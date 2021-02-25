import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())

setup(
    name="test_evocraft_py",
    version="0.1.0",
    url="https://github.com/kragniz/cookiecutter-pypackage-minimal",
    license='MIT',

    author="Shyam Sudhakaran",
    author_email="shyamsnair@protonmail.com",

    description="Python client for Evocraft",

    # long_description_content_type="text/markdown",
    # long_description=read("README.md"),

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
