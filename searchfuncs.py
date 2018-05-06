# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:36:27 2018

@author: WP OCT User
"""
import pyautogui
import time
import numpy as np


def findsetupwin():
    print("Search for setupwindow...")
    pyautogui.moveTo(697, 1074) 
       
    r =None
    while r is None:
            timeout = time.time() + 5
            x,y=np.random.randint(5,size=2)
            pyautogui.moveTo(684+x, 1076+y) 
            r = pyautogui.locateOnScreen('pngs/setupwindow5.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                print("Found setup window")
                break
            r = pyautogui.locateOnScreen('pngs/setupwin6.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                print("Found setup window")
                break
            if time.time()>timeout:
                print("Could not find setupwindow!")
                break
        

def setupinput():
    print("Search for inputbox...")
    r =None
    while r is None:
            r = pyautogui.locateOnScreen('pngs/setupinput.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                print("Found inputbox")
                break
            r = pyautogui.locateOnScreen('pngs/setupinput2.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                print("Found inputbox")
                break
            r = pyautogui.locateOnScreen('pngs/setupinput3.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                print("Found inputbox")
                break
            r = pyautogui.locateOnScreen('pngs/setupinput4.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                print("Found inputbox")
                break


def findsparkoctwin():
            
    pyautogui.moveTo(697, 1080) 
    pyautogui.moveTo(697, 1078)  
    pyautogui.moveTo(697, 1074) 
            
    r =None
    while r is None:
            timeout = time.time() + 5
            x,y=np.random.randint(5,size=2)
            pyautogui.moveTo(684+x, 1076+y) 
            r = pyautogui.locateOnScreen('pngs/sparkoct.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                break
            if time.time()>timeout:
                break

def clickupdate():
        
    #click update
    r =None
    while r is None:
            timeout = time.time() + 5
            r = pyautogui.locateOnScreen('pngs/update.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                break
            if time.time()>timeout:
                break
            

def findimagetab():
            
    r =None
    while r is None:        
            r = pyautogui.locateOnScreen('pngs/OCTImage.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                break
            r = pyautogui.locateOnScreen('pngs/OCTImage2.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                break
        

def findstop(timeout=None):
            
    r =None
    if timeout == None:
        timeout = 100000
        
    while r is None:        
            r = pyautogui.locateOnScreen('pngs/stop.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                #pyautogui.click(homex,homey)
                #pyautogui.click(homex,homey)
                print("hitting stop")
                break
            if time.time()>timeout:
                break
    

def findlive():
            
    r =None
    while r is None:        
            r = pyautogui.locateOnScreen('pngs/live.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                break
        

def findoctvolumetab():
            
    r =None
    while r is None:        
            r = pyautogui.locateOnScreen('pngs/octvolume1.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                break
            r = pyautogui.locateOnScreen('pngs/octvolume2.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                break




















