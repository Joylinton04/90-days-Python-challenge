# Day 17 of py challenge
# Build a simple HTTP request handler in Python to fetch and display the content of a webpage.

import requests
from bs4 import BeautifulSoup

url = input("Enter a URL (eg. https://example.com): ")

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html')
    print("\n\n")
    print(soup.prettify())
    print("\n\n")
except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        
    