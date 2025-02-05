FROM python:3.8-slim

RUN apt-get update && apt-get install -y openssh-client\
    python3-pip

COPY . .

RUN ssh-keygen -t ed25519 -f /root/.ssh/id_ed25519 -q -N ""

