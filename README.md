# Apex AFK Farm Bot

Based on [apexAFKfarmbot](https://github.com/iIndrasura/apexAFKfarmbot) for inspiration

The Apex AFK Farm Bot is a powerful automation tool designed to assist Apex Legends players in farming in-game rewards while being AFK (Away From Keyboard). This repository provides the source code and instructions for using the bot effectively.
This script automates certain actions in the game using Python libraries such as pyautogui, keyboard, and PyScreeze. It simulates human behavior by interacting with the game interface based on screen recognition.

## FEATURES
**WORKS WITH SEASON 19 - ONLY 1920x1080 16:9**
- starting the game automatically
- auto restart game on set interval (default = 9000)
- WHY: on low performance systems sometimes due to low memory game would freeze randomly after some hours
- With this automatic restart it runs 12+ hours tested
- anti-kick
- auto start matchmaking
- getting out of news, battlepass windows etc.
- remembering how much XP you got in a session
- remembering how much time you farmed in a session

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
 ![image](https://github.com/letsmokee/ApexXPFarmer/assets/107760297/4b3cb9ff-20bc-4543-bf8a-9b8423c1f53d)

## PROBLEMS ENCOUNTERED
If you encounter any problem, open a cmd window where executable is, type 'ApexFarmer.exe' and run the script as normal. When the error will occur, cmd window will not close itself
- Open an issue with the error code.

## Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or new features to add, feel free to open an issue or submit a pull request.

**Disclaimer: The usage of this script is at your own risk, and the developer takes no responsibility for any consequences resulting from its use.**
