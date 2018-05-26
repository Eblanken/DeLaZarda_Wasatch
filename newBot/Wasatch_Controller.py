# TODO Controller: maybe nicer GUI?, verify timing, move constants out of
# this file.
#
# File: WasatchInterface_Controller
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/12/2018
#
# Description:
#
# This GUI implements more advanced
# drawing and bleaching functions for
# the Wasatch Microscope.
#

#----------------------- Imported Libraries ------------------------------------

import time
import tkinter

from Wasatch_Serial_Commands import *
from Wasatch_Serial_Interface_AutoGUI import Wasatch_Serial_Interface_AutoGUI
from Wasatch_Serial_Interface_DirectSerial import Wasatch_Serial_Interface_DirectSerial

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
    tkinter.Label(prompt, text = "Start X (mm)").pack()
    startXEntry = FloatEntry(prompt)
    startXEntry.pack()
    tkinter.Label(prompt, text = "Start Y (mm)").pack()
    startYEntry = FloatEntry(prompt)
    startYEntry.pack()
    tkinter.Label(prompt, text = "End X (mm)").pack()
    endXEntry = FloatEntry(prompt)
    endXEntry.pack()
    tkinter.Label(prompt, text = "End Y (mm)").pack()
    endYEntry = FloatEntry(prompt)
    endYEntry.pack()
    tkinter.Label(prompt, text = "Percentage (0 - 1)").pack()
    percentageEntry = FloatEntry(prompt)
    percentageEntry.pack()
    goButton = tkinter.Button(prompt, text = "Go", command = lambda : executeBleachLine(microscopeCommand, (float(startXEntry.get()), float(startYEntry.get())), (float(endXEntry.get()), float(endYEntry.get())), float(percentageEntry.get())))
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
    microscopeCommand.sendCommand(WCommand_ScanPulseDuration(WConvert_PulseDuration()))
    microscopeCommand.sendCommand(WCommand_ScanPulseDelay(WConvert_PulseDelay()))
    microscopeCommand.sendCommand(WCommand_ScanAScans(WConvert_PulsesPerSweep()))
    # Configures path
    microscopeCommand.sendCommand(WCommand_ScanXYRamp(startPoint, stopPoint))
    # Draws the line, number of scans dependent on previous factors
    distance = ((startPoint[0] - stopPoint[0])**2 + (startPoint[1] - stopPoint[1])**2)**0.5
    microscopeCommand.sendCommand(WCommand_ScanNTimes(WConvert_NumScans(distance, exposurePercentage)))
    time.sleep(exposurePercentage * WConvert_BleachExposureTimeSecs(distance) + 1)

#
# Opens a command window for drawing a fiducial hash mark
# and executes when asked by the user.
#
def bleachFiducial(microscopeCommand):
    # Creates main window
    prompt = tkinter.Toplevel()
    prompt.title("Bleach a Fiducial Mark")
    doneButton = tkinter.Button(prompt, text = "Done", command = prompt.destroy)
    doneButton.pack()
    # Options for line settings
    tkinter.Label(prompt, text = "Center X (mm)").pack()
    centerXEntry = FloatEntry(prompt)
    centerXEntry.pack()
    tkinter.Label(prompt, text = "Center Y (mm)").pack()
    centerYEntry = FloatEntry(prompt)
    centerYEntry.pack()
    tkinter.Label(prompt, text = "Fiducial Size (mm)").pack()
    markWidthEntry = FloatEntry(prompt)
    markWidthEntry.pack()
    tkinter.Label(prompt, text = "Gap Width (mm)").pack()
    gapWidth = FloatEntry(prompt)
    gapWidth.pack()
    tkinter.Label(prompt, text = "Exposure Percentage (0 - 1)").pack()
    percentageEntry = FloatEntry(prompt)
    percentageEntry.pack()
    tkinter.Label(prompt, text = "Orientation").pack()
    orientationEntry = tkinter.StringVar()
    ORIENTATIONS = {
        ("Horizontal", "H"),
        ("Vertical", "V")
    }
    for curText, curMode in ORIENTATIONS:
        tkinter.Radiobutton(prompt, text = curText, variable = orientationEntry, value = curMode).pack()
    goButton = tkinter.Button(prompt, text = "Go", command = lambda : executeBleachFiducial(microscopeCommand, (float(centerXEntry.get()), float(centerYEntry.get())), float(markWidthEntry.get()), float(gapWidth.get()), float(percentageEntry.get()), orientationEntry.get()))
    goButton.pack()

