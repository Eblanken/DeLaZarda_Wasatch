#----------------------- Imported Libraries ------------------------------------

import pyautogui
import time
import numpy as np

#---------------------------- Constants ----------------------------------------

CONST_DELAYTIMEOUTOUT = 5

#---------------------- Function Definitions -----------------------------------

#
# returns true if the window was found, false otherwise
#
def findsetupwin():
    pyautogui.moveTo(697, 1074)
    r = None
    timeout = time.time() + CONST_DELAYTIMEOUT
    while r is None:
            x,y=np.random.randint(5,size=2)
            pyautogui.moveTo(684+x, 1076+y)
            r = pyautogui.locateOnScreen('pngs/setupwindow5.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                return True
            r = pyautogui.locateOnScreen('pngs/setupwin6.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                return True
            if time.time() > timeout:
                printf("Failed to find the setup window.");
                return False

#
# Returns true if the setup window input prompt was found, otherwise false
#
def setupinput():
    print("Search for inputbox...")
    r =None
    timeout = time.time() + CONST_DELAYTIMEOUT
    while r is None:
            r = pyautogui.locateOnScreen('pngs/setupinput.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                return True
            r = pyautogui.locateOnScreen('pngs/setupinput2.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                return True
            r = pyautogui.locateOnScreen('pngs/setupinput3.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                return True
            r = pyautogui.locateOnScreen('pngs/setupinput4.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                return True
            if time.time() > timeout
                printf("Failed to find the input box in setup.");
                return False

#
# Returns true if the sparkOCT GUI window was found, otherwise false
#
def findsparkoctwin():
    pyautogui.moveTo(697, 1080)
    pyautogui.moveTo(697, 1078)
    pyautogui.moveTo(697, 1074)
    r = None
    timeout = time.time() + CONST_DELAYTIMEOUT
    while r is None:
            x,y=np.random.randint(5,size=2)
            pyautogui.moveTo(684+x, 1076+y)
            r = pyautogui.locateOnScreen('pngs/sparkoct.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                return true
            if time.time() > timeout:
                printf("Failed to find the Spark OCT window.");
                return false;

#
# Clicks the update button on the sparkOCT GUI menu.
#
# Returns true if succesful, false otherwise.
#
def clickupdate():
    r =None
    timeout = time.time() + CONST_DELAYTIMEOUT
    while r is None:
            r = pyautogui.locateOnScreen('pngs/update.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                return true
            if time.time() > timeout:
                printf("Failed to find the update button.");
                return False

#
# Brings up the image tab in the SparkOCT GUI menu.
#
# Returns true if succesful, false otherwise.
#
def findimagetab():

    r =None
    timeout = time.time() + CONST_DELAYTIMEOUT
    while r is None:
            r = pyautogui.locateOnScreen('pngs/OCTImage.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                return True;
            r = pyautogui.locateOnScreen('pngs/OCTImage2.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                return True;
            if time.time() > timeout:
                printf("Failed to find the image tab.");
                return false

#
# Presses the stop button after a delay 'delayTime'.
#
# Returns true if the button was pressed on time,
# returns false if a failure occurred.
#
def pressStop(delayTime):
    r = None
    if delayTime == None:
        delayTime = 0
    timeout = time.time() + CONST_DELAYTIMEOUT
    timeStop = time.time() + delayTime;
    while r is None:
            r = pyautogui.locateOnScreen('pngs/stop.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                printf("Ready to stop.")
                while(time.time() < timeStop)
                pyautogui.click(homex,homey)
                return True
            if time.time() > timeout:
                return False

#
# Finds and presses the live display button
#
# Returns true if the button was found and pressed,
# returns false otherwise.
#
def findlive():
    r = None
    timeout = time.time() + CONST_DELAYTIMEOUT
    while r is None:
            r = pyautogui.locateOnScreen('pngs/live.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                return True
            if time.time() > timeout:
                return False

#
# Finds and presses the octVolume setting button.
#
# Returns true if the button was found and pressed,
# returns false otherwise.
#
def findoctvolumetab():
    r = None
    timeout = time.time() + CONST_DELAYTIMEOUT
    while r is None:
            r = pyautogui.locateOnScreen('pngs/octvolume1.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                return True;
            r = pyautogui.locateOnScreen('pngs/octvolume2.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                pyautogui.click(homex,homey)
                return False;
            if time.time() > timeout:
                return False
