ARG tag
FROM ghcr.io/jonghwanhyeon/ml:${tag}

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

RUN pip3 install --no-cache-dir jupyterlab
COPY jupyter_lab_config.py /root/.jupyter/

VOLUME /workspace
WORKDIR /workspace

EXPOSE 80
CMD jupyter-lab