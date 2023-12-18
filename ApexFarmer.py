import msvcrt

print("Press any key to continue...")
msvcrt.getch()
print("Continuing...")

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import subprocess
import os
import numpy as np
import pygetwindow as gw

#EDIT HERE----------------------------------
timp = 10800 #after how many hours you want to restart game / 3600s = 1 hours
apexdir = 'C:\Program Files\EA Games\Apex\\r5apex.exe' #set your apex directory here
#EDIT HERE----------------------------------

Random = ['a','w','s','d','4','q','1','2','3','4'] #don't touch
time.sleep(5)

#checking if apex is running
def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False

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
        mod = 2

    #checkking if game was opened and closing news or other in game windows
    while mod == 2:
        print ('----------Checking if game is opened and getting into main menu-------------')
        win = gw.getWindowsWithTitle('Apex Legends')[0]
        win.activate()
        end_time = time.time()
        time_lapsed = end_time - start_time
        pyautogui.moveTo(200,100)
        if pyautogui.locateOnScreen('ss\\InGame.png', region=(87, 755, 379, 304), grayscale=True, confidence=0.5) is not None:
            print("-------------In game detected, moving to mode farming--------------")
            mod = 3

        elif pyautogui.locateOnScreen('ss\\gameopen.png', grayscale=True, confidence=0.7) != None:
            pyautogui.click(956, 647)
            time.sleep(np.random.uniform(0.3,0.8))
            pyautogui.click(956, 647)     
            time.sleep(10)

        elif pyautogui.locateOnScreen('ss\\news.png', grayscale=True, confidence=0.6) != None:
            #print("news")
            keyboard.press_and_release('esc')
            
        elif pyautogui.locateOnScreen('ss\\continue2.png', grayscale=True, confidence=0.6) != None:
            #print("continue2")
            keyboard.press_and_release('esc')

        elif pyautogui.locateOnScreen('ss\\space.png', region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
            #print("space.png")
            keyboard.press_and_release('space')
            time.sleep(np.random.uniform(0.4,0.8))

        elif pyautogui.locateOnScreen('ss\\back.png', grayscale=True, confidence=0.6) != None:
            #print("back")
            time.sleep(np.random.uniform(0.3,0.8))
            keyboard.press_and_release('esc')

        elif pyautogui.locateOnScreen('ss\\team.png', confidence=0.9) != None:
            win = gw.getWindowsWithTitle('Apex')[0]
       	    win.activate()
            pyautogui.moveTo(119,582)
            pyautogui.click(119, 582)
            time.sleep(2)
            pyautogui.moveTo(200,100)
        elif (pyautogui.locateOnScreen('ss\\team.png', confidence=0.9) is None) and (pyautogui.locateOnScreen('ss\\notready.png', region=(0,538,447,528), grayscale=True, confidence=0.7) != None):
            time.sleep(1)
            print ('----------Apex window active and game started------------')
            if pyautogui.locateOnScreen('ss\\team.png', confidence=0.9) is None:
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
        
        #starting matchmaking
        if (pyautogui.locateOnScreen('ss\\notready.png', region=(0,538,447,528), grayscale=True, confidence=0.7) != None) and (time_lapsed < timp-600):
            time.sleep(0.5)
            pyautogui.click(230, 950)
            time.sleep(np.random.uniform(0.3,0.8))
            pyautogui.click(230, 950)     
            time.sleep(np.random.uniform(0.3,0.75))
            pyautogui.click(230, 950)
            time.sleep(np.random.uniform(0.5,1.1)) 
        elif time_lapsed > timp-600:
            pyautogui.click(200, 100)
        
        if pyautogui.locateOnScreen('ss\\space.png', region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
            #print("space.png")
            keyboard.press_and_release('space')
            time.sleep(np.random.uniform(0.4,0.8))
        
        if pyautogui.locateOnScreen('ss\\InGame.png', region=(87, 755, 379, 304), grayscale=True, confidence=0.5) is not None:
            print("-------------In game waiting--------------")
            keyboard.press_and_release(Random)
            time.sleep(0.5)
            ingame = 1
            if '4' in Random:
                time.sleep(np.random.uniform(5.5,6))
            else:
                time.sleep(np.random.uniform(0.6, 1.5)) 
        else: ingame = 0
    
        if pyautogui.locateOnScreen('ss\\dead.png', region=(441,19,1017,304), grayscale=True, confidence=0.6) != None:
            #print("dead")
            keyboard.press_and_release('space')
            time.sleep(np.random.uniform(1,2))
                
        if pyautogui.locateOnScreen('ss\\news.png', grayscale=True, confidence=0.6) != None:
            #print("news")
            keyboard.press_and_release('esc')
        
        if pyautogui.locateOnScreen('ss\\close.png', grayscale=True, confidence=0.6) != None:
            #print("close")
            keyboard.press_and_release('esc')        
        
     
        if pyautogui.locateOnScreen('ss\\yes.png', region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
            pyautogui.click(850, 713)
            time.sleep(np.random.uniform(0.4,0.8))
            pyautogui.click(850, 713)
        
        if pyautogui.locateOnScreen('ss\\space.png', region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
            #print("space.png")
            keyboard.press_and_release('space')
            time.sleep(np.random.uniform(0.4,0.8))
         
        if pyautogui.locateOnScreen('ss\\continue.png', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
            pyautogui.click(952, 717)
            time.sleep(np.random.uniform(0.4,0.7))
            pyautogui.click(952, 717)
        elif pyautogui.locateOnScreen('ss\\continue2.png', grayscale=True, confidence=0.6) != None:
            #print("continue2")
            keyboard.press_and_release('esc')
    
        if pyautogui.locateOnScreen('ss\\space2.png', region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
            #print("space2.png")
            keyboard.press_and_release('space')
            time.sleep(np.random.uniform(0.4,0.8))
    
        if pyautogui.locateOnScreen('ss\\startmenu.png', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
            pyautogui.click(952, 717)
            time.sleep(np.random.uniform(0.4,0.8))
            pyautogui.click(952, 717)
    
        if pyautogui.locateOnScreen('ss\\startmenu.png', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
            pyautogui.click(952, 717)
            time.sleep(np.random.uniform(0.3,0.7))
            pyautogui.click(952, 717)
        print ('----------Currently farming-------------')
        print ('---- time lapsed: ',round(time_lapsed),' seconds','-----','ingame:' ,ingame)
        #checking if time lapsed is more than set time and checking if it's in game
        if (time_lapsed > timp-600) and (ingame == 0):
            time.sleep (15)
            mod = 4

    if mod == 4:
        os.system('taskkill /f /im r5apex.exe')
        os.system('taskkill /f /im r5apex.exe')
        time.sleep(30)
        mod = 1
