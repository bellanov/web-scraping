#!/bin/bash
#
# Format Code Base.

echo "Formatting imports..."
uv run isort web_scraping
uv run isort tests

echo "Formatting code base..."
uv run black web_scraping 
uv run black tests
