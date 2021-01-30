FROM ghcr.io/jonghwanhyeon/ml:latest

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

RUN curl -fsSL https://code-server.dev/install.sh | sh

VOLUME /workspace
WORKDIR /workspace

# code-server
EXPOSE 8080

CMD code-server --bind-addr="0.0.0.0:8080" --disable-telemetry .
