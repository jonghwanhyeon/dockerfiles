FROM debian:buster-slim

LABEL maintainer="jonghwanhyeon93@gmail.com" \
      org.opencontainers.image.source="https://github.com/jonghwanhyeon/dockerfiles"

ENV LANG=C.UTF-8

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
        openssh-server \
    && rm -rf /var/lib/apt/lists/*

# Remove generated host keys
RUN rm /etc/ssh/ssh_host_*

RUN mkdir -p /run/sshd && chmod u=rwx,g=rx,o=rx /run/sshd

COPY entrypoint.sh /entrypoint.sh
RUN chmod u+x /entrypoint.sh

EXPOSE 22
ENTRYPOINT /entrypoint.sh
