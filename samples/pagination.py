"""Web Scraping Template."""

from playwright.sync_api import sync_playwright


def scrape():
    """Template function for web scraping."""
    data = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()
        page.goto("https://sandbox.oxylabs.io/products")

        # Wait for product cards to load
        page.locator(".product-card").first.wait_for(state="visible")

        pagination = page.locator(".pagination")

        if pagination.is_visible():
            page_links = page.locator(".pagination a").all()
            print(f"Total pages found: {len(page_links)}")

            next_button = page.locator("text=Forward").first

            if next_button.is_visible():
                print("Next button is visible. Clicking to go to the next page.")
                next_button.click()

                page.locator(".product-card").first.wait_for(state="visible")

                products = page.locator(".product-card").all()
                print(f"Total products found on the next page: {len(products)}")

        browser.close()

    return data
