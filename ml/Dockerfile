FROM nvidia/cuda:8.0-cudnn5-devel

MAINTAINER Jonghwan Hyeon <hyeon0145@gmail.com>

RUN apt-get update && apt-get install -y \
    git \
    curl \
    libzmq3-dev \
    python3-dev \
&& rm -rf /var/lib/apt/lists/*

RUN curl  https://bootstrap.pypa.io/get-pip.py | python3

RUN pip3 --no-cache-dir install \
    numpy \
    scipy \
    tensorflow-gpu \
    Theano \
    sklearn \
    keras \
    matplotlib
