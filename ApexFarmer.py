import configparser
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import subprocess
import os
import numpy as np
import win32gui
import win32com.client 
import win32con
import sys
import msvcrt
import datetime
import pytesseract
import cv2

# instantiate
config = configparser.ConfigParser()
if os.path.isfile('config.ini') is not True:
    config['CONFIG'] = {'Time': '9000',
                     'ApexDir': r'C:\Program Files\EA Games\Apex\\r5apex.exe',
                     'OCR_debug': '0',
                     'show_exp': '1'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
elif os.path.isfile('config.ini') is True:
# parse existing file
    config.read('config.ini')

# read values from a section
timp = int(config.get('CONFIG', 'Time'))
apexdir = str(config.get('CONFIG', 'ApexDir'))
OCR_debug = int(config.get('CONFIG', 'OCR_debug'))
show_exp = int(config.get('CONFIG', 'show_exp'))

print(r"           _____  ________   __   ______      _____  __  __ ______ _____   ")
print(r"     /\   |  __ \|  ____\ \ / /  |  ____/\   |  __ \|  \/  |  ____|  __ \  ")
print(r"    /  \  | |__) | |__   \ V /   | |__ /  \  | |__) | \  / | |__  | |__) | ")
print(r"   / /\ \ |  ___/|  __|   > <    |  __/ /\ \ |  _  /| |\/| |  __| |  _  /  ")
print(r"  / ____ \| |    | |____ / . \   | | / ____ \| | \ \| |  | | |____| | \ \  ")
print(r" /_/____\_\_|__  |______/_/_\_\  |_|/_/ ___\_\_|  \_\_|__|_|______|_|__\_\ ")
print(r"  ____ _     _    _      ______ ________ ____ __  __  ____  _  __ _____    ")
print(r" |  _ \ \   / /  | |    |  ____|__   __/ ____|  \/  |/ __ \| |/ /  ____|   ")
print(r" | |_) \ \_/ /   | |    | |__     | | | (___ | \  / | |  | | ' /| |__      ")
print(r" |  _ < \   /    | |    |  __|    | |  \___ \| |\/| | |  | |  < |  __|     ")
print(r" | |_) | | |     | |____| |____   | |  ____) | |  | | |__| | . \| |____    ")
print(r" |____/  |_|     |______|______|  |_| |_____/|_|  |_|\____/|_|\_\______|   ")
print("") 
print("            ___________________                      ")
print("CONFIG: -> | Time for restart: | >>>", timp, "sec")
print("CONFIG: -> |  Apex Directory:  | >>>", apexdir)
print("CONFIG: -> |  Show earned XP:  | >>>", show_exp)
print("CONFIG: -> |    DEBUG MODE:    | >>>", OCR_debug)
print("            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                      ")
print("Press any key to continue if settings are correct")
msvcrt.getch()
print("Continuing...")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Random = ['4','q','1','2','3','4'] #don't touch
time.sleep(2)
window_found = 0
exp=0
exp_new=0
exp_new1=0
exp_new2=0
n = 1

#checking if apex is running
def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False

start_time_absolute = time.time()

if process_exists('r5apex.exe'):
    mod = 2
    start_time = time.time()

else: 
    mod = 1
#checking if apex is running    

#program loop
while True:
    #print ('Mod = ', mod)
    print ('----------Starting game and setting Apex window active-----------')
    #starting game, make apex window active, starting counting for game restart
    if mod == 1:
        subprocess.call([apexdir])
        time.sleep(10)
        start_time = time.time()
        window_found = 0
        mod = 2

    #checkking if game was opened and closing news or other in game windows
    while mod == 2:
        print ('----------Checking if game is opened and getting into main menu-------------')
        apex_hwnd = win32gui.FindWindow(None,'Apex Legends')
        time.sleep(0.5)
        if (apex_hwnd != 0) and (window_found == 0):
            time.sleep(5)
            pyautogui.press("alt")
            win32gui.SetForegroundWindow(apex_hwnd)
            win32gui.SetActiveWindow(apex_hwnd)
            win32gui.ShowWindow(apex_hwnd, win32con.SW_RESTORE)
            end_time = time.time()
            time_lapsed = end_time - start_time
            pyautogui.moveTo(200,100)
            window_found = 1
            
        if pyautogui.locateOnScreen(resource_path('ss\\InGame.png'), region=(87, 755, 379, 304), grayscale=True, confidence=0.5) is not None:
            print("-------------In game detected, moving to mode farming--------------")
            mod = 3

        if pyautogui.locateOnScreen(resource_path('ss\\gameopen.png'), grayscale=True, confidence=0.7) != None:
            pyautogui.click(956, 647)
            time.sleep(np.random.uniform(0.3,0.8))
            pyautogui.click(956, 647)     

        if pyautogui.locateOnScreen(resource_path('ss\\news.png'), grayscale=True, confidence=0.6) != None:
            #print("news")
            keyboard.press_and_release('esc')
            
        if pyautogui.locateOnScreen(resource_path('ss\\space2.png'), grayscale=True, confidence=0.6) != None:
            #print("continue2")
            keyboard.press_and_release('esc')

        if pyautogui.locateOnScreen(resource_path('ss\\space2.png'), region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
            #print("space2.png")
            keyboard.press_and_release('space')
            time.sleep(np.random.uniform(0.4,0.8))

        if pyautogui.locateOnScreen(resource_path('ss\\back.png'), grayscale=True, confidence=0.6) != None:
            #print("back")
            time.sleep(np.random.uniform(0.3,0.8))
            keyboard.press_and_release('esc')

        if pyautogui.locateOnScreen(resource_path('ss\\team.png'), confidence=0.9) != None:
            apex_hwnd = win32gui.FindWindow(None,'Apex Legends')
            if apex_hwnd != 0:
                time.sleep(1)
                pyautogui.press("alt")
                win32gui.SetForegroundWindow(apex_hwnd)
                win32gui.SetActiveWindow(apex_hwnd)
                pyautogui.moveTo(119,582)
                pyautogui.click(119,582)
                time.sleep(2)
                pyautogui.moveTo(200,100)
        if (pyautogui.locateOnScreen(resource_path('ss\\team.png'), confidence=0.9) is None) and (pyautogui.locateOnScreen(resource_path('ss\\notready.png'), region=(0,538,447,528), grayscale=True, confidence=0.7) != None):
            time.sleep(1)
            print ('----------Apex window active and game started------------')
            if pyautogui.locateOnScreen(resource_path('ss\\team.png'), confidence=0.9) is None:
                print('------------------------------------------------')            
                print('---------------Fill not checked-----------------')
                print('------------------------------------------------')
                pyautogui.moveTo(200,100)
                mod = 3
        #print ('WHILE mod = ', mod)
    
    
    #program loop
    while mod == 3:
        #print ('Mod = ', mod)
        #updating time lapsed since start of farming on new instance
        end_time = time.time()
        time_lapsed = end_time - start_time
        end_time_absolute = time.time()
        time_lapsed_absolute = end_time_absolute - start_time_absolute
        
        #starting matchmaking
        if time_lapsed > timp-600:
            pyautogui.click(200, 100)
        elif (pyautogui.locateOnScreen(resource_path('ss\\notready.png'), region=(0,538,447,528), confidence=0.8) != None) and (time_lapsed < timp-600):
            pyautogui.moveTo(230,950)
            pyautogui.click(230,950)
            time.sleep(np.random.uniform(0.3,0.8))
            pyautogui.moveTo(200,100)
            time.sleep(0.1)

        elif (pyautogui.locateOnScreen(resource_path('ss\\matchmaking.png'), region=(0,538,447,528), confidence=0.8) != None) and (time_lapsed < timp-600):
            print ('----------MATCHMAKING STARTED------------')
        else:
            pass
        
        if pyautogui.locateOnScreen(resource_path('ss\\space2.png'), region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
            #print("space2.png")
            keyboard.press_and_release('space')
            time.sleep(np.random.uniform(0.4,0.8))
        
        if pyautogui.locateOnScreen(resource_path('ss\\InGame.png'), region=(87, 755, 379, 304), grayscale=True, confidence=0.5) is not None:
            #print("-------------In game waiting--------------")
            keyboard.press_and_release(Random)
            time.sleep(0.5)
            ingame = 1
            if '4' in Random:
                time.sleep(np.random.uniform(5.5,6))
            else:
                time.sleep(np.random.uniform(0.6, 1.5)) 
        else: ingame = 0
    
        if pyautogui.locateOnScreen(resource_path('ss\\dead.png'), region=(441,19,1017,304), grayscale=True, confidence=0.6) or pyautogui.locateOnScreen(resource_path('ss\\2ndplace.png'), region=(441,19,1017,304), confidence=0.6) != None:
            #print("dead")
            time.sleep(np.random.uniform(1,2))
            keyboard.press_and_release('space')
            time.sleep(np.random.uniform(1,2))
            while True:
                if pyautogui.locateOnScreen(resource_path('ss\\yes.png'), region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
                    #print('yes')
                    pyautogui.click(850, 713)
                    time.sleep(np.random.uniform(0.4,0.8))
                    pyautogui.click(850, 713)
                if pyautogui.locateOnScreen(resource_path('ss\\matchsummary.png'), region=(564,18,814,115), grayscale=True, confidence=0.8) != None:
                    #print('matchsummary')
                    keyboard.press_and_release('space')
                    time.sleep(2)
                    if pyautogui.locateOnScreen(resource_path('ss\\matchsummary.png'), region=(564,18,814,115), grayscale=True, confidence=0.8) is None:
                        while True:
                            if pyautogui.locateOnScreen(resource_path('ss\\expscreen.png'), region=(657,0,603,97), confidence=0.8) != None:
                                #print('exp screen')
                                time.sleep(6)
                                if show_exp==1:
                                    image1=pyautogui.screenshot(region=(445,231,80,37))
                                    imagenp1 = np.array(image1)
                                    gray1 = cv2.cvtColor(imagenp1, cv2.COLOR_BGR2GRAY)
                                    invert1 = 255 - gray1
                                    
                                    image2=pyautogui.screenshot(region=(439,272,84,34))
                                    imagenp2 = np.array(image2)
                                    gray2 = cv2.cvtColor(imagenp2, cv2.COLOR_BGR2GRAY)
                                    invert2 = 255 - gray2
                                    if OCR_debug == 1:
                                        pyautogui.screenshot("saved_without"+str(n)+".png")
                                        #pyautogui.screenshot("ocrscan1_"+str(n)+".png",region=(445,231,80,37))
                                        #pyautogui.screenshot("ocrscan2_"+str(n)+".png",region=(439,272,84,34))
                                    exp_new1 = int(pytesseract.image_to_string(invert1,lang='eng', config='--psm 12 -c tessedit_char_whitelist=0123456789'))
                                    try:
                                        exp_new2 = int(pytesseract.image_to_string(invert2,lang='eng', config='--psm 12 -c tessedit_char_whitelist=0123456789'))
                                    except ValueError:
                                        pass
                                    exp_new=exp_new1+exp_new2
                                    exp=exp+exp_new
                                    if OCR_debug == 1:
                                        pyautogui.screenshot("saved_exp" +str(exp_new)+".png")
                                        file = open("data.txt", "a")
                                        file.write("n = " + str(n) + ' - ' + str(exp_new) + " exp" + '--- exp_new=' +str(exp_new1) + " exp" + '--- exp_new=' +str(exp_new2) + " exp\n")
                                        file.close()
                                        n=n+1
                                time.sleep(np.random.uniform(0.4,0.8))
                                #print('space dupa expscreen')
                                keyboard.press_and_release('space')
                                time.sleep(np.random.uniform(0.4,0.7))
                                break
                        break
                
        if pyautogui.locateOnScreen(resource_path('ss\\news.png'), grayscale=True, confidence=0.6) != None:
            #print("news")
            keyboard.press_and_release('esc')
        
        if pyautogui.locateOnScreen(resource_path('ss\\close.png'), grayscale=True, confidence=0.6) != None:
            #print("close")
            keyboard.press_and_release('esc')
        
        if pyautogui.locateOnScreen(resource_path('ss\\startmenu.png'), region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
            pyautogui.click(952, 717)
            time.sleep(np.random.uniform(0.3,0.7))
            pyautogui.click(952, 717)
        if show_exp==1:
            print ('---------- Currently farming for ',datetime.timedelta(seconds=round(time_lapsed_absolute)),'TOTAL EXP:', exp, 'New EXP:',exp_new,'--------------')
            print ('---------- Time counted for restart: ',datetime.timedelta(seconds=round(time_lapsed)),'-----','ingame:' ,ingame, "--------------------")
        else:
            print ('---------- Currently farming for ',datetime.timedelta(seconds=round(time_lapsed_absolute)),'--------------')
            print ('---------- Time counted for restart: ',datetime.timedelta(seconds=round(time_lapsed)),'-----','ingame:' ,ingame, "--------------------")
        
        #checking if time lapsed is more than set time and checking if it's in game
        if (time_lapsed > timp-600) and (ingame == 0):
            time.sleep (15)
            mod = 4
        if process_exists('r5apex.exe'):
            pass
        else: 
            print ('---------- APEX IS NOT RUNNING, WHAT DO YOU WANT TO DO? -------------')
            print ('---------- STOP - TYPE 1 /// RESTART - TYPE 2 -------------')
            while True:
                data_input = int(input('PICK WHAT TO DO NEXT: '))
                if data_input == 1:
                    print ('---------- SESSION STATS -------------')
                    if show_exp==1:
                        print ('---------- TIME: ',datetime.timedelta(seconds=round(time_lapsed_absolute)),' | TOTAL EXP EARNED:', exp,'--------------')
                        print ('---------- EXIT IN 5 SEC --------------')
                        time.sleep(5)
                        exit()
                    else:
                        print ('---------- TIME: ',datetime.timedelta(seconds=round(time_lapsed_absolute)),'--------------')
                        print ('---------- EXIT IN 5 SEC --------------')
                        time.sleep(5)
                        exit()
                elif data_input == 2:
                    print ('---------- PROGRAM RESTART -------------')
                    mod = 1
                    exp=0
                    exp_new=0
                    exp_new1=0
                    exp_new2=0
                    break
                else:
                    print ('You have made an invalid choice, try again.')
            
#checking if apex is running 

    if mod == 4:
        os.system('taskkill /f /im r5apex.exe')
        os.system('taskkill /f /im r5apex.exe')
        time.sleep(15)
        mod = 1
        
