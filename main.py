from config import Config
from services.openweather_api import fetch_weather
import time

while True:
    weather = fetch_weather()
    print(weather)
    # Zapis do excel / csv
    # Zapis do DB
    # Wykresy i interfejs
    time.sleep(60)

