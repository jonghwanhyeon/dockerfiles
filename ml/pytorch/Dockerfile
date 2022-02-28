FROM jonghwanhyeon/cuda:11.3-python3.9

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

ENV LANG=C.UTF-8
ENV TZ=Asia/Seoul
ENV SHELL=/bin/bash

ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

RUN sed --in-place "s/archive\.ubuntu\.com/mirror\.kakao\.com/g" /etc/apt/sources.list
RUN echo "LANG=C.UTF-8" > /etc/default/locale

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

RUN pip3 install --no-cache-dir --find-links=https://download.pytorch.org/whl/torch_stable.html \
        matplotlib \
        numpy \
        pandas \
        plotly \
        pytorch-lightning \
        scikit-learn \
        scipy \
        seaborn \
        streamlit \
        torch==1.10.2+cu113 \
        torchaudio==0.10.2+cu113 \
        torchvision==0.11.3+cu113 \
        tqdm