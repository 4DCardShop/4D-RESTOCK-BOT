import requests
import time

URL = "https://www.pokemoncenter.com/category/collectibles/trading-cards"  # Update this URL as needed
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"  # Replace this with your Discord webhook

def check_restock():
    response = requests.get(URL)
    if "Sold Out" not in response.text:
        data = {
            "content": f"Restock Alert! Check: {URL}"
        }
        requests.post(WEBHOOK_URL, json=data)

if _name_ == "_main_":
    while True:
        check_restock()
        time.sleep(60)  # Check every 60 seconds
