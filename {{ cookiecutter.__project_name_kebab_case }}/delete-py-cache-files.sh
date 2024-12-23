#!/usr/bin/env bash

# Usage: ./delete-py-cache-files.sh

# Find and delete all Python, PyTest, MyPY and Ruff cache files from this directory (recursively).
find . | grep -E "(/__pycache__$|\.mypy_cache$|\.pytest_cache$|\.ruff_cache$|\.pyc$|\.pyo$)" | xargs rm -rf
