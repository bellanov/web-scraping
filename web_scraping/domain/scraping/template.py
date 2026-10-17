"""Web Scraping with Playwright."""

from playwright.sync_api import sync_playwright


def scrape():
    """Template function for web scraping."""
    data = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://sandbox.oxylabs.io/products")

        data["title"] = page.title()
        data["content"] = page.content()

        print(f"Page Title: {data['title']}")
        browser.close()
    return data


if __name__ == "__main__":
    scrape()
