FROM ubuntu:24.04

RUN apt update -y && apt upgrade -y

RUN apt install -y git curl sudo python3

RUN useradd -u 1092 -G sudo -s /bin/bash -m rtimpe

# userid on qgpu
USER 1092:1092

RUN curl -fsSL https://claude.ai/install.sh | bash

RUN echo export PATH="$HOME/.local/bin:$PATH" > "$HOME/.bashrc"
