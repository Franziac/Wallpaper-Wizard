# Wallpaper-Wizard

Wallpaper Wizard is a tool that allows you to change your wallpaper based on the weather and time of day.

## Installation

Note: Python 3.x required
Download the Wallpaper-Wizard-App folder and run the installer.py

## Importing a theme

1. Organize all your images into a folder.
2. In the same folder, add a `theme.json` file.
3. Add the appropriate values into the json file. The following is an example of a theme file with all required values filled.
```
{
    "Title": "Konbini",
    "Day": "Konbini_Day.jpg",
    "Night": "Konbini_Night.jpg",
    "Sunset": "Konbini_Sunset.jpg",
    "Rain": "Konbini_Rain.jpg",
    "Thunderstorm": "Konbini_Rain.jpg",
    "Clouds": "Konbini_Day.jpg",
    "Snow": "Konbini_Rain.jpg",
    "Fog": "Konbini_Day_Foggy.jpg"
}
```

Make sure all filenames and values are spelled correctly with the correct capitalization.
4. Have all the images and the json file in a single folder (preferably with no other files)
5. Run the installer.py and enter advanced options.
6. Say yes to using a different theme and select the folder containing the theme.
7. Finish the installation
