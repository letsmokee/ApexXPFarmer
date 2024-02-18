import configparser
import ctypes
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
import rainbowtext
from inputimeout import inputimeout, TimeoutOccurred


# instantiate

UP = '\033[1A'
CLEAR = '\x1b[2K'
ctypes.windll.kernel32.SetConsoleTitleW("APEX XP FARM BOT BY LETSMOKE")
config = configparser.ConfigParser()
if os.path.isfile('config.ini') is not True:
    config['CONFIG'] = {'Time': '9000',
                     'ApexDir': r'C:\Program Files\EA Games\Apex\\r5apex.exe',
                     'OCR_debug': '0',
                     'show_exp': '1',
                     'Champion': 'Lifeline'}
    config['KEYBINDS'] = {'Crouch_Key': 'c',
                    'Heal_Key': '4',
                    'Ability_Key': 'q',
                    'Custom_Key1': '',
                    'Custom_Key2': ''}
    config['FARM TOGETHER'] = {'LEADER': 'FALSE',
                    'ACCOUNT_1': 'None',
                    'ACCOUNT_2': 'None'}
    

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
champion = str(config.get('CONFIG', 'Champion'))

crouch_key = str(config.get('KEYBINDS', 'Crouch_Key'))
heal_key = str(config.get('KEYBINDS', 'Heal_Key'))
ability_key = str(config.get('KEYBINDS', 'Ability_Key'))
custom_key1 = str(config.get('KEYBINDS', 'Custom_Key1'))
custom_key2 = str(config.get('KEYBINDS', 'Custom_Key2'))

leader = str(config.get('FARM TOGETHER', 'LEADER'))
friend1 = str(config.get('FARM TOGETHER', 'ACCOUNT_1'))
friend2 = str(config.get('FARM TOGETHER', 'ACCOUNT_2'))

if leader=='FALSE':
    friend1='None'
    friend2='None'

#------------------
if (custom_key1 == '') and (custom_key2 == ''):
    Random = ['w','a','s','d',crouch_key,heal_key,ability_key]
elif custom_key1 == '':
    Random = ['w','a','s','d',crouch_key,heal_key,ability_key,custom_key2]
elif custom_key2 == '':
    Random = ['w','a','s','d',crouch_key,heal_key,ability_key,custom_key1]
else:
    Random = ['w','a','s','d',crouch_key,heal_key,ability_key,custom_key1,custom_key2]

exp_read=0
matchmaking=0
timer_matchmaking=0
timer_matchmaking_end=0
timer_matchmaking_start=0
window_found = 0
exp=0
exp_new=0
exp_new1=0
exp_new2=0
exp_new4=0
n = 1
time_stuck=0
time_stuck_start=0
time_stuck_end=0
boost=["1BoostApplied","2BoostApplied","3BoostApplied","4BoostApplied","5BoostApplied","6BoostApplied","7BoostApplied","8BoostApplied","9BoostApplied"]
coords_boost=[849,566,153,62]
coords_no_boost=[807,551,194,62]
team_coords=[24,521,409,189]
xp_hour=0
x=0
y=0
coords_auto_fill_x=0
coords_auto_fill_y=0
champ_list=["Bloodhound","Gibraltar","Lifeline","Pathfinder","Wraith","Bangalore","Caustic","Mirage","Octane","Wattson","Crypto","Revenant","Loba","Rampart","Horizon","Fuse","Valkyrie","Seer","Ash","MadMaggie","Newcastle","Vantage","Catalyst","Ballistic","Conduit"]
champ_string=r'legends\\'+champion+'.png'
friend_region=[[573,265,284,34],(573,365,284,34),(573,465,284,34),(573,565,284,34),(573,665,284,34),(573,765,284,34),(573,865,284,34),(573,965,284,34)]
invite_region=[[560,265,323,82],(560,355,323,82),(560,455,323,82),(560,555,323,82),(560,655,323,82),(560,755,323,82),(560,855,323,82),(560,955,323,82)]
k=0
friend1_invited=0
friend2_invited=0
friendlist_window=0
invite1='0'
invite2='0'
invited1='0'
invited2='0'
time_slept=0
f1_coords=0
f2_coords=0
friendlist1_coords=0
friendlist2_coords=0
leader_text='0'
apex_detected=0
friend1_not_invited=1
friend2_not_invited=1
invite_accepted=0




