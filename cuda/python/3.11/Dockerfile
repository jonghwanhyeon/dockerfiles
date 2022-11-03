ARG cuda
ARG ubuntu
FROM nvidia/cuda:${cuda}-cudnn8-devel-ubuntu${ubuntu}

LABEL maintainer="jonghwanhyeon93@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

ENV PYTHON_VERSION=3.11.0

ENV LANG=C.UTF-8
RUN sed --in-place "s/archive\.ubuntu\.com/mirror\.kakao\.com/g" /etc/apt/sources.list

# Refer to https://devguide.python.org/getting-started/setup-building/#linux
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
        build-essential \
        libbz2-dev \
        libffi-dev \
        libgdbm-compat-dev \
        libgdbm-dev \
        liblzma-dev \
        libncurses5-dev \
        libreadline6-dev \
        libsqlite3-dev \
        libssl-dev \
        pkg-config \
        tk-dev \
        uuid-dev \
        wget \
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
        --with-lto \
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
