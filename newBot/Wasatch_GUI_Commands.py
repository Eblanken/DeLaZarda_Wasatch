#
# TODO: Fill in remaining commands
#
# File: WasatchInterface_MicroscopeSettings
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/12/2018
#
# Description:
#
# These methods allow for direct manipulation of the Wasatch GUI
#

#---------------------- Included Libraries -------------------------------------
import pyautogui
import time
import numpy as np

#--------------------------- Constants -----------------------------------------
DELAY_STARTUP = 10
DELAY_TIMEOUT = 10

KEY_OPENICONBAR = 'win' # Press this key to expose the menu bar
DELAY_OPENICONMENUBAR = 1 # Windows has an animation for the bar

# Various images that correspond to each menu item
# for pyautogui to try to find.

# Desktop icon for the app
IMGS_MAIN_ICON  = { # TODO fill in these images

}

# Target for minimized app in the taskbar
IMGS_MAIN_ICONBAR  = { # TODO fill in these images

}

# Live button in the OCT App
IMGS_MAIN_WINDOW_BLIVE = { # TODO fill in these images

}

# Stop button in the OCT App
IMGS_MAIN_WINDOW_BSTOP = { # TODO fill in these images

}

# Update button in the OCT App
IMGS_MAIN_WINDOW_BUPDATE = { # TODO fill in these images

}

# Advanced menu tab in the OCT App
IMGS_MAIN_WINDOW_TADVANCED = { # TODO fill in these images

}

# Setupmode sub-menu tab in the OCT App
IMGS_MAIN_WINDOW_TADVANCED_SETUPMODE = { # TODO fill in these images

}

# OCT Image tab in the app
IMGS_MAIN_WINDOW_TOCTIMAGE = { # TODO fill in these images

}

# OCT Volume tab in the app
IMGS_MAIN_WINDOW_TOCTVOLUME = { # TODO fill in these images

}

# Sub-Window for setup / serial exposed in the taskbar
IMGS_SERIAL_ICONBAR = {
    'pngs/serialFocus1.png',
    'pngs/serialFocus2.png',
    'pngs/serialFocus3.png',
    'pngs/serialFocus4.png',
    'pngs/serialFocus5.png'
}

# Serial prompt in the serial window
IMGS_SERIAL_PROMPT = {
    'pngs/serialPrompt1.png',
    'pngs/serialPrompt2.png',
    'pngs/serialPrompt3.png',
    'pngs/serialPrompt4.png'
}

#--------------------- Function Definitions ------------------------------------

#--------- General Commands

# Wrapper for autoguiFunction
def WProgram_TypeString(command):
    pyautogui.typewrite(command)

# Wrapper for autoguiFunction
def WProgram_TypePress(key):
    pyautogui.press('enter')

def WProgram_FindAndPressIcon(imageDirectoryList, numTimes):
    timeout = time.time() + DELAY_TIMEOUT
    while True:
        for image in imageDirectoryList:
            r = pyautogui.locateOnScreen(image,grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                for press in range(0, numTimes):
                    pyautogui.click(homex,homey)
                return True
        if time.time() > timeout:
            print("Failed to find the input box in setup.");
            return False

#--------- Startup Commands

#
# Returns true if the spark OCT program was initialized, false otherwise.
#
def WProgram_Start():
    print("Trying to start Spark OCT.")
    if WProgram_FindAndPressIcon(IMGS_MAIN_ICON, 2):
        time.sleep(DELAY_STARTUP)
        return True
    else:
        print("Failed to launch Spark OCT.")

#
# TODO finish WProgram_StartSerial
#
def WProgram_StartSerial():
    raise NotImplimentedError("Not Implimented")

#
# Returns true if the sparkOCT GUI window was found, otherwise false
#
def WProgram_FocusOCTWin():
    pyautogui.moveTo(697, 1080)
    pyautogui.moveTo(697, 1078)
    pyautogui.moveTo(697, 1074)
    r = None
    timeout = time.time() + DELAY_TIMEOUT
    while r is None:
            x,y=np.random.randint(5,size=2)
            pyautogui.moveTo(684+x, 1076+y)
            r = pyautogui.locateOnScreen('pngs/sparkoct.png',grayscale=False)
            if r is not None:
                homex,homey = pyautogui.center(r)
                pyautogui.click(homex,homey)
                return True
            if time.time() > timeout:
                print("Failed to find the Spark OCT window.");
                return False;

#--------- 2d Window Commands

#--------- Volumetric window commands

#--------- Serial window input commands

#
# returns true if the window was found, false otherwise
#
def WProgram_FocusSerialWin():
    pyautogui.moveTo(697, 1074)
    print("Searching for the serial window.")
    if WProgram_FindAndPressIcon(IMGS_MAIN_ICONBAR, 1) and WProgram_FindAndPressIcon(IMGS_SERIAL_ICONBAR, 1):
        return True
    else:
        print("Failed to find the serial window.")

#
# Returns true if the setup window input prompt was found, otherwise false
#
def WProgram_CenterSerialPrompt():
    print("Searching for the serial prompt.")
    if WProgram_FindAndPressIcon(IMGS_SERIAL_PROMPT, 1):
        return True
    else:
        print("Failed to find the serial prompt.")
