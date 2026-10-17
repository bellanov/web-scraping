#
# Execute unit tests.

echo "Executing Unit Tests..."
uv run coverage run -m pytest tests/

echo "Generating Report..."
uv run coverage report -m

echo "Build HTML Report..."
uv run coverage html
