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

#--------------------------- Constants -----------------------------------------

MOTOR_IDENTIFIERS = {'q', 'p', 'i', 'h'}

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
# Description:
#   Sets the voltage control for the liquid lens
#   focus (?).
#
# Parameters:
#   'value' (Integer) (optional) Range from 0 - 4095
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
        raise ValueError("Serial Error: Requested Wasatch focus value %s is invalid." % (value))
    else:
        return "focus %d" % (value)

#
# Description:
#   Sets the voltage control for the liquid lens foci (?).
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
        raise ValueError("Serial Error: Requested Wasatch foci value %s is invalid." % (value))
    else:
        return "foci %d" % (value)

#
# Description:
#   Turns the output on and off (?).
#
# Parameters:
#   'output' (Integer) The output number, either 1 or 2.
#   'value'  (Integer) (optional) 0 for off, all other numbers on. Leave blank
#                                 to read the current settings.
#
# Response:
#   With parameters: 'A'
#   No parameters:   Current setting of the output.
#
# Returns:
#   Serial printable command string.
#
def WCommand_Toggle(output, value = 'default_value'):
    if(isinstance(output, int) and (output == 1 or output == 2)):
        if(value == 'default_value'):
            return "out%d" % (servo)
        if(isinstance(value, int) and (value >= 0)):
            return "out%d %d" % (servo, value)
        else:
            raise ValueError("Serial Error: Requested Wasatch motor state %s is invalid." % (value))
    else:
        raise ValueError("Serial Error: Requested Wasatch motor %s is invalid." % (output))

#
# Descriptions:
#   Reads the EEPROM of the Wasatch at the memory
#   location 'address'
#
# Parameters:
#   'address' (Integer) The address to read
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
        raise ValueError("Serial Error: Requested Wasatch EEPROM address %s is invalid." % (address))

#
# Description:
#   Writes a byte to the given location.
#
# Parameters:
#   'address' (Integer) The location in EEPROM to write to (integer)
#   'value'   (Integer) The value to write in hexadecimal
#
# Response:
#   Always: 'A'
#
# Returns:
#   Serial printable command string.
#
def WCommand_WriteEEPROM(address, value):
    if(isInstance(address, integer) and isInstance(value, integer) and value <= 255)
        return "eew %d %s" % (address, hex(value))
    else
        raise ValueError("Serial Error: Requested Wasatch EEPROM write location %s value %s is invalid." % (address, value))

# ------- Sweep Commands:

#
# Description:
#   Sets the number of pulse triggers per sweep of the camera.
#   Reducing this value will reduce the duration of a single sweep.
#
# Parameters:
#   'numScans' (Integer) (optional) Number of data points per sweep.
#                                   Range is (2-65535). Leave blank
#                                   to read current value.
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
            raise ValueError("Serial Error: Requested Wasatch triggers per minor sweep %s is invalid." % (numScans))
    return "a_scans"

#
# Description:
#   Sets the number of minor sweeps (primary sweeps) per major sweep (slower
#   orthogonal sweep for volume).
#
# Parameters:
#   'numScans' (Integer) (optional) number of minor sweeps per orthogonal sweep.
#                                   Value is in range from [0, 65534] multiple of 2 default is 0.
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
        if(isinstance(numScans, int) and (numScans % 2 == 0) and (numScans >= 0) and (numScans <= 65534)):
            return "b_scans %d" % (numScans)
        else:
            raise ValueError("Serial Error: Requested Wasatch minor sweeps per major sweep %s is invalid." % (numScans))
    return "b_scans"

#
# Description:
#   Sets the delay between camera pulses in microseconds.
#
# Parameters:
#   'duration' (Float) ([Time]) (optional) Delay between camera pulses.
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
        microseconds = integer(round(duration.to(unitRegistry.microsecond).magnitude))
        if(isinstance(microseconds, integer) and (microseconds >= 3)):
            return "delay %d" % (microseconds)
        else:
            raise ValueError("Serial Error: Requested Wasatch pulse delay %s is invalid." % (duration))
    return "delay"

#
# Description:
#   Sets the duration of a camera pulse in microseconds, if set to zero
#   no pulses occur. Will return current settings without parameters.
#
# Parameters:
#   'duration' (Float) ([Time]) (optional) The duration of a camera pulse.
#                                          Range is [0, 65535].
#
# Response:
#   With parameters 'ok.\n'
#   Without parameters returns current setting.
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
#
def WCommand_ScanPulseDuration(duration = "default_value"):
    if(duration != "default_value"):
        microseconds = round(duration.to(unitRegistry.microsecond).magnitude)
        if (isinstance(microseconds, integer) and microseconds >= 0 and microseconds <= 605535):
            return "pulse %d" % (microseconds)
        else:
            raise ValueError("Serial Error: Requested Wasatch pulse duration %s is invalid." % (duration))
    return "pulse"

# TODO Serial_Commands: tret, A_div, phase, trigger, a_hold, b_hold, trdelay

