FROM jonghwanhyeon/cuda:11.2-python3.9

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

ENV LANG=C.UTF-8
ENV TZ=Asia/Seoul
ENV SHELL=/bin/bash

ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

RUN sed -i "s/archive\.ubuntu\.com/mirror\.kakao\.com/g" /etc/apt/sources.list

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
        curl \
        git \
        libgl1-mesa-glx \ 
        wget \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --upgrade \
        pip \
        setuptools \
        wheel

RUN pip3 install --no-cache-dir \
        altair \
        matplotlib \
        numpy \
        pandas \
        plotly \
        scikit-learn \
        scipy \
        seaborn \
        streamlit \
        tensorflow \
        tqdm

RUN pip3 install --no-cache-dir --find-links=https://download.pytorch.org/whl/torch_stable.html \
        torch==1.10.0+cu111 \
        torchvision==0.11.1+cu111 \
        torchaudio==0.10.0+cu111

RUN pip3 install \
        pytorch-lightning
