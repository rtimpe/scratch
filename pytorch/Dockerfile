FROM ubuntu:24.04

RUN apt update -y && apt upgrade -y

RUN apt install -y git curl sudo python3 build-essential

RUN useradd -u 1092 -G sudo -s /bin/bash -m rtimpe

# userid on qgpu
USER 1092:1092

RUN curl -fsSL https://claude.ai/install.sh | bash

RUN curl -fsSL https://pixi.sh/install.sh | sh

# add claude and pixi to path
RUN echo export PATH="$HOME/.local/bin:$HOME/.pixi/bin:$PATH" > "$HOME/.bashrc"
