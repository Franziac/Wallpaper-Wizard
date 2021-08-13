# Wallpaper-Wizard

Wallpaper Wizard is a tool that allows you to change your wallpaper based on the weather and time of day.

## Installation

Note: Python 3.x required
1. Download the Wallpaper-Wizard-App folder
2. Run the installer.py
3. Follow the installers instructions

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

4. Have all the images and the theme.json file in a single folder (preferably with no other files)
5. Run the installer.py and enter advanced options.
6. Say yes to using a different theme and select the folder containing the theme.
7. Finish the installation

## About

I had some issues with the original version made by @Cyndakwill and @diemer (notably the program asking for the API key after every restart) and I found their application to be overly complex (maybe I'm just not used to C#). So I coded my own version of the using the basic principles used in the other version. The program runs nicely and it's quite simple. It doesn't have an UI which isn't an issue for me but with the appropriate skills one could quite easily be made with the config.json working as a bridge.

This version definetly isn't as user-friendly as the original, but with some improvement it could be.

## Credits

Artwork: 
* Firewatch: ?
* Konbini-Old:  [Jaume Rovira Llorca](https://www.artstation.com/jumkun), [@Cyndakwill](https://github.com/Cyndakwil) (?)
* Konbini-New: [Jaume Rovira Llorca](https://www.artstation.com/jumkun), [@Cyndakwill](https://github.com/Cyndakwil)(?), [@Franziac](https://github.com/Franziac)
* Random: ?
    
