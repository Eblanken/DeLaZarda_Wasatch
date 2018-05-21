#
# TODO GUI: Add more GUI commands, check startSerial, verify click order
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
ATTEMPTS = 5

DELAY_STARTUP = 10
DELAY_TIMEOUT = 10

KEY_OPENICONBAR = 'win' # Press this key to expose the menu bar
DELAY_OPENICONBAR = 2 # Windows has an animation for the bar

# Various images that correspond to each menu item
# for pyautogui to try to find.

# Desktop icon for the app
IMGS_MAIN_ICON  = {
    'pngs/mainIcon1.png'
}

# Target for minimized app in the taskbar
IMGS_MAIN_BARICON  = {
    'pngs/mainTaskbar1.png',
    'pngs/mainTaskbar2.png'
}

# Target for main window once exposed in the taskbar
IMGS_MAIN_BARFOCUS = {
    'pngs/mainFocus1.png',
    'pngs/mainFocus2.png'
}

# Main window is already open, might be not highlighted so definitely click
IMGS_MAIN_WINDOW_OPEN = {
    'pngs/mainOpen1.png'
    'pngs/mainOpen2.png'
    'pngs/mainOpen3.png'
    'pngs/mainOpen4.png'
}

# Live button in the OCT App
IMGS_MAIN_WINDOW_BLIVE = {
    'pngs/mainButtonLive1.png'
}

# Stop button in the OCT App
IMGS_MAIN_WINDOW_BSTOP = {
    'pngs/mainButtonStop1.png',
    'pngs/mainButtonStop2.png'
}

# Update button in the OCT App
IMGS_MAIN_WINDOW_BUPDATE = {
    'pngs/mainButtonUpdate1.png'
}

# Advanced menu tab in the OCT App
IMGS_MAIN_WINDOW_TADVANCED = {
    'pngs/mainTabAdvanced1.png'
}

# Setupmode sub-menu tab in the OCT App
IMGS_MAIN_WINDOW_TADVANCED_SETUPMODE = {
    'pngs/mainTabAdvancedOptionSetup1.png'
}

# OCT Image tab in the app is already open
IMGS_MAIN_WINDOW_TOCTIMAGE_OPEN = {
    'pngs/mainTabOCTImage1.png',
}

# OCT Image tab in the app not opened
IMGS_MAIN_WINDOW_TOCTIMAGE = {
    'pngs/mainTabOCTImage1.png',
    'pngs/mainTabOCTImage2.png',
    'pngs/mainTabOCTImage3.png'
}

# OCT image tab in the app already open, may not be highlighted so definitely click.
IMGS_MAIN_WINDOW_TOCTImage_OPEN = {
    'pngs/mainTabOCTImageOpen1.png'
}

# OCT Volume tab in the app not opened
IMGS_MAIN_WINDOW_TOCTVOLUME = {
    'pngs/mainTabOCTVolume1.png'
    'pngs/mainTabOCTVolume2.png'
}

# OCT Volume tab in the app already open
IMGS_MAIN_WINDOW_TOCTVOLUME_OPEN = {
    'pngs/mainTabOCTVolumeOpen1.png'
    'pngs/mainTabOCTVolumeOpen2.png'
}

# Sub-Window for setup / serial exposed in the taskbar
IMGS_SERIAL_BARFOCUS = {
    'pngs/serialFocus1.png',
    'pngs/serialFocus2.png',
    'pngs/serialFocus3.png',
    'pngs/serialFocus4.png',
    'pngs/serialFocus5.png'
}

# Serial window already opened
IMG_SERIAL_WINDOW_OPEN = {
    'pngs/serialOpen1.png'
    'pngs/serialOpen2.png'
    'pngs/serialOpen3.png'
}

# Serial prompt in the serial window
IMGS_SERIAL_WINDOW_PROMPT = {
    'pngs/serialPrompt1.png',
    'pngs/serialPrompt2.png',
    'pngs/serialPrompt3.png',
    'pngs/serialPrompt4.png'
}

#--------------------- Function Definitions ------------------------------------

#--------- General Commands

#
# Wrapper for autoguiFunction
#
# Types string command and then waits
# for 'delay' seconds.
#
def WProgram_TypeString(command, delaySeconds = 0):
    pyautogui.typewrite(command)
    time.Sleep(delay)
    return True

#
# Wrapper for autoguiFunction
#
# Presses key 'key' and then waits
# for 'delay' seconds.
#
def WProgram_TypePress(key, delaySeconds = 0):
    pyautogui.press('enter')
    time.Sleep(delay)
    return True

#
# Executes the given schedule of tasks in reverse order. This means
# that starting from the last entry it will attempt all functions
# and once one returns true will move back up, trying each one for
# 'ATTEMPTS' times.
#
# Returns true if succesful, false otherwise.
#
def WProgram_RunSchedule(schedule):
    # Finds the first succesful step to save time
    for startFunction in reversed(schedule):
        if(startFunction()):
            # Builds forwards from here
            for executingFunction in schedule[(schedule.indexof(startFunction) + 1):]:
                for attemptIndex in range(0, ATTEMPTS):
                    if(executingFunction()):
                        break
                else: # Ran out of attempts
                    return False
            return True # True if executing forward succeeds
    return False # False if all commands attempted


