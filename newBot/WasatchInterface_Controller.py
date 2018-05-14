#
# File: WasatchInterface_Controller
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/12/2018
#
# Description:
#
# This class creates a GUI for a user to interact with the microscope and
# send commands to the Wasatch Microscope. This GUI impliments all of the
# more advanced compound functions that the microscope does not already
# impliment as well as regulate communications for standard commands.
#
# NOTES: See setup notes for the WasatchInterface class you are using to communicate
# with the microscope.
#

#----------------------- Imported Libraries ------------------------------------

import time
import numpy as np
import Tkinter
import tkMessageBox
import wasatchInterface_AutoGUI

#---------------------------- Constants ----------------------------------------

# Dictionary for available menu options and
OPTIONS = {
    "Draw Line" : drawLine
    "Draw Fiducial" : drawFiducial
}

# ---------------------- Function Definitions ----------------------------------

#
# Opens command window for following a line and executes
# when asked by the user
#
def drawLine(mainWindow):
    # Creates main window
    drawLinePrompt = TopLevel()
    drawLinePrompt.title("Draw a Line")
    # Options for end positions
    # Draws the line

#
# Opens a command window for drawing a fiducial hash mark
# and executes when asked by the user.
#
def drawFiducial(mainWindow):

#
# Displays the message in its own popup window and allows
# the user to acknowledge.
#
def displayMessage(mainWindow):


#--------------------------- The Script ----------------------------------------


# Opens GUI
root = Tkinter.Tk()
root.title("Wasatch Command")
root.geometry('350x200')
actionList = Tkinter.Spinbox(root, list(OPTIONS.keys()))
actionList.pack()
goButton = TKinter.Button(root, justify = Tkinter.LEFT,text = 'Build', width = 25, command = OPTIONS[actionList.get()]())
goButton.pack()

# Initializes connection with microscope
microscopeCommand = wasatchInterface_AutoGUI();
if(!microscopeCommand.connectedToMicroscope())
    print("Error, failed to connect to microscope.\n");
root.mainLoop()
