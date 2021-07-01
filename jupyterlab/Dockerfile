FROM ghcr.io/jonghwanhyeon/jupyter:latest

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

RUN pip3 install --no-cache-dir jupyterlab

# for JupyterLab extensions
RUN curl -sL https://deb.nodesource.com/setup_lts.x | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
        nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build

RUN jupyter labextension install jupyterlab-plotly --no-build
RUN jupyter labextension install plotlywidget --no-build

RUN NODE_OPTIONS=--max-old-space-size=4096 jupyter lab build

COPY plugin.jupyterlab-settings /root/.jupyter/lab/user-settings/@jupyterlab/extensionmanager-extension/plugin.jupyterlab-settings

CMD jupyter lab
