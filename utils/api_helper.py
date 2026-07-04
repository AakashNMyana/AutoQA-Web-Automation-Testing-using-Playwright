import requests
from config.config import API_URL


def get_products_count():
    response = requests.get(API_URL)
    return len(response.json()["products"])