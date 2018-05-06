
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pyautogui
import os
import lackey as lk
import time

os.chdir('C:/Users/WP OCT User/Desktop/Sikuli')

screenWidth, screenHeight = pyautogui.size()

pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

def presstab(i):
    for i in range(i):
        pyautogui.press('tab')
        
def alttabcycle(i):        
    pyautogui.keyDown('alt')
    presstab(i)
    pyautogui.keyUp('alt')
    pyautogui.press('tab')


r=None
for tab in range(10):
    alttabcycle(tab+1)
    timeout = time.time() +  1
    while r is None:
        r = pyautogui.locateOnScreen('pngs/setupsend.png',grayscale=False)
        if r is not None:
            homex,homey = pyautogui.center(r)
            pyautogui.click(homex,homey)
            break
        r = pyautogui.locateOnScreen('pngs/setupsend2.png',grayscale=False)
        if r is not None:
            homex,homey = pyautogui.center(r)
            pyautogui.click(homex,homey)
            break
        if time.time()>timeout:
            break
    
    

#lk.click('pngs/Sikulitab.png')

pyautogui.keyUp('Alt')
pyautogui.keyUp('Tab')