#
# Finds and presses any icons that match the given list
# of image files  'imageDirectoryList' for 'numTimes' times.
# The function will wait after pressing for 'delaySeconds'
# seconds. If the first attempt fails will execute escapeFunction
# and try again. Escapefunction must take no parameters.
#
# Returns true if succesful, false otherwise.
#
def WProgram_FindAndPressIcon(imageDirectoryList, numTimes = 1, delaySeconds = 0, backupFunction = None):
    timeout = time.time() + DELAY_TIMEOUT
    while True:
        for image in imageDirectoryList:
            r = pyautogui.locateOnScreen(image, grayscale = False)
            if r is not None:
                for press in range(0, numTimes):
                    homex,homey = pyautogui.center(r)
                    pyautogui.click(homex,homey)
                time.sleep(delaySeconds)
                return True
            else if escapeFunction is not None:
                backupFunction()
        if time.time() > timeout:
            return False

#--------- Main Window Commands

#
# Returns true if the spark OCT program was initialized, false otherwise.
#
# At the end of this function, the taskbar icon will be clicked and
# the subwindows will be ready to be individually selected from the
# taskbar highlight.
#
def WProgram_Start():
    currentSchedule = {
        lambda : WProgram_FindAndPressIcon(IMGS_MAIN_BARICON, 1, DELAY_STARTUP, lambda : WProgram_TypePress(KEY_OPENICONBAR, DELAY_OPENICONBAR))
        lambda : (WProgram_FindAndPressIcon(IMGS_MAIN_BARICON, 1, 1, lambda : WProgram_TypePress(KEY_OPENICONBAR, DELAY_OPENICONBAR)) and not WProgram_FindAndPressIcon(IMGS_MAIN_BOOTUP, 0))
    }
    print("Trying to find Spark OCT app.")
    if WProgram_RunSchedule(currentSchedule):
        return True
    else:
        print("Failed to find Spark OCT app.")

#
# Returns true if the sparkOCT GUI window was found, otherwise false
#
def WProgram_FocusOCTWin():
    currentSchedule = {
        lambda : WProgram_Start(),
        lambda : WProgram_FindAndPressIcon(IMGS_MAIN_BARFOCUS, 1),
        lambda : WProgram_FindAndPressIcon(IMGS_MAIN_WINDOW_OPEN, 1)
    }
    print("Trying to open the OCT window.")
    if WProgram_RunSchedule(currentSchedule):
        return True
    else:
        print("Failed to open the OCT window.")

#--------- 2d Window Commands
def WProgram_ModeImage():
    currentSchedule = {
        lambda : WProgram_FocusOCTWin(),
        lambda : WProgram_FindAndPressIcon(IMGS_MAIN_WINDOW_TOCTIMAGE, 1),
        lambda : WProgram_FindAndPressIcon(IMGS_MAIN_WINDOW_TOCTIMAGE_OPEN, 1)
    }
    print("Trying to open the OCT image tab.")
    if WProgram_RunSchedule(currentSchedule):
        return True
    else:
        print("Failed to open the OCT image tab.")

#--------- Volumetric window commands
def WProgram_ModeVolumetric():
    def WProgram_ModeImage():
        currentSchedule = {
            lambda : WProgram_FocusOCTWin(),
            lambda : WProgram_FindAndPressIcon(IMGS_MAIN_WINDOW_TOCTVOLUME, 1),
            lambda : WProgram_FindAndPressIcon(IMGS_MAIN_WINDOW_TOCTVOLUME_OPEN, 0)
        }
        print("Trying to open the OCT volumetric tab.")
        if WProgram_RunSchedule(currentSchedule):
            return True
        else:
            print("Failed to open the OCT volumetric tab.")

#--------- Serial window input commands

#
# Returns true if the spark debug window was initialized, false otherwise
#
def WProgram_StartSerial():
    currentSchedule = {
        lambda : WProgram_FocusOCTWin(),
        lambda : WProgram_FindAndPressIcon(IMGS_MAIN_WINDOW_TADVANCED, 1),
        lambda : WProgram_FindAndPressIcon(IMGS_MAIN_WINDOW_TADVANCED_SETUPMODE, 1, 1),
        lambda : WProgram_FindAndPressIcon(IMGS_MAIN_WINDOW_TOCTVOLUME, 1),
        lambda : WProgram_FindAndPressIcon(IMGS_MAIN_WINDOW_TOCTVOLUME_OPEN, 1)
    }
    print("Trying to open the serial window.")
    if WProgram_RunSchedule(currentSchedule):
        return True
    else:
        print("Failed to open the serial window.")

#
# returns true if the window was found, false otherwise
#
def WProgram_FocusSerial():
    currentSchedule = {
        lambda : WProgram_StartSerial(),
        lambda : (WProgram_Start() and WProgram_FindAndPressIcon(IMGS_SERIAL_BARFOCUS))
        lambda : WProgram_FindAndPressIcon(IMGS_SERIAL_OPEN, 1)
    }
    print("Searching for the serial window.")
    if WProgram_RunSchedule(currentSchedule):
        return True
    else:
        print("Failed to find the serial window.")

#
# Returns true if the setup window input prompt was found, otherwise false
#
def WProgram_CenterSerialPrompt():
    currentSchedule = {
        lambda : WProgram_FocusSerial(),
        lambda : WProgram_FindAndPressIcon(IMGS_SERIAL_PROMPT)
    }
    print("Searching for the serial prompt.")
    if WProgram_RunSchedule(currentSchedule):
        return True
    else:
        print("Failed to find the serial prompt.")
