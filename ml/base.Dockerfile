ARG cuda
ARG python
FROM ghcr.io/jonghwanhyeon/cuda:${cuda}-python${python}

LABEL maintainer="jonghwanhyeon93@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

ENV LANG=C.UTF-8
ENV TZ=Asia/Seoul
ENV SHELL=/bin/bash

ENV LD_LIBRARY_PATH=/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

RUN sed --in-place "s/archive\.ubuntu\.com/mirror\.kakao\.com/g" /etc/apt/sources.list
RUN echo "LANG=C.UTF-8" > /etc/default/locale

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
        curl \
        git \
        libgl1-mesa-glx \
        wget \
    && rm -rf /var/lib/apt/lists/*

RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash \
    && apt-get install --yes --no-install-recommends git-lfs \
    && git lfs install \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
        datasets \
        matplotlib \
        numpy \
        pandas \
        plotly \
        pyarrow \
        rich \
        scikit-learn \
        scipy \
        seaborn \
        tqdm \
        transformers \
        wandb