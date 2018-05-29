# TODO controller_commands: verify that fiducial works. Standardize documentation
# COMBAK controller_commands: add more commands
#
# File: WasatchInterface_Controller_Commands
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/29/2018
#
# Description:
#
# These commands implement more sophisticated drawing
# options for the microscope.
#

#----------------------- Imported Libraries -----------------------------------

from Wasatch_Serial_Commands import *
from Wasatch_Serial_Interface_AutoGUI import Wasatch_Serial_Interface_Abstract
from Wasatch_Serial_Interface_AutoGUI import Wasatch_Serial_Interface_AutoGUI
from Wasatch_Serial_Interface_DirectSerial import Wasatch_Serial_Interface_DirectSerial

# ---------------------- Function Definitions ---------------------------------

#
# Uses serial input to draw a line from starting points to end points
# for the given percentage of time required for full bleaching exposure.
#
# All coordinates are in mm from the top left corner, exposurePercentage is a
# floating point number between 0 and 1, duration is how long the scan should
# last in microseconds. 'microscopeCommand' is the object that controls serial
# input to the microscope.
#
def GCommand_BleachLine(microscopeCommand, startPoint, stopPoint, timeSecs):
    # Sets duty cycle and pulses per sweep
    microscopeCommand.sendCommand(WCommand_ScanPulseDuration(WConvert_PulseDuration()))
    microscopeCommand.sendCommand(WCommand_ScanPulseDelay(WConvert_PulseDelay()))
    microscopeCommand.sendCommand(WCommand_ScanAScans(WConvert_PulsesPerSweep()))
    microscopeCommand.sendCommand(WCommand_ScanBScans(0))
    # Configures paths
    microscopeCommand.sendCommand(WCommand_ScanXYRamp(startPoint, stopPoint))
    # Draws the line, number of scans dependent on previous factors
    microscopeCommand.sendCommand(WCommand_ScanNTimes(WConvert_NumScansFromSecs(timeSecs)), timeSecs)
    print(WCommand_ScanNTimes(WConvert_NumScansFromSecs(timeSecs)))

#
# Description:
#   Uses serial input to draw a hash fiducial mark.
#
# Parameters:
#   'microscopeCommand' The command module that handles serial
#   'centerPoint'       The point object for the
#
def GCommand_BleachFiducial(microscopeCommand, centerPoint, markWidth, markGapWidth, timeSecs, orientation):
    # Prints out a hash mark with a line in the middle, consists of 5 lines
    boundXStart = centerPoint[0] - (markWidth / 2)
    boundXStop = centerPoint[0] + (markWidth / 2)
    boundYStart = centerPoint[1] - (markWidth / 2)
    boundYStop = centerPoint[1] + (markWidth / 2)
    # Draws horizontal
    hLowY = centerPoint[1] - (markGapWidth / 2)
    hHighY = centerPoint[1] + (markGapWidth / 2)
    GCommand_BleachLine(microscopeCommand, (boundXStart, hLowY), (boundXStop, hLowY), timeSecs)
    GCommand_BleachLine(microscopeCommand, (boundXStart, hHighY), (boundXStop, hHighY), timeSecs)
    # Draws vertical
    vLowX = centerPoint[0] - (markGapWidth / 2)
    vHighX = centerPoint[0] + (markGapWidth / 2)
    GCommand_BleachLine(microscopeCommand, (vLowX, boundYStart), (vLowX, boundYStop), timeSecs)
    GCommand_BleachLine(microscopeCommand, (vHighX, boundYStart), (vHighX, boundYStop), timeSecs)
    # Draws central
    if(orientation == "V"):
        GCommand_BleachLine(microscopeCommand, (centerPoint[0], boundYStart), (centerPoint[0], boundYStop), timeSecs)
    if(orientation == "H"):
        GCommand_BleachLine(microscopeCommand, (boundXStart, centerPoint[1]), (boundXStop, centerPoint[1]), timeSecs)
