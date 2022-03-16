ARG cuda
ARG python
FROM ghcr.io/jonghwanhyeon/ml:base-cuda${cuda}-python${python}

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

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