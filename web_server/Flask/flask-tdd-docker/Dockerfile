# pull official base image
FROM python:3.12-slim-trixie

# Copy uv from the official uv Docker image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-traditional && \
    rm -rf /var/lib/apt/lists/*

# set working directory
WORKDIR /usr/src/app

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr 
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/usr/src/app/
# Use system Python environment in Docker
ENV UV_SYSTEM_PYTHON=1
# Compile bytecode for faster startup
ENV UV_COMPILE_BYTECODE=1
# Cache uv data in Docker layer
ENV UV_CACHE_DIR=/root/.cache/uv

# install dependencies
COPY pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install -r pyproject.toml

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . .

