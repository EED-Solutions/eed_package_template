# Use the official Python image
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# Install the project into `/app`
WORKDIR /app
ADD . /app


# Install system packages:
# git
RUN apt-get update && apt-get install -y git
# duckdb
RUN curl -sL https://install.duckdb.org | sh


# Default shell
SHELL ["/bin/bash", "-c"]


# Create vscode user to satisfy Codespaces requirement
RUN useradd -m vscode
USER vscode
