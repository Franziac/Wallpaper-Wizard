import ctypes
import requests
import json
import time
import schedule
import random
import os
import sys


priority = ["Thunderstorm", "Rain", "Snow", "Night", "Clouds", "Fog", "Sunset", "Day", "Clear"]

def get_weather():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, app_id))
    data = json.loads(response.text)
    weather_name = data.get("weather")[0].get("main")
    sunrise =  data.get("sys").get("sunrise")
    sunset = data.get("sys").get("sunset")
    period = ""
    sunset_duration = 3600 #in seconds
    if (sunset_duration >= abs(time.time() - sunrise) or sunset_duration >= abs(time.time() - sunset)):
        period = "Sunset";
    elif ((sunrise + sunset_duration) < time.time() and time.time() < (sunset - sunset_duration)):
        period = "Day"
    else:
        period = "Night"
    if (weather_name == "Drizzle"):
        weather_name = "Rain"
    elif (weather_name == "Mist" or weather_name == "Smoke" or weather_name == "Haze" or weather_name == "Dust" or weather_name == "Sand" or weather_name == "Ash" or weather_name== "Squall" or weather_name == "Tornado"):
        weather_name = "Fog"
    for p in priority:
        if(p == period or p == weather_name):
            return p

def change_bg(weather):
    f = open(theme_dir+"/theme.json")
    j = json.loads(f.read())
    f.close()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, theme_dir+j.get(weather), 3)
def get_config():
    global city, app_id, theme_dir, default_weather, update_interval, check_internet_interval
    f = open(os.path.dirname(sys.argv[0])+"/config.json")
    j = json.loads(f.read())
    f.close()
    city = j.get("city")
    app_id = j.get("app_id")
    theme_dir = j.get("theme_directory")
    default_weather = j.get("default_weather")
    update_interval = j.get("update_interval (in seconds)")
    check_internet_interval = j.get("check_internet_interval (in seconds)")

last_weather = ""
while True:
    try:
        get_config()
        weather = get_weather()
        if(last_weather != weather):
            change_bg(weather)
            last_weather = weather
        time.sleep(update_interval)
    except:
        get_config()
        change_bg(default_weather)
        time.sleep(check_internet_interval)
    
    

                           



