# Apex AFK Farm Bot

![image](https://github.com/letsmokee/ApexXPFarmer/assets/107760297/cd3ffa15-e314-4c1d-860d-87f75093bd2a)

# SUPORT

**For any support join [telegram group](https://t.me/+vL7stRVin1g2YmM8)**

## GENERAL

Based on [apexAFKfarmbot](https://github.com/iIndrasura/apexAFKfarmbot) for inspiration

The Apex AFK Farm Bot is a powerful automation tool designed to assist Apex Legends players in farming in-game rewards while being AFK (Away From Keyboard). This repository provides the source code and instructions for using the bot effectively.
This script automates certain actions in the game using Python libraries such as pyautogui, keyboard, and PyScreeze. It simulates human behavior by interacting with the game interface based on screen recognition.

## FEATURES
**WORKS WITH SEASON 19 - ONLY 1920x1080 16:9**
- starting the game automatically
- auto restart game on set interval (default = 9000)
- WHY: on low performance systems sometimes due to low memory game would freeze randomly after some hours<br />
  With this automatic restart it runs 12+ hours tested
- anti-kick
- auto start matchmaking
- getting out of news, battlepass windows etc.
- remembering how much XP you got in a session
- remembering how much time you farmed in a session<br />
- restart matchmaking if stuck
- see average XP / HOUR gained
- legend select
- DEBUG: see how many matches OCR for EXP didn't work

## PREREQUISITES
- PYTHON (if you want to use directly the source code)
- WINDOWS 64 BIT (if you use the executable)
- Tesseract open source from Google to OCR the EXP earned in game. Please see following: [Tesseract](https://github.com/tesseract-ocr/tesseract), [Tesseract Installation](https://tesseract-ocr.github.io/tessdoc/Installation.html) and [Tesseract Download for Windows](https://github.com/UB-Mannheim/tesseract/wiki)
- Set PATH for Tesseract to work (see below instructions)

## SETTING UP
**Tesseract:**
1. Download Tesseract from the upper link
2. In the installation process, copy the directory of install (default: C:\Program Files\Tesseract-OCR)
3. Install it
4. After installation, search in windows box 'enviroments' and click on 'Edit the system enviroment variables' (may be different on Windows 10, 8.1 etc.)
5. With the open window, click on Path, either from user variables (if you are only planning on using the bot on current Windows User) or system variables (if you plan to use it system wide)
![image](https://github.com/letsmokee/ApexXPFarmer/assets/107760297/195fa293-71a9-4a3f-a60a-1728bf2cb122)
6. Click on edit -> New and insert Tesseract directory of install
![image](https://github.com/letsmokee/ApexXPFarmer/assets/107760297/7fb99b53-81cb-4b75-a046-f53e7eee7fb3)
7. Save and exit

   NOTE: To test, open cmd and type tesseract, if command is not found, repeat steps

**Apex Farmer**
- To setup, on first run it will generate a config.ini file which you need to edit with your Apex directory and time for restart

## Installation
- WINDOWS installation
    1. Download executable from [release](https://github.com/letsmokee/ApexXPFarmer/releases/)
    2. Run the executable, on first run it will generate a config.ini file which you need to edit with your Apex directory and time for restart
    3. Follow the on screen instructions
       
## CONFIG.INI
 ```
[CONFIG]
time = 9000 -> time to restart game in seconds
apexdir = C:\Program Files\EA Games\Apex\\r5apex.exe -> Apex directory and executable (if using steam, delete the path and just write "steam")
ocr_debug = 0 -> EXP OCR debug mode (make screenshots to see debug why OCR didn't work)
show_exp = 1 -> -> if you want to show experience gained
champion = Lifeline -> Legend that you want to select

[KEYBINDS]
crouch_key = c -> Your crouch key
heal_key = 4 -> Your healing key
ability_key = q -> Your ability key
custom_key1 = -> Custom key if you want (leave blank if you don't want any custom key)
custom_key2 = -> Custom key if you want (leave blank if you don't want any custom key)
```
 For Legend selection use one of the following:
 **"Bloodhound","Gibraltar","Lifeline","Pathfinder","Wraith","Bangalore","Caustic","Mirage","Octane","Wattson","Crypto","Revenant","Loba","Rampart","Horizon","Fuse","Valkyrie","Seer","Ash","MadMaggie","Newcastle","Vantage","Catalyst","Ballistic","Conduit"**

**NOTE: For now, only Ashe, Vangalore, Bloodhound, Catalyst, Conduit, Fuse, Gibraltar, Horizon, Lifeline, Loba, Newcastle, Octane, Pathfinder, Revenant, Rampart, Seer, Valkyrie, Wraith are working**

## PROBLEMS ENCOUNTERED
If you encounter any problem, open a cmd window where executable is, type 'ApexFarmer.exe' and run the script as normal. When the error will occur, cmd window will not close itself
- Open an issue with the error code.
- Join [telegram group](https://t.me/+vL7stRVin1g2YmM8)

## PHOTOS
**24 HOUR FARM SESSION, 6062 XP / HOUR AVERAGE**

![24hrs](https://github.com/letsmokee/ApexXPFarmer/assets/107760297/61549d85-d1df-49f8-862b-e6ce11b88f4b)

**3 DAYS+ FARM SESSION, 7747 XP / HOUR AVERAGE**

![3 days](https://github.com/letsmokee/ApexXPFarmer/assets/107760297/42fdeefe-88d4-4325-9870-1f812f192e77)


## Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or new features to add, feel free to open an issue or submit a pull request.

**Disclaimer: The usage of this script is at your own risk, and the developer takes no responsibility for any consequences resulting from its use.**
