ARG cuda
ARG python
FROM ghcr.io/jonghwanhyeon/ml:base-cuda${cuda}-python${python}

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

RUN pip3 install --no-cache-dir \
        tensorflow