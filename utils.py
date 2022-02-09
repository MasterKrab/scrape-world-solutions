import requests
from bs4 import BeautifulSoup
from config import BASE_URL


def get_soup(route):
    response = requests.get(f"{BASE_URL}{route}")
    return BeautifulSoup(response.text, "html.parser")
