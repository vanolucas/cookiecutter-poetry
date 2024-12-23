#!/usr/bin/env bash

# Usage: ./run-cookiecutter.sh

# Run the project generation assistant.
python3 -m pipx run cookiecutter . &&

# Find the generated project directory by getting the most recent directory.
PROJ_DIR=$(ls -td ./*/ | head -1) &&

# Copy the generated project to the output directory.
cp -r $PROJ_DIR /output/
