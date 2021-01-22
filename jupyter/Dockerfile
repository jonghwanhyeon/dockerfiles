FROM ghcr.io/jonghwanhyeon/ml:latest

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

RUN pip3 install --no-cache-dir jupyter

COPY jupyter_notebook_config.py /root/.jupyter/

VOLUME /workspace
WORKDIR /workspace

# Jupyter
EXPOSE 80
# Tensorboard
EXPOSE 6006

CMD jupyter notebook
