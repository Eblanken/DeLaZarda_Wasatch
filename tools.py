# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:58:50 2018

@author: WP OCT User
"""
import numpy as np
from config import *

def convertinputtostr(startx,endx,starty,endy):
    starty_ =  starty/MAX_LENGTH*(MAX_Y-MIN_Y)*1000 + MIN_Y
    endy_ =  endy/MAX_LENGTH*(MAX_Y-MIN_Y)*1000 + MIN_Y
    startx_ =  startx/MAX_LENGTH*(MAX_X-MIN_X)*1000 + MIN_X
    endx_ =  endx/MAX_LENGTH*(MAX_X-MIN_X)*1000 + MIN_X

    str = "xy_ramp {} {} {} {} 1".format(startx_, endx_, starty_,endy_)
    return(str)

def presstab(i):
    for i in range(i):
        pyautogui.press('tab')

def alttabcycle(i):
    pyautogui.keyDown('alt')
    presstab(i)
    pyautogui.keyUp('alt')
    pyautogui.press('tab')
