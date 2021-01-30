FROM ghcr.io/jonghwanhyeon/ml:latest

LABEL maintainer="hyeon0145@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

RUN curl -fsSL https://code-server.dev/install.sh | sh

# Fix Python extension
RUN mkdir -p ~/.local/share/code-server/User \
    && echo "{\"extensions.autoCheckUpdates\": false," \
             "\"extensions.autoUpdate\": false}" > ~/.local/share/code-server/User/settings.json \
    && wget --quiet https://github.com/microsoft/vscode-python/releases/download/2020.10.332292344/ms-python-release.vsix \
    && code-server --install-extension ms-python-release.vsix || true \
    && rm ms-python-release.vsix \
    && rm ~/.config/code-server/config.yaml # Reset password

VOLUME /workspace
WORKDIR /workspace

# code-server
EXPOSE 8080

CMD code-server --bind-addr="0.0.0.0:8080" --disable-telemetry .
