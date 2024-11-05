FROM python:3.13 AS build


WORKDIR /wd

RUN pip3 install setuptools auditwheel build twine

RUN wget https://github.com/NixOS/patchelf/releases/download/0.18.0/patchelf-0.18.0-aarch64.tar.gz
RUN tar -xvf patchelf-0.18.0-aarch64.tar.gz
RUN cp bin/patchelf /usr/local/bin

ADD example example
ADD setup.py .
ADD README.rst .

RUN python3 -m build --wheel --outdir local-dist
RUN auditwheel repair --plat manylinux_2_31_aarch64 --strip local-dist/*.whl --wheel-dir dist
RUN twine check dist/*.whl
