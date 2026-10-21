"""Data Cleaning and Export Example."""

import json

import pandas as pd
from playwright.sync_api import sync_playwright


def export_to_json(data, filename: str):
    """Export scraped data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def export_to_csv(data, filename: str):
    """Export scraped data to a CSV file."""
    df = pd.DataFrame.from_dict(data, orient="index").rename_axis("name").reset_index()
    df.to_csv(filename, index=False)


def scrape():
    """Template function for web scraping."""
    data = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()
        page.goto("https://sandbox.oxylabs.io/products")

        # Wait for product cards to load
        page.wait_for_selector(".product-card")
        products = page.query_selector_all(".product-card")

        for product in products:
            name_element = product.query_selector(".title")
            name = name_element.inner_text() if name_element else "-"

            price_element = product.query_selector(".price-wrapper")
            price = price_element.inner_text() if price_element else "-"

            print(f"Product: {name}, Price: {price}")
            print("-" * 80)

            data[name] = {"price": price}

        export_to_json(data, "products.json")
        export_to_csv(data, "products.csv")

        browser.close()

    return data


if __name__ == "__main__":
    scrape()
