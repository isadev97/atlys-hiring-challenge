from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from scraper import Scraper
from database import DatabaseManager
from cache import Cache
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
API_KEY = os.getenv('API_KEY')
api_key_header = APIKeyHeader(name='X-API-KEY')

cache = Cache()
db_manager = DatabaseManager('scraped_data.json')

def authenticate(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail='Forbidden')

@app.get('/scrape')
async def scrape_products(pages: int = 5, proxy: str = None, api_key: str = Depends(authenticate)):
    scraper = Scraper(pages, proxy, db_manager, cache)
    scraped_count = await scraper.scrape()
    print(f'Scraping completed. Total products scraped: {scraped_count}')
    return {'message': f'Scraping completed. Total products scraped: {scraped_count}'}
