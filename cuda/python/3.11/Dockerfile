ARG cuda
ARG cudnn
ARG ubuntu
FROM jonghwanhyeon/python:build-deps-ubuntu${ubuntu} AS builder

ENV LANG=C.UTF-8
ENV PYTHON_VERSION=3.11.11

RUN wget -O /tmp/python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" \
    && mkdir -p /usr/src/python \
    && tar -xJC /usr/src/python --strip-components=1 -f /tmp/python.tar.xz \
    && rm /tmp/python.tar.xz

RUN cd /usr/src/python \
    && ./configure \
        --build="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
        --enable-loadable-sqlite-extensions \
        --enable-optimizations \
        --enable-option-checking=fatal \
        --enable-shared \
        --with-lto \
        --with-ensurepip \
    && make -j "$(nproc)" \
    && make install \
    && rm -rf /usr/src/python


FROM nvidia/cuda:${cuda}-cudnn${cudnn}-devel-ubuntu${ubuntu}

LABEL maintainer="jonghwanhyeon93@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

ENV LANG=C.UTF-8
RUN sed --in-place "s/archive\.ubuntu\.com/mirror\.kakao\.com/g" /etc/apt/sources.list

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
        build-essential \
        ca-certificates \
        gdb \
        lcov \
        pkg-config \
        wget \
    && rm -rf /var/lib/apt/lists/*

# Refer to https://devguide.python.org/getting-started/setup-building/#install-dependencies
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
        libbz2-dev \
        libffi-dev \
        libgdbm-compat-dev \
        libgdbm-dev \
        liblzma-dev \
        libncurses5-dev \
        libreadline6-dev \
        libsqlite3-dev \
        libssl-dev \
        tk-dev \
        uuid-dev \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/include /usr/local/include
COPY --from=builder /usr/local/lib /usr/local/lib
RUN ldconfig

RUN cd /usr/local/bin \
    && ln -s idle3 idle \
    && ln -s pip3 pip \
    && ln -s pydoc3 pydoc \
    && ln -s python3 python \
    && ln -s python3-config python-config