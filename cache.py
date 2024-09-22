import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def cache_product(product: dict) -> bool:
    product_title = product.get('product_title')
    product_price = product.get('product_price')

    if product_title is None or product_price is None:
        return False

    cache_key = f"product:{product_title}"
    cached_price = r.get(cache_key)

    if cached_price is not None:
        cached_price = cached_price.decode('utf-8')

    if cached_price and cached_price == str(product_price):
        return True

    r.set(cache_key, str(product_price))
    return False
