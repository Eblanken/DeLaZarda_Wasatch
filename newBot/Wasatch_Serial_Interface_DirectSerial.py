# TODO Interface_Serial: everything.
#
# File: WasatchInterface_DirectSerial
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/12/2018
#
# Description:
#
# This class enables communication with the Wasatch microscope
# by directly accessing serial communication.
#
# NOTES:
# * As of right now, requires NULL MODEM to work
# * Setup:
#   * Set up null modem
#   * Plug in the microscope
#   * Run the controller GUI, wait for confirmation that this program
#    has gained control of the microscope
#   * Run the SparkOCT application, wait for confirmation that the program
#     has established communications with the "microscope" (really this program)
#

import pyautogui
import pyserial
import WasatchInterface_Abstract
from Wasatch_Serial_Commands import *


#
class Wasatch_Serial_Interface_DirectSerial(Wasatch_Serial_Interface_Abstract):
    #-------------------- Public Members ---------------
    # Initializes communications over serial to the Wastach
    def __init__(self):
        reconnectToMicroscope()
    def connectedToMicroscope(self):
        return _currentlyConnected

    # Attempts to reestablish connection with the microscope
    def reconnectToMicroscope(self):
        for i in range(0, _RECONNECTIONATTEMPTS):
            if self.findPort():
                _currentlyConnected = True;
                return True
        return False

    # Sends a serial command to the Wasatch Microscope after 'time' milliseconds
    def sendCommand(self, command):
        self.serialPort.write(command.encode('utf-8'))

    #------------------- Private Members ---------------

    # Functions
    def _findPort(self):
        portList = serial.tools.list_ports.comports()
        for currentPort in portList:
            self.serialPort = serial.Serial(currentPort.device)
            self.serialPort.write(WCommand_Ping().encode('utf-8'))
            if(chr(self.serialPort.readByte()) == 'A'):
                return True
        return False:

    # Variables
    _currentlyConnected = False
    _serialPort # Object for serial comms

    # Constants
    _RECONNECTIONATTEMPTS = 5
