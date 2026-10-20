# web-scraping

Web scraping template.

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