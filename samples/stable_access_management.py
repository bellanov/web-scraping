"""Stable Access Management Example.

This example demonstrates how to manage stable access to web resources using Playwright. This
enables you to bypass blocking mechanisms and maintain consistent access to web content.
"""

from playwright.sync_api import sync_playwright


def scrape():
    """Template function for web scraping."""
    data = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
            # Enable proxy settings if needed for large-scale scraping or to bypass geo-restrictions.
            # proxy={"server": "http://your-proxy-server:port", "username": "your-username", "password": "your-password"}
        )

        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
            locale="en-US",
            timezone_id="America/New_York",
            geolocation={"latitude": 40.7128, "longitude": -74.0060},
            permissions=["geolocation"]
        )

        page = context.new_page()

        page.set_extra_http_headers({
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Set-Fetch-Dest": "document",
            "Set-Fetch-Mode": "navigate",
            "Set-Fetch-Site": "none",
            "Set-Fetch-User": "?1",
            "Cache-Control": "max-age=0",
        })

        page.goto("https://sandbox.oxylabs.io/products")

        # Wait for product cards to load
        page.wait_for_selector(".product-card")
        products = page.query_selector_all(".product-card")

        print("=" * 50)
        print("Extracted Products")
        print("=" * 50)

        for product in products:
            name_element = product.query_selector(".title")
            name = name_element.inner_text() if name_element else "-"

            price_element = product.query_selector(".price-wrapper")
            price = price_element.inner_text() if price_element else "-"

            print(f"Product: {name}, Price: {price}")
            print("-" * 80)

            data[name] = {"price": price}
        

        context.close()
        browser.close()

    return data
