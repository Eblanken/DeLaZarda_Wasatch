#
# File: Wasatch_Controller_GUIObjects
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/12/2018
#
# Description:
#
# These classes are extensions of the tklinter GUI components that automatically
# validate user input.
#

#----------------------- Imported Libraries ------------------------------------

import tkinter

# ------------------------ Class Definitions -----------------------------------

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

    def validate(self, *args):
        try:
            float(self.get())
        except:
            self.delete(len(self.get()) - 1)

#
#
#
class PercentageEntry(tkinter.Entry):
    def __init__(self, master = None, **kwargs):
        self.var = tkinter.StringVar(master, "0.00")
        tkinter.Entry.__init__(self, master, textvariable = self.var, **kwargs)
        self.var.trace('w', self.validate)

    def validate(self, *args):
        while (len(self.get() > 0): # TODO seems to only run once
            try:
                float(self.get())
            except:
                self.delete(len(self.get()) - 1)
