FROM hyeon0145/jupyter:latest

LABEL maintainer="hyeon0145@gmail.com"

RUN pip3 --no-cache-dir install jupyterlab

# for JupyterLab extensions
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs && rm -rf /var/lib/apt/lists/*

COPY plugin.jupyterlab-settings /root/.jupyter/lab/user-settings/@jupyterlab/extensionmanager-extension/plugin.jupyterlab-settings

CMD jupyter lab
