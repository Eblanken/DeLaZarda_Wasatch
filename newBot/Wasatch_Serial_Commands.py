#
# COMBAK Serial_Commands: add more commands
#
# File: WasatchInterface_MicroscopeSettings
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/12/2018
#
# Description:
#   These methods return strings to be
#   sent to the Wasatch via serial.
#

#---------------------- Included Libraries -------------------------------------

from Wasatch_Conversions import *
from units import *

#--------------------- Function Definitions ------------------------------------

# ------- Galvo Commands:

#
# Description:
#   Retrieves the version number of the Wasatch
#
# Response:
#    Always "Ver:#.##\r\nA\n".
#
# Returns:
#   Serial printable command string.
#
def WCommand_Version():
    return "ver"

#
# Description:
#   Resets the Wasatch.
#
# Response:
#   None.
#
# Returns:
#   Serial printable command string.
#
def WCommand_Reset():
    return "reset"

#
# Description:
#   Puts the Wasatch into update mode.
#
# Response:
#   Always 'A'.
#
# Returns:
#   Serial printable command string.
#
def WCommand_FirmwareUpdate():
    return "dfu"

#
# Description:
#   Pings the Wasatch.
#
# Response:
#   Always 'A'.
#
# Returns:
#   Serial printable command string.
#
def WCommand_Ping():
    return "ping"

#
# TODO Serial_Commands: find real world interpretation for value for conversion
#
# Description:
#   Sets the voltage control for the liquid lens
#   focus.
#
# Parameters:
#   'value' (integer) Range from 0 - 4095
#
# Response:
#   With parameters: 'A'
#   No parameters:   Current setting
#
# Returns:
#   Serial printable command string.
#
def WCommand_Focus(value = 'default_value'):
    if(value == 'default_value'):
        return "focus"
    if(isinstance(value, int) and (value > 4095 or value < 0)):
        raise ValueError("Serial Error: Requested Wasatch focus value is invalid.")
    else:
        return "focus %d" % (value)

#
# TODO Serial_Commands: find real world interpretation for value for conversion
#
# Description:
#   Sets the voltage control for the liquid lens foci.
#
# Parameters:
#   'value' (integer) Range from 0-255
#
# Response:
#   With parameters: 'A'
#   No parameters:   Current setting
#
# Returns:
#   Serial printable command string.
#
def WCommand_Foci(value = 'default_value'):
    if(value == 'default_value'):
        return "foci"
    if(isinstance(value, int) and (value > 255 or value < 0)):
        raise ValueError("Serial Error: Requested Wasatch foci value is invalid.")
    else:
        return "foci %d" % (value)

#
# Description: // TODO Serial_Commands: revisit "out#"
#   Turns the given galvo motor on and off.
#
# Parameters:
#   'servo'
#   'value'
#
# Response:
#   With parameters: 'A'
#   No parameters:   Current setting of 'servo'
#
# Returns:
#   Serial printable command string.
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
# Descriptions:
#   Reads the EEPROM of the Wasatch at the memory
#   location 'address'
#
# Parameters:
#   'address' The address to read (integer)
#
# Response:
#   Returns a page of hexadecimal from the EEPROM
#   at that location
#
# Returns:
#   Serial printable command string.
#
def WCommand_ReadEEPROM(address):
    if(isinstance(address, int)):
        return "eer %d" % (address)
    else:
        raise ValueError("Serial Error: Requested Wasatch EEPROM address is invalid.")

#
# TODO Serial_Commands: writeByte
# Description:
#   Writes a byte to the given location.
#
# Parameters:
#   'address' The location in EEPROM to write to (integer)
#   'value'   The value to write (byte)
#
# Response:
#   Always: 'A'
#
# Returns:
#   Serial printable command string.
#
def WCommand_WriteEEPROM(address, value):
    return "eew %d %d" % (address, value)

# ------- Sweep Commands:

#
# Description:
#   Sets the number of pulse triggers per sweep of the camera.
#   Reducing this value will reduce the duration of a single sweep.
#
# Parameters:
#   'numScans' (integer) (optional) Number of data points per sweep.
#                                   Range is (2-65535).
#
# Response:
#   With parameters: "ok.\n"
#   Without parameters: Returns current value
#
# Returns:
#   Serial printable command string.
#
def WCommand_ScanAScans(numScans = "default_value"):
    if(numScans != "default_value"):
        if(isinstance(numScans, int)):
            return "a_scans %d" % (numScans)
        else:
            raise ValueError("Serial Error: Requested Wasatch triggers per minor sweep is invalid.")
    return "a_scans"

