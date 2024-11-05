# Copyright 2024 Vincent Jacques

import setuptools


setuptools.setup(
    name="jacquev6-multiplatform-example",
    version="0.1.0",
    description="An example package for building C/C++ extensions for multiple OSes and architectures",
    url="https://github.com/jacquev6/jacquev6-multiplatform-example",
    author="Vincent Jacques",
    author_email="vincent@vincent-jacques.net",
    packages=setuptools.find_packages(),
    ext_modules=[setuptools.Extension(
        name="libexample",
        sources=["example/libexample/module.c"],
    )],
)
