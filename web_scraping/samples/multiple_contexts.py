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

        context1 = browser.new_context()
        context2 = browser.new_context()

        page1 = context1.new_page()
        page2 = context2.new_page()

        page1.goto("https://sandbox.oxylabs.io/products")
        page2.goto("https://sandbox.oxylabs.io/products")

        context1.add_cookies(
            [
                {
                    "name": "example_cookie",
                    "value": "value1",
                    "domain": "sandbox.oxylabs.io",
                    "path": "/",
                }
            ]
        )

        cookies1 = context1.cookies()
        cookies2 = context2.cookies()

        print(f"Cookies in context 1: {len(cookies1)}")
        print(f"Cookies in context 2: {len(cookies2)}")

        context1.close()
        context2.close()

        browser.close()

    return data


scrape()
