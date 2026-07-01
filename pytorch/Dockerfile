# build with `docker build . -t rtimpe-claude`
# see https://gitlab.com/nvidia/container-images/cuda/blob/master/doc/supported-tags.md for more tags
FROM nvidia/cuda:13.1.2-cudnn-runtime-ubuntu24.04

RUN apt update -y && apt upgrade -y

RUN apt install -y git curl sudo python3 build-essential

RUN groupadd rtimpe --gid 1097 && useradd -u 1092 -g 1097 -G sudo -s /bin/bash -m rtimpe

# userid on qgpu
USER 1092

RUN curl -fsSL https://claude.ai/install.sh | bash

RUN curl -fsSL https://pixi.sh/install.sh | sh

# add claude and pixi to path
RUN echo export PATH="$HOME/.local/bin:$HOME/.pixi/bin:$PATH" > "$HOME/.bashrc"

# install uv, mostly for convenience with the `skills` repo
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
