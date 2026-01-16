from config import Config
import requests
from datetime import datetime

URL = f"https://api.openweathermap.org/data/2.5/weather?q={Config.OPENWEATHER_CITY}&appid={Config.OPENWEATHER_API_KEY}"

# Zainstaluj requests
# Napisz funkcję, fetch_weather, która pobiera dane pogodowe w taki sam sposób jak dane z restcountries

def fetch_weather():
    try:
        response = requests.get(URL)
        data = response.json()

        weather_dict = {
            "miasto": data.get("name"),
            "temperatura": data.get("main").get("temp"),
            "odczuwalna_temperatura": data.get("main").get("feels_like"),
            "wilgotnosc": data.get("main").get("humidity"),
            "cisnienie": data.get("main").get("pressure"),
            "wiatr": {
                "predkosc": data.get("wind").get("speed"),
                "kierunek": data.get("wind").get("deg")
            },
            "data_pomiaru": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return weather_dict

    except Exception as e:
        print(e)

