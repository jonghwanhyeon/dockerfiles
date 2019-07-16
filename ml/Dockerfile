FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

LABEL maintainer="hyeon0145@gmail.com"

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
    https://download.pytorch.org/whl/cu100/torch-1.1.0-cp36-cp36m-linux_x86_64.whl \
    https://download.pytorch.org/whl/cu100/torchvision-0.3.0-cp36-cp36m-linux_x86_64.whl \
    pytorch-ignite \
    tensorflow-gpu==2.0.0-beta1 \
    scikit-learn \
    pandas \
    matplotlib \
    seaborn \
    tqdm

ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
