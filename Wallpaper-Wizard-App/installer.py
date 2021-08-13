import os
import sys
import json
import tkinter as tk
from tkinter import filedialog
def install_config():
    city = input("Where do you live: ")
    has_api_key = input("Do you have an OpenWeatherMap API key (y/n): ")
    if(has_api_key=="y"):
        api_key = input("Enter your OpenWeatherMap API key: ")
    else:
        print("You have to get your own free OpenWeatherMap API key from https://openweathermap.org/api")
        api_id = input("Enter your OpenWeatherMap API key (might take a few minutes to get): ")
    advanced = input("Do you want to enter advanced installation settings (y/n): ")
    def_update_interval = 300
    def_check_internet = 60
    def_sunset_duration = 60
    def_default_weather = "Sunset"
    def_theme_path = curr_path+"Themes/Konbini-New"
    if(advanced=="y"):
        default_weather = input("Choose default weather (no internet) (default={}): ".format(def_default_weather))
        if(default_weather==""):
            default_weather = def_default_weather
            print("using default")
        update_interval = input("How often do you want to update the wallpaper (in seconds) (default={}): ".format(def_update_interval))
        if(update_interval==""):
            update_interval = def_update_interval
            print("using default")
        check_internet = input("How often do you want to check for internet connection (in seconds) (default={}): ".format(def_check_internet))
        if(check_internet==""):
            check_internet = def_check_internet
            print("using default")
        sunset_duration = input("How long do you want sunsets and sunrises to last (in minutes) (default={}): ".format(def_sunset_duration))
        if(sunset_duration==""):
            sunset_duration = def_sunset_duration
            print("using default")
        different_theme = input("Would you like to use a different theme (y/n): ")
        if(different_theme == "y"):
            print("Choose theme folder")
            theme_path = filedialog.askdirectory()
            if(theme_path == ""):
                theme_path = def_theme_path
                print("using default")
        else:
            theme_path = def_theme_path
    else:
        update_interval = def_update_interval
        check_internet = def_check_internet
        sunset_duration = def_sunset_duration
        default_weather = def_default_weather
        theme_path = def_theme_path
    j_dict = {"city":city, "api_key":api_key, "theme_directory":theme_path, "default_weather": default_weather, "update_interval (in seconds)": float(update_interval), "check_internet_interval (in seconds)": float(check_internet), "sunset/sunrise duration (in minutes)":float(sunset_duration)}
    j_str = json.dumps(j_dict, indent=4)
    j_file = open("config.json", "w")
    j_file.write(j_str)
    j_file.close()

def install_startup_script():
    
    startup = "{}/{}/{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/".format(split_path[0], split_path[1], split_path[2])
    f = open(startup+"WallpaperWizard.vbs", mode="w")
    f.write('Set oShell = CreateObject ("WScript.Shell")\n')
    f.write('oShell.run "pythonw {}"'.format(curr_path+"WallpaperWizard.py"))
    f.close()
def get_current_path():
    curr_path = os.path.dirname(sys.argv[0])
    split_path = curr_path.split("\\")
    curr_path = ""
    for i in split_path:
        curr_path += i+"/"
    return curr_path, split_path
def main():
    global curr_path, split_path
    print("Setup\n")
    print("You can change these values later by running this script again, or by editing the config.json file directly.\n")
    curr_path, split_path = get_current_path()
    tk.Tk().withdraw()
    install_config()
    install_startup_script()
    
    print("installation succeeded")
    input("press enter to exit")
if(__name__=="__main__"):
    main()
