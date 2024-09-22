from fastapi import FastAPI, Depends, HTTPException
from scraper import Scraper
from config import get_settings, Settings
from models import Product
from database import save_products
from cache import cache_product
from typing import List

app = FastAPI()

# Authentication dependency
def authenticate(api_key: str = Depends(get_settings)):
    if api_key.API_KEY != Settings().API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

@app.get("/api/scrape", response_model=List[Product])
async def scrape_products(
    page_limit: int = 5, 
    proxy: str = None, 
    api_key: str = Depends(authenticate)
):
    scraper = Scraper(page_limit, proxy)
    products = scraper.scrape_catalogue()
    
    for product in products:
        cached = cache_product(product)
        if not cached:
            save_products(products)
    
    return products
