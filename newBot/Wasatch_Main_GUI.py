# TODO Controller_GUI: Verify input correctness
# COMBAK Controller_GUI: Nicer GUI.
#
# File: Wasatch_Main_GUI
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/12/2018
#
# Description:
#   Executable GUI interface for drawing bleached lines
#   with the Wasatch microscope.
#

#----------------------- Imported Libraries ------------------------------------

import tkinter
import units

from Wasatch_Controller_Commands import *
from Wasatch_Serial_Interface_AutoGUI import Wasatch_Serial_Interface_AutoGUI
from Wasatch_Serial_Interface_DirectSerial import Wasatch_Serial_Interface_DirectSerial

# ---------------------- Function Definitions ----------------------------------

#
# Description:
#   Opens a settings window for drawing a line.
#
# Parameters:
#   'microscopeCommand' Serial interface module (Subclass of Wasatch_Serial_Interface_Abstract)
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
    goButton = tkinter.Button(prompt, text = "Go", command = lambda : GCommand_BleachLine(microscopeCommand, (float(startXEntry.get()) * unitRegistry.millimeter, float(startYEntry.get()) * unitRegistry.millimeter), (float(endXEntry.get()) * unitRegistry.millimeter, float(endYEntry.get()) * unitRegistry.millimeter), float(timeEntry.get()) * unitRegistry.second))
    goButton.pack()

#
# Description:
#   Opens a command window for drawing a fiducial hash mark
#   and executes when asked by the user.
#
#  Parameters:
#   'microscopeCommand' Serial interface module (Subclass of Wasatch_Serial_Interface_Abstract)
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
    goButton = tkinter.Button(prompt, text = "Go", command = lambda : GCommand_BleachFiducial(microscopeCommand, (float(centerXEntry.get()) * unitRegistry.millimeter, float(centerYEntry.get()) * unitRegistry.millimeter), float(markWidthEntry.get()) * unitRegistry.millimeter, float(gapWidth.get()) * unitRegistry.millimeter, float(timeEntry.get()) * unitRegistry.second, orientationEntry.get()))
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
#   'root'          Main window object (tklinter.TK)
#   'commandModule' Subclass of Wasatch_Serial_Interface_Abstract that controls interactions.
#
def microscopeTerminal_exit(root, commandModule):
    commandModule.close()
    print("Closed galvo connection.")
    root.destroy();

#------------------------ Class Definitions ------------------------------------

#
# Description:
#   Entry widget that accepts a floating point number.
#   Based off of https://www.reddit.com/r/learnpython/comments/7c3edu/best_way_to_do_input_validation_on_tkinter_entry/dpmxt3i/
#
class FloatEntry(tkinter.Entry):
    #
    # Description:
    #   Initializer for the class.
    #
    def __init__(self, master = None, **kwargs):
        self.var = tkinter.StringVar(master, "0.0")
        tkinter.Entry.__init__(self, master, textvariable = self.var, **kwargs)
        self.var.trace('w', self.validate)

    #
    # Description:
    #   Checks status of entry.
    #
    # Returns:
    #   True if the entry is a float, false otherwise.
    #
    def _isFloat(self):
        try:
            float(self.get())
        except:
            return False;
        return True;

    #
    # Description:
    #   Verifies that the entry is a float.
    #
    def validate(self, *args):
        while not self._isFloat():
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
root.protocol("WM_DELETE_WINDOW", lambda : microscopeTerminal_exit(root, microscopeCommand))
if not microscopeCommand.connectedToMicroscope():
    print("Failed to connect to microscope.")
    microscopeTerminal_exit()

# Starts program
root.mainloop()
