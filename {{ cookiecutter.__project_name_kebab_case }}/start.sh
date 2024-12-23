#!/usr/bin/env bash

# Usage: ./start.sh <env_name>

ENV_NAME=$1

docker compose -f docker-compose.yml -f docker-compose."$ENV_NAME".yml up -d --build -- api
