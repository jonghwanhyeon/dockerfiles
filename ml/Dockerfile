FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

MAINTAINER Jonghwan Hyeon <hyeon0145@gmail.com>

ENV LANG=C.UTF-8

RUN sed -i "s/archive\.ubuntu/kr.archive.ubuntu/g" /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    curl \
    wget \
    git \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 --no-cache-dir install --upgrade pip

RUN pip3 --no-cache-dir install \
    numpy \
    scipy \
    torch \
    torchvision \
    tensorflow-gpu \
    keras \
    scikit-learn

ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
