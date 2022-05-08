ARG cuda
ARG python
FROM ghcr.io/jonghwanhyeon/ml:cuda${cuda}-python${python}-base

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

RUN pip3 install --no-cache-dir \
        tensorflow

ARG cuda
ARG python
ARG torch
ARG torchvision
ARG torchaudio

COPY install-torch.py /tmp/install-torch.py
RUN python3 /tmp/install-torch.py \
        --cuda=${cuda} \
        --python=${python} \
        --torch=${torch} \
        --torchaudio=${torchaudio} \
        --torchvision=${torchvision} \
    && rm /tmp/install-torch.py
