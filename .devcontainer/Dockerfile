# Use the official Python image
FROM mcr.microsoft.com/devcontainers/python:3.13

# Install dependencies
RUN apt-get update && apt-get install -y curl unzip

# Install uv globally (latest release from GitHub)
RUN curl -sSf https://astral.sh/uv/install.sh | bash && \
    ln -s /root/.cargo/bin/uv /usr/local/bin/uv


# Add uv to PATH
ENV PATH="/root/.cargo/bin:$PATH"

# Set working directory
WORKDIR /workspace

# Default shell
SHELL ["/bin/bash", "-c"]
