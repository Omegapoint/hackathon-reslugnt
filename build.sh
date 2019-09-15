#!/usr/bin/env bash

set -eou pipefail

readonly PREFIX="reslugnt"
readonly BUILD_IMAGE="${PREFIX}-build-image"
readonly BUILD_CONTAINER="${PREFIX}-build-container"

docker build -t "${BUILD_IMAGE}" .
docker run --rm -it "${BUILD_IMAGE}" sh

#docker create --name "${BUILD_CONTAINER}" "${BUILD_IMAGE}"
#docker cp "${BUILD_CONTAINER}":/src/build ./build

