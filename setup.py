# This file is part of "oracc2csv"
# by Tom Elliott
# (c) Copyright 2022 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oracc2csv",
    version="0.0.1",
    author="Tom Elliott",
    author_email="tom.elliott@nyu.edu",
    description="oracc2csv",
    license='AGPL-3.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_url="https://github.com/isawnyu/oracc2csv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10.4",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    install_requires=['airtight'],
    python_requires='>=3.10.4'
)
