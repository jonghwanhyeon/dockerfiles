ARG cuda
ARG python
FROM ghcr.io/jonghwanhyeon/ml:cuda${cuda}-python${python}-base

LABEL maintainer="jonghwanhyeon93@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

ARG cuda
ARG python
ARG torch
ARG torchvision
ARG torchaudio
ARG torchtext

COPY install-torch.py /tmp/install-torch.py
RUN python3 /tmp/install-torch.py \
        --cuda=${cuda} \
        --torch=${torch} \
        --torchaudio=${torchaudio} \
        --torchvision=${torchvision} \
        --torchtext=${torchtext} \
    && rm /tmp/install-torch.py

RUN pip3 install --no-cache-dir \
        "transformers[torch]"