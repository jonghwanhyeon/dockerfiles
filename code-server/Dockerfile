FROM jonghwanhyeon/ml:latest

LABEL maintainer="hyeon0145@gmail.com"

RUN curl -fsSL https://code-server.dev/install.sh | sh

VOLUME /workspace
WORKDIR /workspace

# code-server
EXPOSE 8080

CMD code-server --bind-addr="0.0.0.0:8080" .
