import requests
import time

URL = "https://www.pokemoncenter.com/category/collectibles/trading-cards"  # Update this URL as needed
WEBHOOK_URL = "https://discord.com/api/webhooks/1354836336510501135/w3D94qWYD83iIpOUMaWKWwqChg8oWjdufWYq_pU_rwJ1_8647fUjfxL6OWX0GWrGR5_b"  # Replace this with your Discord webhook

def check_restock():
    response = requests.get(URL)
    if "Sold Out" not in response.text:
        data = {
            "content": f"Restock Alert! Check: {URL}"
        }
        requests.post(WEBHOOK_URL, json=data)

if __name__ == "__main__":
    while True:
        check_restock()
        time.sleep(60)  # Check every 60 seconds