print(rainbowtext.text(r"           _____  ________   __   ______      _____  __  __ ______ _____   "))
print(rainbowtext.text(r"     /\   |  __ \|  ____\ \ / /  |  ____/\   |  __ \|  \/  |  ____|  __ \  "))
print(rainbowtext.text(r"    /  \  | |__) | |__   \ V /   | |__ /  \  | |__) | \  / | |__  | |__) | "))
print(rainbowtext.text(r"   / /\ \ |  ___/|  __|   > <    |  __/ /\ \ |  _  /| |\/| |  __| |  _  /  "))
print(rainbowtext.text(r"  / ____ \| |    | |____ / . \   | | / ____ \| | \ \| |  | | |____| | \ \  "))
print(rainbowtext.text(r" /_/____\_\_|__  |______/_/_\_\  |_|/_/ ___\_\_|  \_\_|__|_|______|_|__\_\ "))
print(rainbowtext.text(r"  ____ _     _    _      ______ ________ ____ __  __  ____  _  __ _____    "))
print(rainbowtext.text(r" |  _ \ \   / /  | |    |  ____|__   __/ ____|  \/  |/ __ \| |/ /  ____|   "))
print(rainbowtext.text(r" | |_) \ \_/ /   | |    | |__     | | | (___ | \  / | |  | | ' /| |__      "))
print(rainbowtext.text(r" |  _ < \   /    | |    |  __|    | |  \___ \| |\/| | |  | |  < |  __|     "))
print(rainbowtext.text(r" | |_) | | |     | |____| |____   | |  ____) | |  | | |__| | . \| |____    "))
print(rainbowtext.text(r" |____/  |_|     |______|______|  |_| |_____/|_|  |_|\____/|_|\_\______|   "))
print("") 
print("            ___________________                      ")
print("CONFIG: -> | Time for restart: | >>>", timp, "sec")
print("CONFIG: -> |  Apex Directory:  | >>>", apexdir)
print("CONFIG: -> |  Show earned XP:  | >>>", show_exp)
print("CONFIG: -> |      Champion     | >>>", champion)
print("CONFIG: -> |    DEBUG MODE:    | >>>", OCR_debug)
print("            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                      ")
print('')
print('')
print('')
print('')
print('')
print("Press any key to continue if settings are correct")
msvcrt.getch()
print(UP, end=CLEAR)
time.sleep(0.005)
print("Continuing...")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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
    time_stuck_start= time.time()
    apex_detected=1

else: 
    mod = 1
