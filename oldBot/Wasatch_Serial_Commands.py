#
# COMBAK Serial_Commands: add more commands, standardize documentation.
#
# File: WasatchInterface_MicroscopeSettings
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/12/2018
#
# Description:
#   These methods take in parameters for serial commands and return a complete
#   string that can be entered into the terminal. Units are in mm and seconds.
#

#---------------------- Included Libraries -------------------------------------

from Wasatch_Conversions import *

#--------------------- Function Definitions ------------------------------------

# ------- Galvo Commands:

#
# Retrieves the version number of the Wasatch
#
# Response is: Ver:#.##\r\nA\n
#
def WCommand_Version():
    return "ver"

#
# Resets the Wasatch
#
# No response
#
def WCommand_Reset():
    return "reset"

#
# Puts the Wasatch into update mode
#
# Response is ACK
#
def WCommand_FirmwareUpdate():
    return "dfu"

#
# Pings the Wasatch
#
# Response is ACK
#
def WCommand_Ping():
    return "ping"

#
# TODO Serial_Commands: find real world interpretation for value for conversion
#
# Sets the voltage control for the liquid lens
# focus, value is 0 - 4095.
#
# Response is ACK, if no value is given response
# is the current setting.
#
def WCommand_Focus(value = 'default_value'):
    if(value == 'default_value'):
        return "focus"
    if(isinstance(value, int) and (value > 4095 or value < 0)):
        raise ValueError("Serial Error: Requested Wasatch focus value is invalid.")
    return

#
# TODO Serial_Commands: find real world interpretation for value for conversion
#
# Sets the voltage control for the liquid lens
# foci, value is 0 - 255.
#
# Response is ACK, if no value is given response is the current
# microscope setting.
#
def WCommand_Foci(value = 'default_value'):
    if(value == 'default_value'):
        return "foci"
    if(isinstance(value, int) and (value > 255 or value < 0)):
        raise ValueError("Serial Error: Requested Wasatch foci value is invalid.")
    return

#
# Turns the galvo motor 'servo' on and off. The motors are
# disabled if 'value' is zero, enabled if greater than zero.
#
# Typical response is ACK, responds with current state of
# 'servo' if value is blank.
#
def WCommand_Toggle(servo, value = 'default_value'):
    if(isinstance(servo, int) and (servo == 1 or servo == 2)):
        if(value == 'default_value'):
            return "out%d" % (servo)
        if(isinstance(value, int) and (value >= 0)):
            return "out%d %d" % (servo, value)
        else:
            raise ValueError("Serial Error: Requested Wasatch motor state is invalid.")
    else:
        raise ValueError("Serial Error: Requested Wasatch motor is invalid.")

#
# Reads the EEPROM of the Wasatch at the memory
# location 'address'
#
# Returns a page of hexadecimal from the EEPROM
# at that location
#
def WCommand_ReadEEPROM(address):
    if(isinstance(address, int)):
        return "eer %d" % (address)
    else:
        raise ValueError("Serial Error: Requested Wasatch EEPROM address is invalid.")

#
# TODO Serial_Commands: writeByte
# Writes the byte 'byte' to the location 'address'.
#
# Response is ACK.
#
def WCommand_WriteEEPROM(value, address):
    return " "

# ------- Sweep Commands:

#
# Sets the number of pulse triggers per sweep of the camera. Reducing
# this value will reduce the duration of a single sweep.
#
# Typical response is "ok.\n". Will respond with the current value
# if no command is entered.
#
def WCommand_ScanAScans(numScans):
    if(isinstance(numScans, int)):
        return "a_scans %d" % (numScans)
    else:
        raise ValueError("Serial Error: Requested Wasatch triggers per minor sweep is invalid.")

#
# Sets the number of minor sweeps (primary sweeps) per major sweep (slower
# orthogonal sweep for volume). Value ranges from 0 - 65534. Default is 0.
#
# Typical response is "ok.\n". Will respond with the current value
# if no command is entered.
#
def WCommand_ScanBScans(numScans):
    if(isinstance(numScans, int)):
        return "b_scans %d" % (numScans)
    else:
        raise ValueError("Serial Error: Requested Wasatch minor sweeps per major sweep is invalid.")

#
# Sets the delay between camera pulses in microseconds.
# Minimum value is 3, default is 50, maximum value is 65535.
#
# Typical response is "ok.\n", if no settings given than
# the response is the current setting for the delay between
# pulses.
#
def WCommand_ScanPulseDelay(microseconds):
    if(isinstance(microseconds, int) and (microseconds >= 3)):
        return "delay %d" % (microseconds)
    else:
        raise ValueError("Serial Error: Requested Wasatch pulse duration is invalid.")

#
# Sets the duration of a camera pulse in microseconds, if set to zero
# no pulses occur. The value is 5 by default maximum is 65535.
#
# Typical response is "ok.\n". If no pulse setting is entered will
# respond with the current pulse setting.
#
def WCommand_ScanPulseDuration(microseconds):
    if(isinstance(microseconds, int)):
        return "pulse %d" % (microseconds)
    else:
        raise ValueError("Serial Error: Requested Wasatch pulse duration is invalid.")

# TODO Serial_Commands: more scan settings
# TODO Serial_Commands: other ramp xy function alternatives

#
# Configures the Wasatch to scan a square region
# from the two specified corners.
#
# All of the coordinates assumed to be in mm and
# are converted to mm from the top left corner.
#
def WCommand_ScanXYRamp(startPoint, stopPoint):
    if(isinstance(startPoint[0], float) and isinstance(stopPoint[0], float) and isinstance(startPoint[1], float) and isinstance(stopPoint[1], float)):
        return "xy_ramp %d %d %d %d" % (WConvert_FromMM(startPoint)[0], WConvert_FromMM(stopPoint)[0], WConvert_FromMM(startPoint)[1], WConvert_FromMM(stopPoint)[1])
    else:
        raise ValueError("Serial Error: Requested Wasatch coordinates are invalid.")

# TODO Serial_Commands: xy_ramp w/ repeated

# TODO Serial_Commands: other ramps

#
# Initiates a scan that repeats for 'count' times. If 'count'
# is negative or if there are no arguments, scans indefinitely.
# In vector mode, this is the number of single b-scans, in raster
# mode these are c-scans.
#
# Response is ACK
#
def WCommand_ScanNTimes(count):
    if(isinstance(count, int)):
        return "scan %d" % (count)
    else:
        raise ValueError("Serial Error: Requested Wasatch scan count is invalid.")

# TODO Serial_Commands: ntscans

#
# Stops the current Wasatch scan at the end of the
# current minor scan and turns off the mirrors.
#
# response is ACK
#
def WCommand_ScanStop():
    return "stop"

# ------- Motor Commands:

# TODO Serial_Commands: motorTopSpeed
def WCommand_MotorSetTopSpeed():
    return " "

# TODO Serial_Commands: motorHome
def WCommand_MotorHome():
    return " "
