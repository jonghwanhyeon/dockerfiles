FROM jonghwanhyeon/cuda:10.1-python3

LABEL maintainer="hyeon0145@gmail.com"

ENV LANG=C.UTF-8
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

RUN sed -i "s/archive\.ubuntu\.com/mirror\.kakao\.com/g" /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
    curl \
    git \
    wget \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip setuptools wheel

RUN pip3 install \
    bokeh \
    matplotlib \
    numpy \
    pandas \
    plotly \
    scikit-learn \
    scipy \
    seaborn \
    tensorflow \
    tqdm

RUN pip3 install \
    --find-links=https://download.pytorch.org/whl/torch_stable.html \
    torch==1.5.1+cu101 \
    torchvision==0.6.1+cu101

RUN pip3 install pytorch-ignite
