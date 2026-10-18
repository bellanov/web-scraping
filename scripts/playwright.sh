#!/bin/bash
#
# Install Playwright.

echo "Installing Playwright..."
uv run python -m playwright install --with-deps
