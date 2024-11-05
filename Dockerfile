ARG PYTHON_VERSION=3.8
FROM python:$PYTHON_VERSION AS build

WORKDIR /wd

RUN pip3 install setuptools auditwheel build twine

RUN set -x \
 && mkdir download-patchelf \
 && cd download-patchelf \
 && wget https://github.com/NixOS/patchelf/releases/download/0.18.0/patchelf-0.18.0-aarch64.tar.gz \
 && tar -xf patchelf-*.tar.gz \
 && cp bin/patchelf /usr/local/bin \
 && cd .. \
 && rm -rf download-patchelf

ADD example example
ADD setup.py .
ADD README.rst .

RUN python3 -m build --wheel --outdir local-dist
RUN auditwheel repair --plat manylinux_2_17_aarch64 --strip local-dist/*.whl --wheel-dir dist
RUN twine check dist/*.whl
