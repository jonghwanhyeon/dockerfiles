ARG tag
FROM ghcr.io/jonghwanhyeon/ml:${tag}

LABEL maintainer="jonghwanhyeon93@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

RUN pip install --no-cache-dir \
      ipywidgets \
      jupyterlab

COPY jupyter_lab_config.py /root/.jupyter/

RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
        nodejs \
    && rm -rf /var/lib/apt/lists/*

VOLUME /workspace
WORKDIR /workspace

EXPOSE 80
CMD jupyter-lab