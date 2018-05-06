# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:46:43 2018

@author: WP OCT User
"""

import time
from tools import*
from searchfuncs import*

def findsetupandinput(startx,endx,starty,endy):
    findsparkoctwin()
    findoctvolumetab()
    findsetupwin()
    setupinput()
    
    str = convertinputtostr(startx,endx,starty,endy)
    pyautogui.typewrite(str)
    pyautogui.press('enter')
    
def photobleachandwait(orientation,position,length,thickness,waittime):
    if orientation =='hor':
        startx = position[0] 
        endx = position[0] + length
        starty = position[1]
        endy = position[1] + thickness
    if orientation =='vert':
        startx = position[0] 
        endx = position[0] + thickness
        starty = position[1]
        endy = position[1] + length
    
    findsetupandinput(startx,endx,starty,endy)
    

    print("Photobleaching for %s minutes..." % str(waittime))
    clickupdate()
    time.sleep(waittime*60)
    print("Photobleaching done")
   

    