#
# Description:
#   Sets whether the trigger delay is added to the
#   beginning and end of the sweep. Will return current settings
#   without parameters.
#
# Parameters:
#   'enable' (Integer) Set to 1 to enable the trigger, 0 to disable.
#                      Leave blank to return the current setting.
#
# Response:
#   With parameters 'ok.\n'
#   Without parameters returns current setting.
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
#
def WCommand_ScanTriggerDelayEnable(enable = "default_value"):
    if(enable != "default_value"):
        if isinstance(enable, integer) and (enable == 0 or enable == 1):
            return "trdmode %d" % (enable)
        else:
            raise ValueError("Serial Error: Requested Wasatch trigger delay enable %s is invalid." % (enable))
    return "trdmode"

#
# Description:
#   Configures the X ramp scanning parameters for the Wasatch
#
# Parameters:
#   'startX' (float) ([Length]) Starting X position of the rectangle.
#   'stopX'  (float) ([Length]) End X position of the rectangle
#   'bRepeats'   (integer)      The number of times to repeat
#                               each scan line, defaults to 1
#
# Response:
#   Always 'A'
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
#
def WCommand_ScanXRamp(startX, stopX, bRepeats = 1):
    if(isinstance(startX.magnitude, float) and isinstance(stopX.magnitude, float) and isinstance(bRepeats, int)):
        return "xramp %d %d %d" % (WConvert_FromMM(startX.magnitude), WConvert_FromMM(stopX.magnitude), bRepeats)
    else:
        raise ValueError("Serial Error: Requested Wasatch coordinates are invalid.")

#
# Description:
#   Configures the Y ramp scanning parameters for the Wasatch
#
# Parameters:
#   'startY' (float) ([Length]) Starting Y position of the rectangle.
#   'stopY'  (float) ([Length]) End Y position of the rectangle
#   'bRepeats'   (integer)      The number of times to repeat
#                               each scan line, defaults to 1
#
# Response:
#   Always 'A'
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
#
def WCommand_ScanYRamp(startY, stopY, bRepeats = 1):
    if(isinstance(startX.magnitude, float) and isinstance(stopY.magnitude, float) and isinstance(bRepeats, int)):
        return "yramp %d %d %d" % (WConvert_FromMM(startY.magnitude), WConvert_FromMM(stopY.magnitude), bRepeats)
    else:
        raise ValueError("Serial Error: Requested Wasatch coordinates are invalid.")

#
# Description:
#   Configures the Wasatch to scan a square region
#   from the two specified corners.
#   All measurements are distance from the center.
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
    if(isinstance(startPoint[0].magnitude, float) and isinstance(stopPoint[0].magnitude, float) and isinstance(startPoint[1].magnitude, float) and isinstance(stopPoint[1].magnitude, float), isinstance(bRepeats, int)):
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
def WCommand_ScanNTimes(count = 0):
    if(isinstance(count, int)):
        return "scan %d" % (count)
    else:
        raise ValueError("Serial Error: Requested Wasatch scan count is invalid.")

#
# Description:
#   Same as above but without triggers.
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
def WCommand_ScanNTimesNoTrigger(count = 0):
    if(isinstance(count, int)):
        return "ntscan %d" % (count)
    else:
        raise ValueError("Serial Error: Requested Wasatch non-triggering scan count is invalid.")

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

#
# Description:
#   Sets the top speed of the given motor, not currently
#   implimented in the Wasatch.
#
# Parameters:
#   'motorIdentifier' (String or Char) (optional) Value is 'q', 'p', 'i', or 'h', sets the motors top speed
#
# Response:
#   Will return 'A' with no parameters
#   or with the current setting otherwise.
#   This is not currently implimented.
#
# Returns:
#   String to be directly entered into the Wasatch terminal.
#
def WCommand_MotorSetTopSpeed(motorIdentifier = 'default_value'):
    if(motorIdentifier != 'default_value')
        if(motorIdentifier in MOTOR_IDENTIFIERS)
            return "mmset %s" % (motorIdentifier)
        else
            ValueError("Serial Error: Requested Wasatch motor top speed for %s is invalid." % (motorIdentifier))
    return "mmset"

#
# Description:
#   Sets the top acceleration of the given motor, not currently
#   implimented in the Wasatch.
#
# Parameters:
#   'motorIdentifier' (String or Char) (optional) Value is 'q', 'p', 'i', or 'h'.
#                                                 Sets the target motor.
#
# Response:
#   Will return 'A' with no parameters
#   or with the current setting otherwise.
#   This is not currently implimented.
#
# Returns:
#   String to be directly entered into the Wasatch terminal.
#
def WCommand_MotorSetTopAcceleration(motorIdentifier = 'default_value'):
    if(motorIdentifier != 'default_value')
        if(motorIdentifier in MOTOR_IDENTIFIERS)
            return "maset %s" % (motorIdentifier)
        else
            ValueError("Serial Error: Requested Wasatch motor top acceleration for %s is invalid." % (motorIdentifier))
    return "maset"

