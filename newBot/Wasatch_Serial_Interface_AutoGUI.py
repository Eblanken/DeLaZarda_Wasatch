#
# File: WasatchInterface_AutoGUI
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/12/2018
#
# Description:
#
# This class enables communication with the Wasatch microscope
# by directly accessing the Spark GUI.
#
# NOTES:
# * Make sure that the sparkOCT program is already running
#

from Wasatch_Serial_Interface_Abstract import Wasatch_Serial_Interface_Abstract
from Wasatch_GUI_Commands import *

class Wasatch_Serial_Interface_AutoGUI(Wasatch_Serial_Interface_Abstract):

    #-------------------- Public Members ---------------

    # Initializes communications over the Wasatch GUI
    def __init__(self):
        # Boots up the program
        WProgram_Start()
        # Verifies connection
        self._currentlyConnected = self.reconnectToMicroscope()

    # Returns whether the microscope was able to establish a connection
    def connectedToMicroscope(self):
        return self._currentlyConnected

    # Attempts to reestablish connection with the microscope, returns true if
    # succesful false otherwise
    def reconnectToMicroscope(self):
        for i in range(1, self._RECONNECTIONATTEMPTS):
            if self._centerOnPrompt():
                return True
        return False


    # Sends a serial command to the Wasatch Microscope
    def sendCommand(self, command):
        if self._centerOnPrompt():
            WProgram_TypeString(command)
            WProgram_TypePress('enter')
        else:
            raise RuntimeError("AutoGUI: Failed to find the serial prompt.")

    #------------------- Private Members ---------------

    # Constants
    _RECONNECTIONATTEMPTS = 5

    # Variables
    _currentlyConnected = False

    #
    # This function attempts to ping the microscope
    #
    # Returns true if a correct response was recorded,
    # false otherwise.
    #
    def _pingMicroscope(self):
        return True # TODO SerialAuto: make autogui serial check ping response

    def _centerOnPrompt(self):
        return WProgram_CenterSerialPrompt()
