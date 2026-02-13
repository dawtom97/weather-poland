import threading
import atexit

from services.openweather_api import fetch_weather
from services.mysql_db import save_record

_stop_event = threading.Event()
_thread = None

def _loop(interval_seconds: int):
    while not _stop_event.is_set():
        try:
            weather = fetch_weather()
            if weather:
                save_record(weather)
        except Exception as e:
            print(f"[weather_job] error: {e}")

        _stop_event.wait(interval_seconds)

def start_weather_job(interval_seconds: int = 30):
    global _thread

    if _thread and _thread.is_alive():
        return

    _stop_event.clear()
    _thread = threading.Thread(
        target=_loop,
        args=(interval_seconds,),
        daemon=True
    )
    _thread.start()

def stop_weather_job():
    _stop_event.set()

atexit.register(stop_weather_job)
