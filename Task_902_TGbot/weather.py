import pyowm
import keys

def weather_checker(city: str):
    owm = pyowm.OWM(keys.OWM_TOKEN)
    mng = owm.weather_manager()
    get_data = mng.weather_at_place(city)
    w = get_data.weather
    temperature = w.temperature('celsius')['temp']
    wind = w.wind()['speed']
    res = f'Сейчас в {city} температура: {temperature} по Цельсию\nСкорость ветра {wind} м/c'
    return res

# ---------- FREE API KEY examples ---------------------
# w.detailed_status         # 'clouds'
# w.wind()                  # {'speed': 4.6, 'deg': 330}
# w.humidity                # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain                    # {}
# w.heat_index              # None
# w.clouds                  # 75
# ---------- FREE API KEY examples ---------------------