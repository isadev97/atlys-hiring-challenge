import requests
from bs4 import BeautifulSoup
import time
from typing import List, Dict

class Scraper:
    def __init__(self, pages: int, proxy: str, db_manager, cache):
        self.pages = pages
        self.proxy = proxy
        self.db_manager = db_manager
        self.cache = cache

    async def scrape(self) -> int:
        scraped_products = 0
        for page in range(1, self.pages + 1):
            url = f'https://dentalstall.com/shop/page/{page}/'
            response = self.fetch_page(url)
            if response:
                products = self.parse_products(response)
                for product in products:
                    if self.cache.is_new_or_updated(product):
                        self.db_manager.save_product(product)
                        self.cache.store_product(product)
                        scraped_products += 1
            time.sleep(2)
        return scraped_products

    def fetch_page(self, url: str):
        for attempt in range(3):
            try:
                response = requests.get(url, proxies={'http': self.proxy, 'https': self.proxy} if self.proxy else None)
                response.raise_for_status()
                return response.text
            except requests.RequestException:
                time.sleep(5)
        return None

    def parse_products(self, html: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html, 'html.parser')
        products = []
        for item in soup.select('.product-item'):
            title = item.select_one('.product-title').get_text(strip=True)
            price = float(item.select_one('.product-price').get_text(strip=True).replace('$', ''))
            image_path = item.select_one('img')['src']
            products.append({
                'product_title': title,
                'product_price': price,
                'path_to_image': image_path,
            })
        return products
