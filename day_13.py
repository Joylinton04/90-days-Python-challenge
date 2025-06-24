# Day 13 of py challenge
# Create a Python script that fetches data from a public API (e.g., OpenWeatherMap) and displays the
# weather.

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

try:
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=new york&appid={API_KEY}")
    response.raise_for_status()  # Raises HTTPError if the response has a bad status
    data = response.json()       # Convert JSON string to Python dictionary
    print(data)
    print("\nWeather condition")
    print(data['weather'][0]['main'])
    print(data['weather'][0]['description'])
except (requests.exceptions.HTTPError, ValueError, TypeError) as err:
    print(f"An error occurred: {err}")
