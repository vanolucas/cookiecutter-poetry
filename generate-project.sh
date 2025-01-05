#!/usr/bin/env bash

# Usage: ./generate-project.sh <target_dir>

# Set the target directory inside which the new project directory will be created.
TARGET_DIR=$1

# Name of the Docker image to create.
IMAGE_NAME=cookiecutter-poetry

# Get current user and group IDs.
UID=$(id -u)
GID=$(id -g)

# Build the project generation tool's Docker image.
docker build --build-arg UID=$UID --build-arg GID=$GID --tag $IMAGE_NAME . &&

# Launch the cookiecutter project generation script in a Docker container.
docker run -it --rm \
    -v $TARGET_DIR:/output \
    --name $IMAGE_NAME \
    $IMAGE_NAME &&

# Navigate to the target directory where the project got created.
cd $TARGET_DIR
