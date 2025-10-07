import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_nemlig_data():
    url = "https://www.nemlig.com/dagligvarer/nye-varer-inspiration/oekologi/frugt-og-gront"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return pd.DataFrame([{"Error": f"Failed to load page: {response.status_code}"}])

    soup = BeautifulSoup(response.text, "html.parser")
    products = []

    for item in soup.select(".product-list__item"):
        name_tag = item.select_one(".product-title")
        price_tag = item.select_one(".price-tag")

        name = name_tag.text.strip() if name_tag else "N/A"
        price = price_tag.text.strip() if price_tag else "N/A"

        products.append({
            "Product": name,
            "Price": price
        })

    if not products:
        return pd.DataFrame([{"Message": "No products found. Page structure may have changed."}])

    return pd.DataFrame(products)
