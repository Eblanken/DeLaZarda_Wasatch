
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pyautogui
import os
import lackey as lk
import time
import numpy as np


from tools import*
from config import*
from searchfuncs import*
from wrapperfuncs import*

os.chdir('C:/Users/WP OCT User/Desktop/Sikuli')
print("\n"*100)

screenWidth, screenHeight = pyautogui.size()

#
#findsetupwin()
#setupinput()
#
#str = convertinputtostr(1,4,5,5)
#pyautogui.typewrite(str)
#pyautogui.press('enter')


#Initialize--------------------------------------
findsparkoctwin()
findimagetab()
findstop(2)

count=1

#Photobleach1--------------------------------------
print("line{}".format(count))

orientation='hor'
position=[2,4.5]  #a single x,y coordinate, the lower right corner of the box
length= 5          # length in mm's
thickness= 1       # length in mm's
waittime= 0.2           # time in minutes
photobleachandwait(orientation,position,length,thickness,waittime)

count+=1
print("---------------------------------")

#Photobleach1--------------------------------------
print("line{}".format(count))
orientation='vert'
position=[1,4.5]  #a single x,y coordinate, the lower right corner of the box
length= 5          # length in mm's
thickness= 0.2       # length in mm's
waittime= 0.2            # time in minutes
photobleachandwait(orientation,position,length,thickness,waittime)

count+=1
print("---------------------------------")


#Stop--------------------------------------
findsparkoctwin()
findimagetab()
findstop()
time.sleep(2)
findstop()


























#
##click live
#r =None
#while r is None:
#        timeout = time.time() + 5
#        r = pyautogui.locateOnScreen('pngs/live.png',grayscale=False)
#        if r is not None:
#            homex,homey = pyautogui.center(r)
#            pyautogui.click(homex,homey)
#            break
#        if time.time()>timeout:
#            break
#lk.click('pngs/Sikulitab.png')
#
#pyautogui.keyUp('Alt')
#pyautogui.keyUp('Tab')
