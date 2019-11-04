FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

LABEL maintainer="hyeon0145@gmail.com"

ENV LANG=C.UTF-8
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

RUN sed -i "s/archive\.ubuntu\.com/mirror\.kakao\.com/g" /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
    curl \
    git \
    python3-dev \
    python3-pip \
    wget \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip setuptools wheel

RUN pip3 install \
    matplotlib \
    numpy \
    pandas \
    plotly \
    pytorch-ignite \
    scikit-learn \
    scipy \
    seaborn \
    tensorflow-gpu \
    torch \
    torchvision \
    tqdm
