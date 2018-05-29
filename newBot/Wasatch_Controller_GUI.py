# TODO Controller_GUI: Verify input correctness.
# COMBAK Controller_GUI: Nicer GUI. Standardize documentation.
#
# File: Wasatch_Interface_Controller_GUI
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/12/2018
#
# Description:
#   This GUI implements more advanced
#   drawing and bleaching functions for
#   the Wasatch Microscope.
#

#----------------------- Imported Libraries ------------------------------------

import tkinter

from Wasatch_Controller_Commands import *
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
    tkinter.Label(prompt, text = "Runtime (S)").pack()
    timeEntry = FloatEntry(prompt)
    timeEntry.pack()
    goButton = tkinter.Button(prompt, text = "Go", command = lambda : GCommand_BleachLine(microscopeCommand, (float(startXEntry.get()), float(startYEntry.get())), (float(endXEntry.get()), float(endYEntry.get())), float(timeEntry.get())))
    goButton.pack()

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
    tkinter.Label(prompt, text = "Runtime (S)").pack()
    timeEntry = FloatEntry(prompt)
    timeEntry.pack()
    tkinter.Label(prompt, text = "Orientation").pack()
    orientationEntry = tkinter.StringVar()
    ORIENTATIONS = {
        ("Horizontal", "H"),
        ("Vertical", "V")
    }
    for curText, curMode in ORIENTATIONS:
        tkinter.Radiobutton(prompt, text = curText, variable = orientationEntry, value = curMode).pack()
    goButton = tkinter.Button(prompt, text = "Go", command = lambda : GCommand_BleachFiducial(microscopeCommand, (float(centerXEntry.get()), float(centerYEntry.get())), float(markWidthEntry.get()), float(gapWidth.get()), float(timeEntry.get()), orientationEntry.get()))
    goButton.pack()

# Available menu options
OPTIONS = {
    "Bleach Line" : bleachLine,
    "Bleach Fiducial" : bleachFiducial
}

#
# Description:
#   Function called when the GUI window is closed.
#
# Parameters:
#   'commandModule' Subclass of Wasatch_Serial_Interface_Abstract that controls interactions.
#
def microscopeTerminal_exit(root, commandModule):
    commandModule.close()
    print("Closed galvo connection.")
    root.destroy();

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
root.protocol("WM_DELETE_WINDOW", lambda : microscopeTerminal_exit(root, microscopeCommand))
# Starts program
root.mainloop()
