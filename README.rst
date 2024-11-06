An example package for building C/C++ extensions for multiple OSes and architectures

It supports C, C++ and OpenMP code.

It's able to build the following binary wheels on GitHub Actions:

- example-1.0-cp38-cp38-macosx_12_0_x86_64.whl
- example-1.0-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
- example-1.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_31_x86_64.whl
- example-1.0-cp38-cp38-win_amd64.whl
- example-1.0-cp39-cp39-macosx_12_0_x86_64.whl
- example-1.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
- example-1.0-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_31_x86_64.whl
- example-1.0-cp39-cp39-win_amd64.whl
- example-1.0-cp310-cp310-macosx_12_0_x86_64.whl
- example-1.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
- example-1.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_31_x86_64.whl
- example-1.0-cp310-cp310-win_amd64.whl
- example-1.0-cp311-cp311-macosx_12_0_universal2.whl
- example-1.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
- example-1.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_31_x86_64.whl
- example-1.0-cp311-cp311-win_amd64.whl
- example-1.0-cp312-cp312-macosx_12_0_universal2.whl
- example-1.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
- example-1.0-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_31_x86_64.whl
- example-1.0-cp312-cp312-win_amd64.whl
- example-1.0-cp313-cp313-macosx_12_0_universal2.whl
- example-1.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
- example-1.0-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_31_x86_64.whl
- example-1.0-cp313-cp313-win_amd64.whl

Note that for recent versions of Python on macOS, it produces *universal2* wheels, that run on x86_64 and arm64 (M1, *etc.*).

For arm64 on Linux, while waiting for [GitHub-hosted arm64 runners](https://github.com/orgs/community/discussions/19197), it uses Qemu and Docker Buildx on x86 runners.
This is an order of magnitude slower than native arm64 runners, but it works.
