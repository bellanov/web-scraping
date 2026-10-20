"""Request Interception Example.

This example demonstrates how to intercept network requests and modify their behavior using Playwright. This
enables you to block images, stylesheets, and other unnecessary resources, which can speed up your scraping
process and reduce bandwidth usage.
"""

from playwright.sync_api import sync_playwright


def block_resources(route, request):
    """Block unnecessary resources like images and stylesheets."""

    if request.resource_type in ["image", "stylesheet", "font", "media"]:
        route.abort()
    else:
        route.continue_()


def scrape():
    """Template function for web scraping."""
    data = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.route("**/*", block_resources)

        page.goto("https://sandbox.oxylabs.io/products")

        # Wait for product cards to load
        products = page.locator(".product-card").all()
        print(f"Total products found: {len(products)}")

        browser.close()

    return data