#
# Description:
#   Sets the number of minor sweeps (primary sweeps) per major sweep (slower
#   orthogonal sweep for volume).
#
# Parameters:
#   'numScans' (integer) (optional) number of minor sweeps per orthogonal sweep.
#                                   Value is in range from 0 - 65534, default is 0.
#
# Response:
#   With parameters: "ok.\n"
#   Without parameters: returns current setting
#
# Returns:
#   Serial printable command string.
#
def WCommand_ScanBScans(numScans = "default_value"):
    if numScans != "default_value":
        if(isinstance(numScans, int)):
            return "b_scans %d" % (numScans)
        else:
            raise ValueError("Serial Error: Requested Wasatch minor sweeps per major sweep is invalid.")
    return "b_scans"

#
# Description:
#   Sets the delay between camera pulses in microseconds.
#
# Parameters:
#   'duration' (float) ([Time]) (optional) Delay between camera pulses.
#
#
# Response:
#   With settings: "ok.\n"
#   Without parameters: returns current setting
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
#
def WCommand_ScanPulseDelay(duration = "default_value"):
    if(duration != "default_value"):
        microseconds = round(duration.to(unitRegistry.microsecond))
        if(isinstance(microseconds.magnitude, float) and (microseconds.magnitude >= 3.0)):
            return "delay %d" % (microseconds.magnitude)
        else:
            raise ValueError("Serial Error: Requested Wasatch pulse duration is invalid.")
    return "delay"

#
# Description:
#   Sets the duration of a camera pulse in microseconds, if set to zero
#   no pulses occur.
#
#   Typical response is "ok.\n". If no pulse setting is entered will
#   respond with the current pulse setting.
#
# Parameters:
#   'duration' (float) ([Time]) (optional) The duration of a camera pulse.
#                                          Range is (0 - 65535).
#
# Response:
#   With parameters 'ok.\n'
#   Without parameters returns current setting
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
#
def WCommand_ScanPulseDuration(duration = "default_value"):
    if(duration != "default_value"):
        microseconds = round(duration.to(unitRegistry.microsecond))
        if isinstance(microseconds.magnitude, float):
            return "pulse %d" % (microseconds.magnitude)
        else:
            raise ValueError("Serial Error: Requested Wasatch pulse duration is invalid.")
    return "pulse"

# TODO Serial_Commands: more scan settings

#
# Description:
#   Configures the Wasatch to scan a square region
#   from the two specified corners.
#   All of the coordinates assumed to be in mm and
#   are converted to mm from the center.
#
# Parameters:
#   'startPoint' (Tuple of floats) ([Length]) First corner of the rectangle
#   'stopPoint'  (Tuple of floats) ([Length]) Last corner of the rectangle
#   'bRepeats'   (integer)                    The number of times to repeat
#                                             each scan line, defaults to 1
#
# Response:
#   Always 'A'
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
#
def WCommand_ScanXYRamp(startPoint, stopPoint, bRepeats = 1):
    if(isinstance(startPoint[0], float) and isinstance(stopPoint[0], float) and isinstance(startPoint[1], float) and isinstance(stopPoint[1], float), isinstance(bRepeats, int)):
        return "xy_ramp %d %d %d %d %d" % (WConvert_FromMM(startPoint)[0].magnitude, WConvert_FromMM(stopPoint)[0].magnitude, WConvert_FromMM(startPoint)[1].magnitude, WConvert_FromMM(stopPoint)[1].magnitude, bRepeats)
    else:
        raise ValueError("Serial Error: Requested Wasatch coordinates are invalid.")

# TODO Serial_Commands: other ramps

#
# Description:
#   Draws a polar ramp (concentric circular scan).
#
# Parameters:
#   'centerPoint'    The center of the scan of the form (x (mm), y (mm)) (Tuple of floats)
#   'radius'         The radius of the scanned region in mm (float)
#   'rings'          The number of concentric scanned circles. (integer)
#   'pointsPerRing'  The number of data points per scanned circle. (integer)
#   'ringRepeats'    The number of times to repeat each layer of the scan, defaults to 1 (integer)
#
# Response:
#   Always 'A'
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
#
def WCommand_ScanPolar(centerPoint, radius, rings, pointsPerRing, ringRepeats = 1):
    raise ValueError("Serial Error: Polar ramp not implimented.") # TODO

#
# Description:
#   Initiates a scan that repeats for 'count' times. If 'count'
#   is negative or if there are no arguments, scans indefinitely.
#   In vector mode, this is the number of single b-scans, in raster
#   mode these are c-scans.
#
# Parameters:
#   'count' (int) Number of scans, ranges from +- 2,147,483,648
#
# Response:
#   Always 'A'
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
#
def WCommand_ScanNTimes(count):
    if(isinstance(count, int)):
        return "scan %d" % (count)
    else:
        raise ValueError("Serial Error: Requested Wasatch scan count is invalid.")

# TODO Serial_Commands: ntscans

#
# Description:
#   Stops the current Wasatch scan at the end of the
#   current minor scan and turns off the mirrors.
#
# Response:
#   Always 'A'
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
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
