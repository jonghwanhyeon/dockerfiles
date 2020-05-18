FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

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
    tensorflow \
    torch \
    torchvision \
    tqdm


# To support static image export of plotly figures
RUN apt-get update && apt-get install -y \
    libasound2 \
    libgconf-2-4 \
    libgtk-3-0 \
    libnss3 \
    libxss1 \
    libxtst6 \
    xvfb \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install \
    psutil \
    requests

RUN curl \
    --location --output /tmp/orca-x86_64.AppImage \
    https://github.com/plotly/orca/releases/download/v1.3.1/orca-1.3.1.AppImage \
&& chmod +x /tmp/orca-x86_64.AppImage

WORKDIR /usr/local/share
RUN /tmp/orca-x86_64.AppImage --appimage-extract && mv squashfs-root orca
RUN rm /tmp/orca-x86_64.AppImage

WORKDIR /usr/local/bin
COPY orca /usr/local/bin/orca
RUN chmod +x /usr/local/bin/orca
