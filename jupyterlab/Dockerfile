FROM hyeon0145/ml:latest

MAINTAINER Jonghwan Hyeon <hyeon0145@gmail.com>

RUN pip3 --no-cache-dir install \
    jupyter \
    jupyterlab

COPY jupyter_notebook_config.py /root/.jupyter/

VOLUME /notebooks
WORKDIR /notebooks

# Jupyter
EXPOSE 80
# Tensorboard
EXPOSE 6006

CMD jupyter lab
