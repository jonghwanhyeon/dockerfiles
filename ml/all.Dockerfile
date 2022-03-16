ARG CUDA_VERSION
ARG PYTHON_VERSION
FROM ghcr.io/jonghwanhyeon/ml:base-cuda${CUDA_VERSION}-python${PYTHON_VERSION}

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

RUN pip3 install --no-cache-dir \
        tensorflow

ARG TORCH_VERSION
ARG TORCHVISION_VERSION
ARG TORCHAUDIO_VERSION

COPY install-torch.py /tmp/install-torch.py
RUN python3 /tmp/install-torch.py \
        --cuda=${CUDA_VERSION} \
        --python=${PYTHON_VERSION} \
        --torch=${TORCH_VERSION} \
        --torchaudio=${TORCHAUDIO_VERSION} \
        --torchvision=${TORCHVISION_VERSION} \
    && rm /tmp/install-torch.py