from typing import Dict

class Cache:
    def __init__(self):
        self.products: Dict[str, Dict[str, float]] = {}

    def is_new_or_updated(self, product: Dict[str, str]) -> bool:
        key = product['product_title']
        if key not in self.products or self.products[key]['product_price'] != product['product_price']:
            self.products[key] = product
            return True
        return False

    def store_product(self, product: Dict[str, str]):
        self.products[product['product_title']] = product
