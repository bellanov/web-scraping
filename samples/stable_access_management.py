"""Stable Access Management Example.

This example demonstrates how to manage stable access to web resources using Playwright. This
enables you to bypass blocking mechanisms and maintain consistent access to web content.
"""

from playwright.sync_api import sync_playwright


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
