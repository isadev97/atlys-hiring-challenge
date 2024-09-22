import json
from typing import List

DB_FILE = "scraped_data.json"

def save_products(products: List[dict]):
    try:
        with open(DB_FILE, 'w') as f:
            json.dump(products, f)
        print(f"Saved {len(products)} products to {DB_FILE}")
    except Exception as e:
        print(f"Error saving products: {e}")
