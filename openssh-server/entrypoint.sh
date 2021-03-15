#!/bin/sh

if [ ! -n "$(find /etc/ssh -name 'ssh_host*')" ]; then
    echo "Regenerating keys..."
    DEBIAN_FRONTEND=noninteractive dpkg-reconfigure openssh-server
fi

echo "Starting openssh server..."
/usr/sbin/sshd -D
