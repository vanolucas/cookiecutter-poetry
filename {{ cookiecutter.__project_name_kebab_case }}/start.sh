#!/usr/bin/env bash

# Usage: ./start.sh <service_name> <env_name>

# The Docker Compose service to start. Typically app or api.
SERVICE=$1

# The environment name of the Docker Compose file to use. Typically dev or prod.
ENV_NAME=$2

# Build and start the service using Docker Compose.
docker compose -f docker-compose.yml -f docker-compose."$ENV_NAME".yml up -d --build -- "$SERVICE" &&

echo "Started $SERVICE ($ENV_NAME)."
