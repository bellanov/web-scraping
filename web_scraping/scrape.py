"""Web Scraping with Playwright."""

from playwright.sync_api import sync_playwright


def scrape():
    """Template function for web scraping."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://sandbox.oxylabs.io/products")
        content = page.content()
        print(content)
        browser.close()


if __name__ == "__main__":
    scrape()
