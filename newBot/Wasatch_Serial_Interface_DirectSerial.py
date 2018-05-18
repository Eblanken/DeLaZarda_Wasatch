# TODO everything.
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
import WasatchInterface_Abstract
from wasatchGUISearchfuncs import *

#
class Wasatch_Serial_Interface_DirectSerial(Wasatch_Serial_Interface_Abstract):
    #-------------------- Public Members ---------------
    # Initializes communications over serial to the Wastach
    def __init__(self):

    # Sends a serial command to the Wasatch Microscope after 'time' milliseconds
    def sendCommand(self, command, time):

    #------------------- Private Members ---------------

    __screenWidth
    __screenHeight