#
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
    print("Horizontal lines:")
    print(hLowY)
    print(hHighY)
    print(boundXStart)
    print(boundXStop)
    executeBleachLine(microscopeCommand, (boundXStart, hLowY), (boundXStop, hLowY), exposurePercentage)
    executeBleachLine(microscopeCommand, (boundXStart, hHighY), (boundXStop, hHighY), exposurePercentage)
    # Draws vertical
    vLowX = centerPoint[0] - (markGapWidth / 2)
    vHighX = centerPoint[0] + (markGapWidth / 2)
    print("Vertical lines:")
    print(vLowX)
    print(vHighX)
    print(boundYStart)
    print(boundYStop)
    executeBleachLine(microscopeCommand, (vLowX, boundYStart), (vLowX, boundYStop), exposurePercentage)
    executeBleachLine(microscopeCommand, (vHighX, boundYStart), (vHighX, boundYStop), exposurePercentage)
    # Draws central
    if(orientation == "V"):
        executeBleachLine(microscopeCommand, (centerPoint[0], boundYStart), (centerPoint[0], boundYStop), exposurePercentage)
    if(orientation == "H"):
        executeBleachLine(microscopeCommand, (boundXStart, centerPoint[1]), (boundXStop, centerPoint[1]), exposurePercentage)

# Available menu options
OPTIONS = {
    "Bleach Line" : bleachLine,
    "Bleach Fiducial" : bleachFiducial
}

#------------------------ Class Definitions ------------------------------------

#
# Entry widget that accepts a floating point number.
#
# Based off of https://www.reddit.com/r/learnpython/comments/7c3edu/best_way_to_do_input_validation_on_tkinter_entry/dpmxt3i/
#
class FloatEntry(tkinter.Entry):
    def __init__(self, master = None, **kwargs):
        self.var = tkinter.StringVar(master, "0.0")
        tkinter.Entry.__init__(self, master, textvariable = self.var, **kwargs)
        self.var.trace('w', self.validate)

    def _isFloat(self):
        try:
            float(self.get())
        except:
            return False;
        return True;

    def validate(self, *args):
        while not self._isFloat():
            if float(self.get()) >= 0:
                self.delete(len(self.get()) - 1)
            else:
                self.var = tkinter.StringVar(master, "0.0")

#
# This entry widget requires that the user enter a percentage
# between 0 and 100
#
class PercentageEntry(FloatEntry):
    def __init__(self, master = None, **kwargs):
        self.var = tkinter.StringVar(master, "0.0")
        tkinter.Entry.__init__(self, master, textvariable = self.var, **kwargs)
        self.var.trace('w', self._validate)

    def _validate(self):
        while not self.isFloat() or float(self.get()) > 100 or float(self.get()) < 0:
            if float(self.get()) >= 0:
                self.delete(len(self.get()) - 1)
            else:
                self.var = tkinter.StringVar(master, "0.0")

#--------------------------- The Script ----------------------------------------

# Opens GUI
root = tkinter.Tk()
root.title("Wasatch Command")
root.geometry("350x200")
actionList = tkinter.Spinbox(root, values = tuple(OPTIONS.keys()))
actionList.pack()
goButton = tkinter.Button(root, justify = tkinter.LEFT,text = "Build", width = 25, command = lambda: OPTIONS[actionList.get()](microscopeCommand))
goButton.pack()

# Initializes connection with microscope
microscopeCommand = Wasatch_Serial_Interface_DirectSerial();
if not microscopeCommand.connectedToMicroscope():
    print("Failed to connect to microscope.")
# Starts program
root.mainloop()
