FROM hyeon0145/ml:latest

MAINTAINER Jonghwan Hyeon <hyeon0145@gmail.com>

RUN pip3 --no-cache-dir install \
    jupyter \
    jupyterlab

RUN jupyter serverextension enable --py jupyterlab --sys-prefix

COPY jupyter_notebook_config.py /root/.jupyter/

VOLUME /notebooks
WORKDIR /notebooks

# Jupyter
EXPOSE 8888
# Tensorboard
EXPOSE 6006

CMD jupyter lab
