#
# File: WasatchInterface_Main_Commands
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/29/2018
#
# Description:
#   These are the top level abstraction commands for
#   bleaching marks with the Wasatch microscope.
#

#----------------------- Imported Libraries -----------------------------------

from Wasatch_Serial_Commands import *
from Wasatch_Serial_Interface_Abstract import Wasatch_Serial_Interface_Abstract

# ---------------------- Function Definitions ---------------------------------

#
# Decription:
#   Draws a line.
#
# Parameters:
#   'microscopeCommand' Serial interface module (Subclass of Wasatch_Serial_Interface_Abstract)
#   'startPoint'        Point of form (x (mm), y (mm)) (Tuple of floats)
#   'endPoint'          Point of form (x (mm), y (mm)) (Tuple of floats)
#   'timeSecs'          Duration of drawing in seconds (Float)
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

#
# Description:
#   Draws a pound-sign shaped fiducial mark with an orientation
#   line running through the center either horizontally or vertically.
#
# Parameters:
#   'microscopeCommand' Serial interface module (Subclass of Wasatch_Serial_Interface_Abstract)
#   'centerPoint'       Center point of the fiducial of form (x (mm), y (mm)) (Tuple of floats)
#   'markWidth'         Width of the entire mark in mm. (float)
#   'markGapWidth'      Width between outer parralel members of the fiducial in mm (float)
#   'timeSecs'          Duration of draw time for each line in seconds (float)
#   'orientation'       Whether the orientation line is drawn horizontally or vertically through the centerPoint (string "H" or "V")
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