#
# Description:
#   Sends the motor to the relative location given in value.
#
# Parameters:
#   'motorIdentifier' (String or Char)   Value is 'q', 'p', 'i', or 'h'.
#                                        Sets the target motor.
#   'value'           (float) ([Length]) Location to send the motor to
#                                        from current position.
#
# Response:
#   Always 'A'
#
# Returns:
#   String to be directly entered into the Wasatch serial terminal.
#
def WCommand_MotorGoAbsolute(motorIdentifier, value):
    if(motorIdentifier in MOTOR_IDENTIFIERS and isInstance(value.magnitude, float))
        return "mgr %s %d" % (motorIdentifier, WConvert_FromMM(value))
    else
        ValueError("Serial Error: Requested Wasatch motor travel distance %s is invalid." % (motorIdentifier))

#
# Description:
#   Sends the motor to the absolute location given in value.
#
# Parameters:
#   'motorIdentifier' (String or Char)   Value is 'q', 'p', 'i', or 'h'.
#                                        Sets the target motor.
#   'value'           (float) ([Length]) Location to send the motor to.
#
# Response:
#   Always 'A'
#
# Returns:
#   String to be directly entered into the Wasatch serial terminal.
#
def WCommand_MotorGoAbsolute(motorIdentifier, value):
    if(motorIdentifier in MOTOR_IDENTIFIERS and isInstance(value.magnitude, float))
        return "mg2 %s %d" % (motorIdentifier, WConvert_FromMM(value))
    else
        ValueError("Serial Error: Requested Wasatch motor travel distance %s is invalid." % (motorIdentifier))

#
# Description:
#   Sends the target motor to the home location.
#   Note: Currently disabled in the firmware.
#
# Parameters:
#   'motorIdentifier' (String or Char) (optional) Value is 'q', 'p', 'i', or 'h'.
#                                                 Sets the target motor. If not
#                                                 specified all are homed.
#
# Response:
#   Always 'A'.
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
#
def WCommand_MotorHome(motorIdentifier = 'a'):
    if(motorIdentifier != 'a')
        if(motorIdentifier in MOTOR_IDENTIFIERS)
            return "mgh %s" % (motorIdentifier)
        else
            ValueError("Serial Error: Requested Wasatch motor to home %s is invalid." % (motorIdentifier))
    return "mgh a"

#
# Description:
#   Sets the motor direction for the given motor.
#
# Parameters:
#   'motorIdentifier' (String or Char) Value is 'q', 'p', 'i', or 'h'.
#                                      Sets the target motor.
#
#   'value'           (Integer) (optional) Sets the motor forward if zero (defualt),
#                                          backwards otherwise.
#
# Response:
#   Always 'A'.
#
# Returns:
#   String to be directly entered into the Wasatch serial terminal.
#
def WCommand_MotorDirection(motorIdentifier, value = 0):
    if(motorIdentifier in MOTOR_IDENTIFIERS and isInstance(value, int))
        return "mgd %s %d" % (motorIdentifier, value)
    ValueError("Serial Error: Requested Wasatch motor %s or direction %s is invalid." % (motorIdentifier, value))

#
# Description:
#   Stops the given motor.
#
# Parameters:
#   'motorIdentifier' (String or Char) (optional) Value is 'q', 'p', 'i', or 'h', motor to stop.
#                                                 If left blank, will use 'a' to stop all motors.
#
# Response:
#   Always responds with 'A'.
#
# Returns:
#   String to enter directly into the Wasatch terminal.
#
def WCommand_MotorStop(motorIdentifier = 'a'):
    if(motorIdentifier != 'a')
        if(motorIdentifier in MOTOR_IDENTIFIERS)
            return "mstop %s" % (motorIdentifier)
        else
            ValueError("Serial Error: Requested Wasatch motor halt for %s is invalid." % (motorIdentifier))
    return "mstop a"

# Description:
#   Returns the speed and destination for each motor.
#
# Response:
#   Returns the motor parameters, also returns 'A'.
#
# Returns:
#   String to be entered directly into the Wasatch serial terminal.
#
def WCommand_MotorGetInfo():
    return "minfo"

#
# Description:
#   Returns whether the motors are currently in the home positon.
#
# Parameters:
#   'motorIdentifier' (String or Char) (optional) Value is 'q', 'p', 'i', or 'h', motor to query if home
#                                                 If left blank, will use 'a' which will return a byte
#                                                 whose bits are set to one if the motor is home, false otherwise.
#
# Response:
#   Always responds with 'A', but also responds with 1 if the motor is home, 0 otherwise.
#
# Returns:
#   String to enter directly into the Wasatch terminal.
#
def WCommand_MotorIsHome(motorIdentifier = 'a'):
    if(motorIdentifier != 'a')
        if(motorIdentifier in MOTOR_IDENTIFIERS)
            return "mih %s" % (motorIdentifier)
        else
            ValueError("Serial Error: Requested Wasatch motor home status for %s is invalid." % (motorIdentifier))
    return "mih a"
