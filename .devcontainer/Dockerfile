# Use the official Python image
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# Install the project into `/app`
WORKDIR /app
ADD . /app


# Install system packages:
# curl
RUN apt-get update && apt-get install -y curl

RUN apt-get update && apt-get install -y gnupg

# git
RUN apt-get update && apt-get install -y git
# duckdb
RUN curl -sL https://install.duckdb.org | sh
#11 1.139 Successfully installed DuckDB binary to /root/.duckdb/cli/1.3.2/duckdb
#11 1.140   with a link from                      /root/.duckdb/cli/latest/duckdb


# Install DuckDB CLI
RUN curl -sL https://install.duckdb.org | sh && \
    mkdir -p  /usr/local/bin && \
    cp /root/.duckdb/cli/latest/duckdb /usr/local/bin/duckdb && \
    chmod +x /usr/local/bin/duckdb

# github cli
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | \
    gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | \
    tee /etc/apt/sources.list.d/github-cli.list > /dev/null && \
    apt-get update && apt-get install -y gh



# Default shell
SHELL ["/bin/bash", "-c"]


# Create vscode user to satisfy Codespaces requirement
RUN useradd -m vscode
USER vscode
