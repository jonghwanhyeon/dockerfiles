FROM jonghwanhyeon/cuda:10.1-python3

LABEL maintainer="hyeon0145@gmail.com"

ENV LANG=C.UTF-8
ENV SHELL=/bin/bash

ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

RUN sed -i "s/archive\.ubuntu\.com/mirror\.kakao\.com/g" /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
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
        "numpy<1.19.0" \
        pandas \
        plotly \
        scikit-learn \
        "scipy==1.4.1" \
        seaborn \
        tensorflow \
        tqdm

RUN pip3 install --no-cache-dir --find-links=https://download.pytorch.org/whl/torch_stable.html \
        torch==1.6.0+cu101 \
        torchvision==0.7.0+cu101

RUN pip3 install \
        pytorch-ignite
