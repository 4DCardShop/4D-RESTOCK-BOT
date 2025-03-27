import requests
import time
from bs4 import BeautifulSoup

URL = "https://www.pokemoncenter.com/category/new"
WEBHOOK_URL = "https://discord.com/api/webhooks/1354836336510501135/w3D94qWYD83iIpOUMaWKWwqChg8oWjdufWYq_pU_rwJ1_8647fUjfxL6OWX0GWrGR5_b"

seen_items = set()

def check_new_arrivals():
    global seen_items

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Grab all product links
    products = soup.find_all("a", class_="product-card__link")

    new_alerts = []

    for product in products:
        title = product.get("aria-label")
        link = "https://www.pokemoncenter.com" + product.get("href")

        if title and title not in seen_items:
            seen_items.add(title)
            new_alerts.append(f"**{title}**\n{link}")

    # Send Discord message if new products were found
    if new_alerts:
        message = "\n\n".join(new_alerts)
        payload = {"content": f"**New Pokémon Center Drops!**\n\n{message}"}
        requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    while True:
        check_new_arrivals()
        time.sleep(60)  # Check every 60 seconds
