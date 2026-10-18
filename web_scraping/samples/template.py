"""Web Scraper."""

from playwright.sync_api import sync_playwright


def scrape():
    """Template function for web scraping."""
    data = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()
        page.goto("https://sandbox.oxylabs.io/products")

        page.wait_for_selector(".product-card")  # Wait for product cards to load
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

        print("\n" + "=" * 50)
        print("Using playwright locators")
        print("-" * 50)

        all_links = page.get_by_role("link").all()
        print(f"Total links found: {len(all_links)}")

        heading = page.get_by_text("Products").first
        print(f"Heading text: {heading.inner_text()}")

        browser.close()

    return data


if __name__ == "__main__":
    scrape()
