# web-scraping

Web scraping template with Playwright. Sample code is provided in the `samples` directory.

| Sample | Description |
|---|---|
| [*multiple_contexts.py*](https://github.com/bellanov/python-samples/tree/main/samples/multiple_contexts.py) | Example of using multiple contexts in web scraping. |
| [*pagination.py*](https://github.com/bellanov/python-samples/tree/main/samples/pagination.py) | Example of pagination / dynamic content in web scraping. |
| [*request_interception.py*](https://github.com/bellanov/python-samples/tree/main/samples/request_interception.py) | Example of request interception in web scraping to improve performance. |
| [*stable_access_management.py*](https://github.com/bellanov/python-samples/tree/main/samples/stable_access_management.py) | Example of managing stable access to web resources in web scraping (i.e., bypassing blocking mechanisms). |
| [*template.py*](https://github.com/bellanov/python-samples/tree/main/samples/template.py) | A simple *web scraping* template. |

## Requirements

To execute the sample scripts, ensure you have the following installed:

- Python 3.11 or higher
- [Playwright](https://playwright.dev/python/docs/intro) for Python.

## Script Execution

First, a local project environment needs to be created, then the project's dependencies need to be be installed.

1. Clone the repository.

   ```sh
   git clone https://github.com/bellanov/web-scraping.git
   cd web-scraping
   ```

2. Install Dependencies.

   ```sh
   # Install Dependencies
   scripts/install.sh
   scripts/playwright.sh
   ```

## Testing, Linting, and Formatting

Execute the tests to validate your installation.

```sh
# Execute Unit Tests
scripts/test.sh

# Lint / Format Codebase
scripts/lint.sh
scripts/format.sh
```

## Execute Sample Scripts

```sh
# Execute Sample Scripts
uv run samples/template.py
uv run samples/stable_access_management.py
uv run samples/request_interception.py
uv run samples/pagination.py
uv run samples/multiple_contexts.py
```