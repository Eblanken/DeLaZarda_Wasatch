# TODO get serial connection to work, maybe nicer GUI?
#
# File: WasatchInterface_Controller
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/12/2018
#
# Description:
#
# This class creates a GUI for a user to interact with the
# microscope and send commands to the Wasatch Microscope.
# This GUI impliments all of the more advanced compound functions
# that the microscope does not already impliment as well as
# regulate communications for standard commands.
#
# NOTES: See setup notes for the WasatchInterface class you are
# using to communicate with the microscope for setup instructions.
#

#----------------------- Imported Libraries ------------------------------------

import time
import numpy as np
import tkinter
from tkinter import messagebox
from Wasatch_Serial_Commands import *
from Wasatch_Controller_GUIObjects import *
from Wasatch_Serial_Interface_AutoGUI import Wasatch_Serial_Interface_AutoGUI

#---------------------------- Constants ----------------------------------------
# Note that actual exposure times are determined from Conversions, these
# are just preferences but should not effect the total amount of energy recieved
# by the sample.
PULSEPERIOD = 100 # Duration of a delay-pulse pair in microseconds
PULSESPERSWEEP = 100 # Number of pulses per sweep of the scanner
DUTY_CYCLE = 0.75 # Percentage of on time for pulses

# ---------------------- Function Definitions ----------------------------------

#
# Opens command window for following a line and executes
# when asked by the user
#
def bleachLine(microscopeCommand):
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
    gapWidth.pack()
    percentageEntry.pack()
    startPoint = (float(startXEntry.get()), float(startYEntry.get()))
    stopPoint = (float(endXEntry.get()), float(endYEntry.get()))
    goButton = tkinter.Button(prompt, text = "Go", command = lambda: executeBleachLine(microscopeCommand, startPoint, stopPoint, float(percentageEntry.get())))
    goButton.pack()

#
# Uses serial input to draw a line from starting points to end points
# for the given percentage of time required for full bleaching exposure.
#
# All coordinates are in mm from the top left corner, exposurePercentage is a
# floating point number between 0 and 1, duration is how long the scan should
# last in microseconds. 'microscopeCommand' is the object that controls serial
# input to the microscope.
#
def executeBleachLine(microscopeCommand, startPoint, stopPoint, exposurePercentage):
    # Sets duty cycle and pulses per sweep
    onDuration = int(round(DUTY_CYCLE * PULSEPERIOD))
    offDuration = int(round((1 - DUTY_CYCLE) * PULSEPERIOD))
    microscopeCommand.sendCommand(WCommand_ScanPulseDuration(onDuration))
    microscopeCommand.sendCommand(WCommand_ScanPulseDelay(offDuration))
    microscopeCommand.sendCommand(WCommand_ScanAScans(PULSESPERSWEEP))
    # Configures path
    microscopeCommand.sendCommand(WCommand_XYRamp(startPoint, stopPoint))
    # Draws the line, number of scans dependent on previous factors
    nTimes = int(round((exposurePercentage * WConvert_BleachExposureTime(np.linalg.norm(startPoint, stopPoint))) / (2 * PULSEPERSWEEP * PULSEPERIOD)))
    microscopeCommand.sendCommand(WCommand_ScanNTimes(nTimes))

#
# Opens a command window for drawing a fiducial hash mark
# and executes when asked by the user.
#
def bleachFiducial(microscopeCommand):
    # Creates main window
    prompt = TopLevel()
    prompt.title("Bleach a Fiducial Mark")
    doneButton = tkinter.Button(prompt, text = "Done", command = prompt.destroy)
    doneButton.pack()
    # Options for line settings
    centerXEntry = FloatEntry(prompt)
    centerYEntry = FloatEntry(prompt)
    markEntry = FloatEntry(prompt)
    gapWidth = FloatEntry(prompt)
    percentageEntry = FloatEntry(prompt)
    orientationEntry = StringVar()
    ORIENTATIONS = {
        ("Horizontal", "H"),
        ("Vertical", "V")
    }
    for text, mode in MODES:
        b = Radiobutton(prompt, text = text, variable = orientationEntry, value = mode)
        b.pack()
    centerXEntry.pack()
    centerYEntry.pack()
    markEntry.pack()
    percentageEntry.pack()
    centerPoint = (float(centerXEntry.get()), float(centerYEntry.get()))
    goButton = tkinter.Button(prompt, text = "Go", command = executeBleachFiducial(microscopeCommand, centerPoint, float(markWidthEntry.get()), float(gapWidth.get()), float(percentageEntry.get()), orientationEntry.get()))
    goButton.pack()

# TODO make either vertical or horizontal optional, duration
# Uses serial input to draw a hash fiducial mark centered at
# "center" with the given width "width".
#
def executeBleachFiducial(microscopeCommand, centerPoint, markWidth, markGapWidth, exposurePercentage, orientation):
    # Prints out a hash mark with a line in the middle, consists of 5 lines
    boundXStart = centerPoint[0] - (markWidth / 2)
    boundXStop = centerPoint[0] + (markWidth / 2)
    boundYStart = centerPoint[1] - (markWidth / 2)
    boundYStop = centerPoint[1] + (markWidth / 2)
    # Draws horizontal
    hLowY = centerPoint[1] - (markGapWidth / 2)
    hHighY = centerPoint[1] + (markGapWidth / 2)
    executeBleachLine(microscopeCommand, (boundXStart, hLowY), (boundXStop, hLowY), exposurePercentage)
    executeBleachLine(microscopeCommand, (boundXStart, hHighY), (boundXStop, hHighY), exposurePercentage)
    # Draws vertical
    vLowX = centerPoint[0] - (markGapWidth / 2)
    vHighX = centerPoint[0] + (markGapWidth / 2)
    executeBleachLine(microscopeCommand, (vLowX, startY), (vLowX, stopY), exposurePercentage)
    executeBleachLine(microscopeCommand, (vHighX, startY), (vHighX, stopY), exposurePercentage)
    # Draws central
    if(orientation == "V"):
        executeBleachLine(microscopeCommand, (centerX, startY), (centerX, stopY), exposurePercentage)
    if(orientation == "H"):
        executeBleachLine(microscopeCommand, (startX, centerY), (stopX, centerY), exposurePercentage)


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
microscopeCommand = Wasatch_Serial_Interface_AutoGUI();
if not microscopeCommand.connectedToMicroscope():
    tklinter.messageBox.showError("Failed to connect to microscope.");
    goButton.state = DISABLED
# Starts program
root.mainloop()
