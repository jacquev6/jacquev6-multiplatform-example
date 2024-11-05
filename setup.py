# Copyright 2024 Vincent Jacques

import setuptools


with open("README.rst") as f:
    long_description = f.read()

setuptools.setup(
    name="example",
    version="1.0",
    description="An example package for building C/C++ extensions for multiple OSes and architectures",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/jacquev6/jacquev6-multiplatform-example",
    author="Vincent Jacques",
    author_email="vincent@vincent-jacques.net",
    packages=setuptools.find_packages(),
    ext_modules=[setuptools.Extension(
        name="libexample",
        sources=["example/libexample/module.c"],
    )],
)
