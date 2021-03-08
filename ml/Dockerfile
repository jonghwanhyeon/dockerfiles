FROM ghcr.io/jonghwanhyeon/cuda:11.0-python3.8

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

ENV LANG=C.UTF-8
ENV SHELL=/bin/bash

ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

RUN sed -i "s/archive\.ubuntu\.com/mirror\.kakao\.com/g" /etc/apt/sources.list

RUN apt-get update && apt-get install --yes --no-install-recommends \
        curl \
        git \
        wget \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --upgrade \
        pip \
        setuptools \
        wheel

RUN pip3 install --no-cache-dir \
        kaleido \
        matplotlib \
        numpy \
        pandas \
        plotly \
        scikit-learn \
        scipy \
        seaborn \
        tensorflow \
        tqdm

RUN pip3 install --no-cache-dir --find-links=https://download.pytorch.org/whl/torch_stable.html \
        torch==1.7.1+cu110 \
        torchvision==0.8.2+cu110 \
        torchaudio==0.7.2

RUN pip3 install \
        pytorch-ignite \
        pytorch-lightning
