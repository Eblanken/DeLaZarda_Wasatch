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

import time
import WasatchInterface_Abstract
from wasatchInterface_AutoGUI_Funcs import *

#
class WasatchInterface_AutoGUI(WasatchInterface_Abstract):
    #-------------------- Public Members ---------------
    # Initializes communications over the Wasatch GUI
    def __init__(self):
        self.currentlyConnected = self.reconnectToMicroscope();

    # Returns whether the microscope was able to establish a connection
    def connectedToMicroscope(self):
        return currentlyConnected

    # Attempts to reestablish connection with the microscope, returns true if
    # succesful false otherwise
    def reconnectToMicroscope(self):
        if(!pingMicroscope())
            for i in range(1, reconectionAttempts)
                if(pingMicroscope())
                    return True
            return False
        return True


    # Sends a serial command to the Wasatch Microscope after 'time' in milliseconds
    # has elapsed. Returns a bool true if succesful and fale if failed.
    def sendCommand(self, command, time):
        # all GUI commands internally feature timer safety

    #------------------- Private Members ---------------

    #
    # This function attempts to ping the microscope
    #
    def _pingMicroscope():

    __currentlyConnected
    __screenWidth
    __screenHeight
    --reconnectionAttempts = 5;
