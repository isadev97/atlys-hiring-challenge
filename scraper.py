import requests
from bs4 import BeautifulSoup
from models import Product
from time import sleep
from typing import List

PAGE_LIMIT = 3

class Scraper:
    def __init__(self, page_limit: int, proxy: str = None):
        self.page_limit = page_limit
        self.proxy = proxy
        self.base_url = "https://dentalstall.com/shop/page/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_catalogue(self) -> List[Product]:
        products = []
        for page_num in range(1, PAGE_LIMIT):
            try:
                url = f"{self.base_url}{page_num}/"  if page_num >=2 else f"https://dentalstall.com/shop/" 
                print(f"Scraping {url}")
                response = self.get_page_content(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                for item in soup.select(".product"):
                    name = item.select_one(".woo-loop-product__title").get_text(strip=True)
                    price = item.select_one(".amount").get_text(strip=True)
                    image_url = item.select_one(".mf-product-thumbnail").find("img")["data-lazy-src"]
                    products.append({
                        'product_title': name,
                        'product_price': price,
                        'path_to_image': image_url,
                    })
            except Exception as e:
                print(f"Error scraping page {page_num}: {e}. Retrying...")
                sleep(5)
        return products

    def get_page_content(self, url: str):
        proxies = {"http": self.proxy, "https": self.proxy} if self.proxy else None
        response = requests.get(url, headers=self.headers, proxies=proxies)
        if response.status_code != 200:
            print(f"Failed to retrieve {url}. Status code: {response.status_code}")
            raise Exception(f"Failed to retrieve {url}")
        return response

   