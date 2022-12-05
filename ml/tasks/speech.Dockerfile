ARG tag
FROM ghcr.io/jonghwanhyeon/ml:${tag}

LABEL maintainer="jonghwanhyeon93@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"


RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
        cmake \
        ffmpeg \
        flac \
        libsndfile1-dev \
        sox \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir \
        Cython

RUN pip3 install --no-cache-dir \
        datasets \
        g2pk \
        librosa \
        soundfile \
        transformers

VOLUME /workspace
WORKDIR /workspace

RUN git clone --depth=1 https://github.com/espnet/espnet \
    && cd espnet/tools \
    && ./setup_python.sh $(command -v python3) \
    && make \
    && cd ../..

RUN git clone --depth=1 https://github.com/NVIDIA/NeMo \
    && cd NeMo \
    && pip3 install --editable .[all]
