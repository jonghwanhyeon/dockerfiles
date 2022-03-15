ARG CUDA_VERSION
FROM nvidia/cuda:${CUDA_VERSION}-cudnn8-devel-ubuntu20.04

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

ENV PYTHON_VERSION 3.9.10

ENV LANG=C.UTF-8
RUN sed --in-place "s/archive\.ubuntu\.com/mirror\.kakao\.com/g" /etc/apt/sources.list

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
        dpkg-dev \
        gcc \
        libbluetooth-dev \
        libbz2-dev \
        libc6-dev \
        libexpat1-dev \
        libffi-dev \
        libgdbm-compat-dev \
        libgdbm-dev \
        liblzma-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        make \
        tk-dev \
        uuid-dev \
        wget \
        xz-utils \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

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
        --with-system-expat \
        --with-system-ffi \
        --without-ensurepip \
    && make -j "$(nproc)" \
    && make install \
    && ldconfig \
    && rm -rf /usr/src/python

RUN cd /usr/local/bin \
    && ln -s idle3 idle \
    && ln -s pydoc3 pydoc \
    && ln -s python3 python \
    && ln -s python3-config python-config

RUN wget -O /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py" \
    && python /tmp/get-pip.py --no-cache-dir \
    && rm /tmp/get-pip.py
