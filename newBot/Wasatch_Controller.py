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
import tkinter
from tkinter import messagebox
from Wasatch_Controller_GUIObjects import *
"""
from Wasatch_Serial_Interface_AutoGUI import *
"""

#---------------------------- Constants ----------------------------------------

# ---------------------- Function Definitions ----------------------------------

#
# Opens command window for following a line and executes
# when asked by the user
#
def bleachLine():
    # Creates main window
    prompt = tkinter.Toplevel()
    prompt.title("Bleach a Line")
    doneButton = tkinter.Button(prompt, text = "Done", command = prompt.destroy)
    doneButton.pack()
    # Options for line settings
    startXEntry = FloatEntry(prompt)
    startYEntry = FloatEntry(prompt)
    endXEntry = FloatEntry(prompt)
    endYEntry = FloatEntry(prompt)
    percentageEntry = FloatEntry(prompt)
    startXEntry.pack()
    startYEntry.pack()
    endXEntry.pack()
    endYEntry.pack()
    percentageEntry.pack()
    goButton = tkinter.Button(prompt, text = "Go", command = lambda: executeBleachLine(float(startXEntry.get()), float(startYEntry.get()), float(endXEntry.get()), float(endYEntry.get()), float(percentageEntry.get())))
    goButton.pack()

#
# Uses serial input to draw a line from starting points to end points
# for the given percentage of time required for full bleaching exposure.
#
def executeBleachLine(startX, startY, stopX, stopY, exposurePercentage):
    return 0
#
# Opens a command window for drawing a fiducial hash mark
# and executes when asked by the user.
#
def bleachFiducial(mainWindow):
    # Creates main window
    prompt = TopLevel()
    prompt.title("Bleach a Fiducial Mark")
    doneButton = tkinter.Button(prompt, text = "Done", command = prompt.destroy)
    doneButton.pack()
    # Options for line settings
    centerXEntry = FloatEntry(prompt)
    centerYEntry = FloatEntry(prompt)
    markEntry = FloatEntry(prompt)
    percentageEntry = FloatEntry(prompt)
    centerXEntry.pack()
    centerYEntry.pack()
    markEntry.pack()
    percentageEntry.pack()
    goButton = tkinter.Button(prompt, text = "Go", command = executeBleachFiducial(float(centerXEntry.get()), float(centerYEntry.get()), float(markWidthEntry.get()), float(percentageEntry.get())))
    goButton.pack()

#
# Uses serial input to draw a hash fiducial mark centered at
# "center" with the given width "width".
#
def executeBleachFiducial(centerX, centerY, markWidth, exposurePercentage):
    return 0

#
# Displays the message in its own popup window and allows
# the user to acknowledge.
#
def displayMessage(mainWindow):
    return 0

# Dictionary for available menu options and
OPTIONS = {
    "Bleach Line" : bleachLine,
    "Bleach Fiducial" : bleachFiducial
}


#--------------------------- The Script ----------------------------------------


# Opens GUI
root = tkinter.Tk()
root.title("Wasatch Command")
root.geometry("350x200")
actionList = tkinter.Spinbox(root, values = list(OPTIONS.keys()))
actionList.pack()
goButton = tkinter.Button(root, justify = tkinter.LEFT,text = "Build", width = 25, command = lambda: OPTIONS[actionList.get()]()) # TODO get serial connnections to this
goButton.pack()

# Initializes connection with microscope
#
"""
microscopeCommand = wasatchInterface_AutoGUI();
if(!microscopeCommand.connectedToMicroscope())
    messageBox.showError("Failed to connect to microscope.");
    goButton.state = DISABLED
"""
# Starts program
root.mainloop()
