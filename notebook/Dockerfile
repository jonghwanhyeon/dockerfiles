FROM keci/ml:latest

MAINTAINER Jonghwan Hyeon <hyeon0145@gmail.com>

RUN pip3 --no-cache-dir install \
    jupyter jupyter_contrib_nbextensions jupyter_nbextensions_configurator

RUN jupyter contrib nbextension install --system
RUN jupyter nbextensions_configurator enable --system
RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension

COPY jupyter_notebook_config.py /root/.jupyter/

VOLUME /notebooks
WORKDIR /notebooks

# Jupyter
EXPOSE 8888
# Tensorboard
EXPOSE 6006

# See: https://github.com/ipython/ipython/issues/7062
# CMD ["jupyter", "notebook"]

COPY run-jupyter-notebook.sh /
CMD ["/run-jupyter-notebook.sh"]