#checking if apex is running   
#program loop
while True:
    time.sleep(0.005)
    #starting game, make apex window active, starting counting for game restart
    if mod == 1:
        if process_exists('r5apex.exe') is False:
            print(UP, end=CLEAR)
            print ("------------------------------------GAME NOT STARTED, STARTING-------------------------------------")
            if apexdir=='steam':
                subprocess.run("start steam://rungameid/1172470", shell=True)
            else:
                subprocess.call([apexdir])
        start_time = time.time()
        time_stuck_start= time.time()
        time_stuck_end=0
        time.sleep(10)
        window_found = 0
        mod = 2

    #checkking if game was opened and closing news or other in game windows
    while mod == 2:
        time_stuck_end=time.time()
        time.sleep(0.5)
        time_stuck=time_stuck_end-time_stuck_start
        if time_stuck>240:
            mod=4
        apex_hwnd = win32gui.FindWindow(None,'Apex Legends')
        time.sleep(0.5)
        if (apex_hwnd != 0) and (window_found == 0):
            print(UP, end=CLEAR)
            print ('----------APEX LEGENDS FOUND, PROCEEDING SETTING ACTIVE WINDOW AND PREPARE FOR MATCHMAKING-------------')
            time.sleep(5)
            pyautogui.press("alt")
            win32gui.SetForegroundWindow(apex_hwnd)
            win32gui.SetActiveWindow(apex_hwnd)
            win32gui.ShowWindow(apex_hwnd, win32con.SW_RESTORE)
            end_time = time.time()
            time_lapsed = end_time - start_time
            pyautogui.moveTo(200,100)
            window_found = 1
            
        if pyautogui.locateOnScreen(resource_path('ss\\InGame.png'), region=(255, 885, 172, 81), grayscale=True, confidence=0.5) is not None:
            print(UP, end=CLEAR)
            print("------------------------------DETECTED IN MATCH, MOVING TO FARMING MODE-----------------------------")
            time_stuck_start= 0
            mod = 3

        if pyautogui.locateOnScreen(resource_path('ss\\gameopen.png'), grayscale=True, confidence=0.7) != None:
            pyautogui.click(956, 647)
            time.sleep(np.random.uniform(0.3,0.8))
            pyautogui.click(956, 647)     

        if pyautogui.locateOnScreen(resource_path('ss\\news.png'), grayscale=True, confidence=0.6) != None:
            keyboard.press_and_release('esc')
            
        if pyautogui.locateOnScreen(resource_path('ss\\space2.png'), grayscale=True, confidence=0.6) != None:
            keyboard.press_and_release('esc')

        if pyautogui.locateOnScreen(resource_path('ss\\space2.png'), region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
            keyboard.press_and_release('space')
            time.sleep(np.random.uniform(0.4,0.8))

        if pyautogui.locateOnScreen(resource_path('ss\\back.png'), grayscale=True, confidence=0.6) != None:
            time.sleep(np.random.uniform(0.3,0.8))
            keyboard.press_and_release('esc')

        if pyautogui.locateOnScreen(resource_path('ss\\team.png'), region=(team_coords), grayscale=True, confidence=0.9) != None:
            apex_hwnd = win32gui.FindWindow(None,'Apex Legends')
            if apex_hwnd != 0:
                time.sleep(1)
                pyautogui.press("alt")
                win32gui.SetForegroundWindow(apex_hwnd)
                win32gui.SetActiveWindow(apex_hwnd)
                try:
                    coords_auto_fill_x, coords_auto_fill_y = pyautogui.locateCenterOnScreen(resource_path('ss\\team.png'),region=(team_coords),confidence=0.9)
                except TypeError:
                    x=0
                    y=0
                if (coords_auto_fill_x!=0) and (coords_auto_fill_y!=0):
                    pyautogui.moveTo(coords_auto_fill_x,coords_auto_fill_y)
                    pyautogui.click(coords_auto_fill_x,coords_auto_fill_y)
                    time.sleep(2)
                    pyautogui.moveTo(200,100)
        if (pyautogui.locateOnScreen(resource_path('ss\\team.png'), region=(team_coords), grayscale=True, confidence=0.9) is None) and (pyautogui.locateOnScreen(resource_path('ss\\notready.png'), region=(0,538,447,528), grayscale=True, confidence=0.7) != None):
            time.sleep(1)
            print(UP, end=CLEAR)
            print ('-------------------------------------------READY TO FARM-------------------------------------------')
            if pyautogui.locateOnScreen(resource_path('ss\\team.png'), region=(team_coords), grayscale=True, confidence=0.9) is None:            
                #print('---------------Fill not checked-----------------')
                #print(UP, end=CLEAR)
                time.sleep(2)
                pyautogui.moveTo(200,100)
                mod = 5
    
    #program loop
    while mod == 3:
        if pyautogui.locateOnScreen(resource_path('ss\\team.png'), region=(team_coords), grayscale=True, confidence=0.9) != None:
                try:
                    coords_auto_fill_x, coords_auto_fill_y = pyautogui.locateCenterOnScreen(resource_path('ss\\team.png'),region=(team_coords),confidence=0.9)
                except TypeError:
                    x=0
                    y=0
                time.sleep(0.5)
                pyautogui.press("alt")
                win32gui.SetForegroundWindow(apex_hwnd)
                win32gui.SetActiveWindow(apex_hwnd)
                if (coords_auto_fill_x!=0) and (coords_auto_fill_y!=0):
                    pyautogui.moveTo(coords_auto_fill_x,coords_auto_fill_y)
                    pyautogui.click(coords_auto_fill_x,coords_auto_fill_y)
                time.sleep(0.5)
                pyautogui.moveTo(200,100)
        elif pyautogui.locateOnScreen(resource_path('ss\\team.png'), region=(team_coords), grayscale=True, confidence=0.9) is None:                       
            end_time = time.time()
            time_lapsed = end_time - start_time
            end_time_absolute = time.time()
            time_lapsed_absolute = end_time_absolute - start_time_absolute
            
            #starting matchmaking
            if time_lapsed > timp:
                pyautogui.click(200, 100)
            elif (pyautogui.locateOnScreen(resource_path('ss\\notready.png'), region=(0,856,482,209), confidence=0.5) != None) and (time_lapsed < timp):
                pyautogui.moveTo(230,950)
                pyautogui.click(230,950)
                time.sleep(np.random.uniform(0.3,0.8))
                pyautogui.moveTo(200,100)
                time.sleep(0.1)
            
            if (pyautogui.locateOnScreen(resource_path('ss\\matchmaking.png'), region=(0,856,482,209), confidence=0.5) != None) and (matchmaking == 0):
                matchmaking=1
                timer_matchmaking_start=time.time()
            while matchmaking==1:
                #print(timer_matchmaking)
                timer_matchmaking_end=time.time()
                time.sleep(0.05)
                timer_matchmaking=timer_matchmaking_end-timer_matchmaking_start
                if (pyautogui.locateOnScreen(resource_path('ss\\matchmaking.png'), region=(0,856,482,209), confidence=0.5) != None) and (timer_matchmaking>240):
                    pyautogui.moveTo(230,950)
                    pyautogui.click(230,950)
                    time.sleep(np.random.uniform(0.3,0.8))
                    pyautogui.moveTo(200,100)
                    time.sleep(0.1)
                    matchmaking=0
                    timer_matchmaking=0
                    break
                elif pyautogui.locateOnScreen(resource_path('ss\\matchmaking.png'), region=(0,856,482,209), confidence=0.5) != None:
                    time.sleep(1)

                elif pyautogui.locateOnScreen(resource_path('ss\\matchmaking.png'), region=(0,856,482,209), confidence=0.5) is None:
                    matchmaking=0
                    timer_matchmaking=0
                    break
            if pyautogui.locateOnScreen(resource_path('ss\\champselect.png'), region=(494,794,253,42), confidence=0.9) != None:
                if champion not in champ_list:
                    pass
                else:
                    try:
                        x, y = pyautogui.locateCenterOnScreen(resource_path(champ_string),region=(246,695,1357,294),confidence=0.9)
                    except TypeError:
                        x=0
                        y=0
                    if x==0 and y==0:
                        pass
                    else:
                        pyautogui.click(x,y)
                        pyautogui.click(x,y)
                        time.sleep(0.2)
                        pyautogui.click(x,y)
                        time.sleep(5)
            
            if pyautogui.locateOnScreen(resource_path('ss\\space2.png'), region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
                #print("space2.png")
                keyboard.press_and_release('space')
                time.sleep(np.random.uniform(0.4,0.8))
            
            if pyautogui.locateOnScreen(resource_path('ss\\InGame.png'), region=(255, 885, 172, 81), grayscale=True, confidence=0.5) is not None:
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
                time.sleep(np.random.uniform(0.3,0.5))
                keyboard.press_and_release('space')
                time.sleep(np.random.uniform(0.3,0.7))
                while True:
                    if pyautogui.locateOnScreen(resource_path('ss\\yes.png'), region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
                        #print('yes')
                        pyautogui.click(850, 713)
                        time.sleep(np.random.uniform(0.4,0.8))
                        pyautogui.click(850, 713)
                        time.sleep(0.5)
                    if pyautogui.locateOnScreen(resource_path('ss\\battlepass.png'), region=(51,987,122,41), grayscale=True, confidence=0.8) != None:
                            #print('space2')
                            keyboard.press_and_release('space')
                            time.sleep(0.5)
                    if pyautogui.locateOnScreen(resource_path('ss\\matchsummary.png'), region=(564,18,814,115), grayscale=True, confidence=0.8) != None:
                        #print('matchsummary')
                        keyboard.press_and_release('space')
                        time.sleep(0.5)
                        if pyautogui.locateOnScreen(resource_path('ss\\matchsummary.png'), region=(564,18,814,115), grayscale=True, confidence=0.8) is None:
                            while True:
                                if pyautogui.locateOnScreen(resource_path('ss\\expscreen.png'), region=(657,0,603,97), confidence=0.8) != None:
                                    #print('exp screen')
                                    time.sleep(5)
                                    if show_exp==1:
                                        image4=pyautogui.screenshot(region=(840,543,131,24))
                                        imagenp4 = np.array(image4)
                                        gray4 = cv2.cvtColor(imagenp4, cv2.COLOR_BGR2GRAY)
                                        invert4 = 255 - gray4
                                        boost_text=pytesseract.image_to_string(invert4,lang='eng', config='--psm 12 -c tessedit_char_whitelist=123456789BostAplied')
                                        res = any(ele in boost_text for ele in boost)
                                        if res is True:
                                            #print("coords boost")
                                            coords=coords_boost
                                        else:
                                            #print("coords no boost")
                                            coords=coords_no_boost
                                            
                                            
                                        image1=pyautogui.screenshot(region=(457,231,61,38))
                                        imagenp1 = np.array(image1)
                                        gray1 = cv2.cvtColor(imagenp1, cv2.COLOR_BGR2GRAY)
                                        invert1 = 255 - gray1
                                        
                                        image2=pyautogui.screenshot(region=(457,271,61,38))
                                        imagenp2 = np.array(image2)
                                        gray2 = cv2.cvtColor(imagenp2, cv2.COLOR_BGR2GRAY)
                                        invert2 = 255 - gray2
                                        
                                        image5=pyautogui.screenshot(region=(924,311,73,35))
                                        imagenp5 = np.array(image5)
                                        gray5 = cv2.cvtColor(imagenp5, cv2.COLOR_BGR2GRAY)
                                        invert5 = 255 - gray5
                                        
                                        image3=pyautogui.screenshot(region=(coords))
                                        imagenp3 = np.array(image3)
                                        gray3 = cv2.cvtColor(imagenp3, cv2.COLOR_BGR2GRAY)
                                        invert3 = 255 - gray3
                                        
                                        if OCR_debug == 1:
                                            pyautogui.screenshot("saved_without_exp"+str(n)+".png")
                                        try:
                                            exp_new3 = int(pytesseract.image_to_string(invert3,lang='eng', config='--psm 6 -c tessedit_char_whitelist=0123456789'))
                                        except ValueError:
                                            exp_new3 = 0
                                            pass    
                                        
                                        exp_new1 = pytesseract.image_to_string(invert1,lang='eng', config='--psm 6 -c tessedit_char_whitelist=0123456789')
                                        exp_new2 = pytesseract.image_to_string(invert2,lang='eng', config='--psm 6 -c tessedit_char_whitelist=0123456789')
                                        exp_new4 = pytesseract.image_to_string(invert5,lang='eng', config='--psm 6 -c tessedit_char_whitelist=0123456789')
                                            
                                        if len(exp_new1) == 6 and exp_new1[0] == '4':
                                            exp_new1=int(exp_new1[1:])
                                            #print('EXP1 - 5 CHAR DETECTED')
                                        if len(exp_new2) == 6 and int(exp_new2[0]) == '4':
                                            exp_new2=int(exp_new2[1:])
                                            #print('EXP2 - 5 CHAR DETECTED')
                                        if len(exp_new4) == 4 and int(exp_new4[0]) == '4':
                                            exp_new4=int(exp_new4[1:])
                                            #print('EXP2 - 5 CHAR DETECTED')
                                            
                                        try:
                                            exp_new1 = int(exp_new1)
                                        except ValueError:
                                            exp_new1 = 0
                                        
                                        try:
                                            exp_new2 = int(exp_new2)
                                        except ValueError:
                                            exp_new2 = 0
                                            
                                        try:
                                            exp_new4 = int(exp_new4)
                                        except ValueError:
                                            exp_new4 = 0
                                            
                                        exp_new=exp_new1+exp_new2+exp_new4
                                        exp_new=str(exp_new) 
                                        
                                        if exp_new[0]=='4' and exp_new[1]=='4' and len(exp_new)==4:
                                            exp_new=exp_new[1:]
                                        
                                        exp_new = int(exp_new)
                                        
                                        if exp_new == exp_new3:
                                            pass
                                        if exp_new > 4000:
                                            exp_new=exp_new3
                                        elif len(str(exp_new))==3 and len(str(exp_new3))==4:
                                            exp_new=exp_new3
                                        
                                        if exp_new==0:
                                            exp_read=exp_read+1
                                        
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
                xp_hour=(exp*3600)/time_lapsed_absolute
                print(UP, end=CLEAR)
                print(UP, end=CLEAR)
                print(UP, end=CLEAR)
                print(UP, end=CLEAR)
                print("            ___________________   ")
                print ('           | TOTAL TIME FARMED | -> |',' | TOTAL EXP:', exp," | XP/HOUR:",round(xp_hour)," | ",datetime.timedelta(seconds=round(time_lapsed_absolute)),"| ",)
                print ('           |    RESTART TIME   | -> |',' |  NEW EXP:',exp_new," | ",datetime.timedelta(seconds=round(time_lapsed))," / ", datetime.timedelta(seconds=round(timp)),"| ", "NO EXP:", exp_read)
                print("            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  ")
            else:
                print(UP, end=CLEAR)
                print(UP, end=CLEAR)
                print(UP, end=CLEAR)
                print(UP, end=CLEAR)
                print("            ___________________   ")
                print ('           | TOTAL TIME FARMED | -> |'," | ",datetime.timedelta(seconds=round(time_lapsed_absolute)),"| ",)
                print ('           |    RESTART TIME   | -> |'," | ",datetime.timedelta(seconds=round(time_lapsed))," / ", datetime.timedelta(seconds=round(timp)),"| ")
                print("            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  ")        
            #checking if time lapsed is more than set time and checking if it's in game
            if (time_lapsed > timp-600) and (ingame == 0):
                time.sleep (15)
                mod = 4
            if pyautogui.locateOnScreen(resource_path('ss\\afk.png'), region=(588,265,776,536), grayscale=True, confidence=0.8) != None: 
                #print ('---------- DETECTED AFK, PROCEEDING TO REINITIALIZE -------------')
                pyautogui.click(960, 719)
                time.sleep(np.random.uniform(0.3,0.7))
                pyautogui.click(960, 719)
                window_found = 0
                mod = 2
                
            if process_exists('r5apex.exe'):
                pass
            else: 
                print(UP, end=CLEAR)
                print(UP, end=CLEAR)
                print(UP, end=CLEAR)
                print(UP, end=CLEAR)
                print('')
                print ('---------------------- APEX IS NOT RUNNING, WHAT DO YOU WANT TO DO? ----------------------')
                print ('--- STOP - TYPE 1 /// RESTART - TYPE 2 // OR WITHIN 30 SEC RESTART WITH EXISTING STATS ---')
                while True:

                    try:
                        data_input = inputimeout(prompt='------------------------------------- SELECT OPTION: -------------------------------------\n', timeout=30)
                    except TimeoutOccurred:
                        print(UP, end=CLEAR)
                        print(UP, end=CLEAR)
                        data_input = ''
                        mod=1
                        break
                    if data_input == '1':
                        xp_hour=(exp*3600)/time_lapsed_absolute
                        print(UP, end=CLEAR)
                        print(UP, end=CLEAR)
                        print(UP, end=CLEAR)
                        print(UP, end=CLEAR)
                        print("               ____________   ")
                        print ('              | FARM STATS |')
                        print("               ‾‾‾‾‾‾‾‾‾‾‾‾  ")
                        if show_exp==1:
                            print("            ___________________   ")
                            print ('           |  TOTAL XP GAINED  | -> | ', exp," | XP/HOUR:",round(xp_hour), " | NO EXP:", exp_read)
                            print ('           | TOTAL TIME FARMED | -> | ',datetime.timedelta(seconds=round(time_lapsed_absolute)))
                            print("            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  ")
                            time.sleep(15)
                            sys.exit()
                        else:
                            print("            ___________________   ")
                            print ('           |  TOTAL XP GAINED  | -> | N/A')
                            print ('           | TOTAL TIME FARMED | -> | ',datetime.timedelta(seconds=round(time_lapsed_absolute)))
                            print("            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  ")
                            time.sleep(15)
                            sys.exit()
                    elif data_input == '2':
                        print(UP, end=CLEAR)
                        print(UP, end=CLEAR)
                        print(UP, end=CLEAR)
                        print(UP, end=CLEAR)
                        print ('')
                        print ('')
                        print ('')
                        print ('---------- PROGRAM RESTART -------------')
                        time.sleep(1)
                        mod = 1
                        exp=0
                        exp_new=0
                        exp_new1=0
                        exp_new2=0
                        exp_read=0
                        break
                    else:
                        print ('You have made an invalid choice, try again.')
                        time.sleep(1)
                        print(UP, end=CLEAR)
            
#checking if apex is running 

    if mod == 4:
        os.system('taskkill /f /im r5apex.exe')
        time.sleep(5)
        print(UP, end=CLEAR)
        time.sleep(10)
        mod = 1
        
    while mod==5:
        if leader=='FALSE':
            mod=3
            break
        if leader=='TRUE':
            pyautogui.click(200,100)
            pyautogui.click(200,100)
            if (time_slept==0) and (apex_detected==0):
                time.sleep(45)
                time_slept=1
            time.sleep(3)
                
            if pyautogui.locateOnScreen(resource_path('ss\\friendlist.png'),region=(1483,942,461,101),confidence=0.9) != None:
                try:
                    friendlist1_coords, friendlist2_coords = pyautogui.locateCenterOnScreen(resource_path('ss\\friendlist.png'),region=(1483,942,461,101),confidence=0.9)
                except TypeError:
                    friendlist1_coords=0
                    friendlist2_coords=0
                if (friendlist1_coords!=0) and (friendlist2_coords!=0):
                    pyautogui.moveTo(friendlist1_coords,friendlist2_coords)
                    pyautogui.click(friendlist1_coords,friendlist2_coords)
                    time.sleep(2)
            if pyautogui.locateOnScreen(resource_path('ss\\friends_window.png'),region=(774,32,385,83),confidence=0.9) != None:
                    friendlist_window=1    
                    while True:
                    
                        if (friend1 != 'None') and (friend1_not_invited==1) and (friendlist_window==1):
                            time.sleep(1)
                                    
                            if friend1 not in invite1:
                                who_invite=pyautogui.screenshot(region=friend_region[k])
                                who_invite_np = np.array(who_invite)
                                gray_who_invite = cv2.cvtColor(who_invite_np, cv2.COLOR_BGR2GRAY)
                                invert_who_invite = 255 - gray_who_invite
                                invite1 = pytesseract.image_to_string(invert_who_invite,lang='eng', config='--psm 7')
                                time.sleep(1)
                            if (friend1 in invite1) and (friend1_not_invited==1):
                                try:
                                    f1_coords, f2_coords = pyautogui.locateCenterOnScreen(resource_path('ss\\invite.png'),region=(invite_region[k]),confidence=0.9)
                                except TypeError:
                                    f1_coords=0
                                    f2_coords=0
                                if (f1_coords!=0) and (f2_coords!=0):
                                    pyautogui.moveTo(f1_coords,f2_coords)
                                    pyautogui.click(f1_coords,f2_coords)
                                    friend1_not_invited=0
                                    if friend2 =='None':
                                        friend2_not_invited=0
                                    time.sleep(0.5)
                                    
                                
                        if (friend2 != 'None') and (friend2_not_invited==1) and (friendlist_window==1):
                            time.sleep(1)
                                  
                            if friend2 not in invite2:
                                who_invite=pyautogui.screenshot(region=friend_region[k])
                                who_invite_np = np.array(who_invite)
                                gray_who_invite = cv2.cvtColor(who_invite_np, cv2.COLOR_BGR2GRAY)
                                invert_who_invite = 255 - gray_who_invite
                                invite2 = pytesseract.image_to_string(invert_who_invite,lang='eng', config='--psm 7')
                                time.sleep(0.5)
                            if (friend2 in invite2) and (friend2_not_invited==1):
                                try:
                                    f1_coords, f2_coords = pyautogui.locateCenterOnScreen(resource_path('ss\\invite.png'),region=(invite_region[k]),confidence=0.9)
                                except TypeError:
                                    f1_coords=0
                                    f2_coords=0
                                if (f1_coords!=0) and (f2_coords!=0):
                                    pyautogui.moveTo(f1_coords,f2_coords)
                                    pyautogui.click(f1_coords,f2_coords)
                                    friend2_not_invited=0
                                    time.sleep(0.5)
                                   
                        
                        if k==6:
                            k=0
                        else:
                            k=k+1
                
                        if (friend1_not_invited==0) and (friend2_not_invited==0):
                            keyboard.press_and_release('esc')
                            friendlist_window=0
                            k=0
                        time.sleep(2)
                        '''if pyautogui.locateOnScreen(resource_path('ss\\friendlist.png'),region=(1483,942,461,101),confidence=0.9) != None:
                            who_invited=pyautogui.screenshot(region=(492,163,209,27))
                            who_invited_np = np.array(who_invited)
                            gray_who_invited = cv2.cvtColor(who_invited_np, cv2.COLOR_BGR2GRAY)
                            invert_who_invited = 255 - gray_who_invited
                            invited1 = pytesseract.image_to_string(invert_who_invited,lang='eng', config='--psm 7')
                            time.sleep(0.5)            
                            if (friend1 in invited1) and (friend1 != 'None'):
                                friend1_invited=1
                                if friend2=='None':
                                    friend2_invited==1
                                    
                            who_invited=pyautogui.screenshot(region=(1187,147,244,95))
                            who_invited_np = np.array(who_invited)
                            gray_who_invited = cv2.cvtColor(who_invited_np, cv2.COLOR_BGR2GRAY)
                            invert_who_invited = 255 - gray_who_invited
                            invited2 = pytesseract.image_to_string(invert_who_invited,lang='eng', config='--psm 7')
                            time.sleep(0.5)
                            if friend2 in invited2:
                                friend2_invited=1
                                
                        if (friend1_invited==1) and (friend2_invited==1):
                            mod=3
                            time.sleep(0.5)
                        else:
                            friend1_not_invited=1
                            friend2_not_invited=1
                            invite1='0'
                            invite2='0'
                            time.sleep(3)'''
                        if pyautogui.locateOnScreen(resource_path('ss\\slave.png'), region=(398,140,334,71), confidence=0.8) != None:  
                            if (friend1 != 'None') and (friend2 == 'None'):
                                mod=3
                                friend1_not_invited=1
                                friend2_not_invited=1
                                invite1='0'
                                invite2='0'
                                time.sleep(3)
                                break
                            if (friend1 != 'None') and (friend2!='None'):
                                if pyautogui.locateOnScreen(resource_path('ss\\slave.png'), region=(1187,147,244,95), confidence=0.8) != None:
                                    mod=3
                                    break
                        else:
                            friend1_not_invited=1
                            friend2_not_invited=1
                            invite1='0'
                            invite2='0'
                            time.sleep(10)
                            break

                                   
        if leader=='SLAVE':
            time.sleep(5)
            if (friend1 not in leader_text) and (friend1 != None):
                leader_photo=pyautogui.screenshot(region=(1572,927,324,20))
                leader_photo_np = np.array(leader_photo)
                gray_leader_photo = cv2.cvtColor(leader_photo_np, cv2.COLOR_BGR2GRAY)
                invert_leader_photo = 255 - gray_leader_photo
                leader_text = pytesseract.image_to_string(invert_leader_photo,lang='eng', config='--psm 7')
                time.sleep(0.5)
            if (friend1 in leader_text) and (friend1 != 'None'):
                try:
                    f1_coords, f2_coords = pyautogui.locateCenterOnScreen(resource_path('ss\\accept.png'),region=(1812,970,90,42),confidence=0.9)
                except TypeError:
                    f1_coords=0
                    f2_coords=0
                if (f1_coords!=0) and (f2_coords!=0):
                    pyautogui.click(200,100)
                    pyautogui.moveTo(f1_coords,f2_coords)
                    pyautogui.click(f1_coords,f2_coords)
                    time.sleep(0.5)

            '''who_invited=pyautogui.screenshot(region=(492,163,209,27))
            who_invited_np = np.array(who_invited)
            gray_who_invited = cv2.cvtColor(who_invited_np, cv2.COLOR_BGR2GRAY)
            invert_who_invited = 255 - gray_who_invited
            invited1 = pytesseract.image_to_string(invert_who_invited,lang='eng', config='--psm 7')
            who_invited=pyautogui.screenshot(region=(1187,147,244,95))
            who_invited_np = np.array(who_invited)
            gray_who_invited = cv2.cvtColor(who_invited_np, cv2.COLOR_BGR2GRAY)
            invert_who_invited = 255 - gray_who_invited
            invited2 = pytesseract.image_to_string(invert_who_invited,lang='eng', config='--psm 7')
            time.sleep(0.5)            
            print(invited1)
            print(invited2)
            
            if (friend1 in invited1) or (friend1 in invite2):
                invite_accepted=1
                mod=3
                break
            else:
                leader_text='0'
                break'''
            if (pyautogui.locateOnScreen(resource_path('ss\\leader.png'), region=(398,140,334,71), confidence=0.8) != None) or (pyautogui.locateOnScreen(resource_path('ss\\leader.png'), region=(1187,147,244,95), confidence=0.8) != None):
                mod=3
                            
                                    
            
                
                
                
            
        
        
        
