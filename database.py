import json
from typing import List, Dict

class DatabaseManager:
    def __init__(self, filename: str):
        self.filename = filename

    def load_products(self) -> List[Dict[str, str]]:
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_product(self, product: Dict[str, str]):
        products = self.load_products()
        products.append(product)
        with open(self.filename, 'w') as file:
            json.dump(products, file)
