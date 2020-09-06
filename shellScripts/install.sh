#!/bin/sh

# Here checking for root access
if [ "$(id -u)" -ne "0" ]
then
    echo "Requiers root access."
    exit 1
fi

apt-get install python3-gi python3-notify2 python3-bs4 python3-requests python3-setproctitle -y 