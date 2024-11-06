# Copyright 2024 Vincent Jacques

import sys

import setuptools


with open("README.rst") as f:
    long_description = f.read()

if sys.platform == "linux":
    extra_compile_args = ["-std=c++17", "-fopenmp"]
    extra_link_args = ["-fopenmp"]
elif sys.platform == "win32":
    extra_compile_args = ["/std:c++17", "/openmp"]
    extra_link_args = []
elif sys.platform == "darwin":
    extra_compile_args = ["-std=c++17", "-Xclang", "-fopenmp"]
    extra_link_args = ["-lomp"]
else:
    raise NotImplementedError(f"Unsupported platform: {sys.platform}")

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
        sources=["example/libexample/module.cpp"],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
    )],
)
