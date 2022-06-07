#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   setup.py
@Time    :   2022/06/07 17:11:19
@Author  :   Leon1s
@E-mail  :   Leon1s152427@gmail.com
@Desc    :   Setup Uttu
"""

import setuptools
from sys import version_info
from os.path import dirname, join

if version_info < (3, 6, 0):
    raise SystemExit("Sorry! Uttu requires python 3.6.0 or later.")

with open(join(dirname(__file__), "uttu/VERSION"), "rb") as f:
    version = f.read().decode("ascii").strip()

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = setuptools.find_packages()
packages.extend([
    "uttu",
    "uttu.templates",
    "uttu.templates.project_template",
    "uttu.templates.project_template.spiders",
    "uttu.templates.project_template.items",
])

requires = [
    "better-exceptions>=0.2.2",
    "DBUtils>=2.0",
    "parsel>=1.5.2",
    "PyExecJS>=1.5.1",
    "PyMySQL>=0.9.3",
    "redis>=2.10.6,<4.0.0",
    "requests>=2.22.0",
    "bs4>=0.0.1",
    "ipython>=7.14.0",
    "redis-py-cluster>=2.1.0",
    "cryptography>=3.3.2",
    "selenium>=3.141.0",
    "pymongo>=3.10.1",
    "urllib3>=1.25.8",
    "loguru>=0.5.3",
    "influxdb>=5.3.1",
    "pyperclip>=1.8.2",
    "webdriver-manager>=3.5.3",
]

memory_dedup_requires = ["bitarray>=1.5.3"]
all_requires = memory_dedup_requires

setuptools.setup(
    name="uttu",
    version=version,
    author="Leon1s",
    license="MIT",
    author_email="Leon1s152427@gmail.com",
    python_requires=">=3.6",
    description="Uttu is a next generation distributed crawler framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requires,
    extras_require={"all": all_requires},
    entry_points={"console_scripts": ["feapder = feapder.commands.cmdline:execute"]},
    url="https://github.com/Leon1s97/Uttu.git",
    packages=packages,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
)
