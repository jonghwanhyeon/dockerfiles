FROM hyeon0145/ml:latest

MAINTAINER Jonghwan Hyeon <hyeon0145@gmail.com>

RUN pip3 --no-cache-dir install \
    jupyter \
    jupyterlab

# Install Jupyter Widgets
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt install -y nodejs && rm -rf /var/lib/apt/lists/*
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager

COPY jupyter_notebook_config.py /root/.jupyter/

VOLUME /notebooks
WORKDIR /notebooks

# Jupyter
EXPOSE 80
# Tensorboard
EXPOSE 6006

CMD jupyter lab
