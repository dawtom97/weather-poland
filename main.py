from config import Config
from services.openweather_api import fetch_weather
from services.excel_files import save_to_excel,read_excel_file
from services.mysql_db import save_record
from config import Config
import time

while True:
    weather = fetch_weather()
    # save_to_excel(weather, Config.XLSX_PATH)
    # read_excel_file(Config.XLSX_PATH)
    save_record(weather)
    # Zapis do DB
    # Wykresy i interfejs
    time.sleep(5)

