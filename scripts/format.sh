#!/bin/bash
#
# Format Code Base.

echo "Formatting imports..."
uv run isort samples
uv run isort tests

echo "Formatting code base..."
uv run black samples 
uv run black tests
