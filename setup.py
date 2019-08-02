# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

__version__ = '0.0.1'


setup(
    name="app_payment",
    version=__version__,
    packages=find_packages(exclude=["tests.*", "tests", "docs"]),
    description="Payment application",
    long_description="Payment application",
    author="jiao.xue",
    author_email="jiao.xuejiao@gmial.com",
    include_package_data=True,
    zip_safe=False,
    license="Proprietary",
    keywords=("payment", "service"),
    platforms="any",
    install_requires=[],
    entry_points={},
)
