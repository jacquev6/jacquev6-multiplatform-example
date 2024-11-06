#!/bin/bash

set -o errexit
set -x


docker_platforms="linux/amd64 linux/arm64"
python_versions="3.13"

# Run beforhand: docker buildx create --name multiplatform --platform linux/amd64,linux/arm64

rm -rf dist
for docker_platform in $docker_platforms
do
  for python_version in $python_versions
  do
    # Build
    docker buildx build --builder multiplatform --build-arg PYTHON_VERSION=$python_version --platform $docker_platform . --load
    image=$(docker buildx build --builder multiplatform --build-arg PYTHON_VERSION=$python_version --platform $docker_platform . --load --quiet)

    # Extract from Docker image
    container=$(docker create --platform $docker_platform $image)
    docker cp $container:/wd/dist .
    docker rm $container
  done
done

for docker_platform in $docker_platforms
do
  for python_version in $python_versions
  do
    # Check
    docker buildx build --builder multiplatform --build-arg PYTHON_VERSION=$python_version --platform $docker_platform --load . --file Dockerfile.check
    image=$(docker buildx build --builder multiplatform --build-arg PYTHON_VERSION=$python_version --platform $docker_platform --load . --file Dockerfile.check --quiet)
    container=$(docker create --platform $docker_platform $image)
    docker cp $container:/output.txt - | tar --extract --to-stdout
    docker rm $container
  done
done

echo
find dist -type f
