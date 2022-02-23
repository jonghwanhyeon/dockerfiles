FROM jonghwanhyeon/cuda:11.2-python3.9

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

ARG uid=1000
ARG gid=$uid
ARG username=ml
ARG comment=jonghwanhyeon/ml

ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

RUN sed --in-place "s/archive\.ubuntu\.com/mirror\.kakao\.com/g" /etc/apt/sources.list

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
        sudo \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --system privileged \
    && groupadd --gid=$gid $username \
    && useradd --uid=$uid \
               --gid=$gid \
               --groups=privileged \
               --comment=$comment \
               --shell=/bin/bash \
               --create-home \
               $username \
    && echo %privileged ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/privileged \
    && chmod u=r,g=r,o= /etc/sudoers.d/privileged

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
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
        tensorflow \
        torch==1.10.2+cu111 \
        torchaudio==0.10.2+cu111 \
        torchvision==0.11.3+cu111 \
        tqdm

COPY /docker-init-user /usr/local/bin
RUN chmod u+s /usr/local/bin/docker-init-user

COPY docker-entrypoint.py /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.py"]