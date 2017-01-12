FROM keci/ml:latest

MAINTAINER Jonghwan Hyeon <hyeon0145@gmail.com>

RUN pip3 --no-cache-dir install \
    jupyter

COPY jupyter_notebook_config.py /root/.jupyter/

VOLUME /notebooks
WORKDIR /notebooks

EXPOSE 8888

# See: https://github.com/ipython/ipython/issues/7062
# CMD ["jupyter", "notebook"]

COPY run-jupyter-notebook.sh /
CMD ["/run-jupyter-notebook.sh"]
