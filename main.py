import requests
import time
from bs4 import BeautifulSoup

URL = "https://www.pokemoncenter.com/category/new"
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_HERE"

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

        target_keywords = [
            "Pokémon TCG: Scarlet & Violet—Destined Rivals Pokémon Center Elite Trainer Box",
            "Pokémon TCG: Scarlet & Violet—Prismatic Evolutions Super-Premium Collection"
        ]

        if title and title not in seen_items:
            for keyword in target_keywords:
                if keyword.lower() in title.lower():
                    seen_items.add(title)
                    new_alerts.append(f"**{title}**\n{link}")
                    break

    # Send Discord message if new products were found
    if new_alerts:
        message = "\n\n".join(new_alerts)
        payload = {"content": f"**New Pokémon Center Drop Detected!**\n\n{message}"}
        requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    while True:
        check_new_arrivals()
        time.sleep(60)  # Check every 60 seconds
