ARG cuda
ARG python
FROM ghcr.io/jonghwanhyeon/ml:cuda${cuda}-python${python}-base

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

ARG tensorflow

RUN pip3 install --no-cache-dir \
        "tensorflow==${tensorflow}"
