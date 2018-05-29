# TODO: Conversions: Bleachpercentage overhaul, use default values for conversions
# COMBAK Conversions: Standardize documentation. Add more conversions.
#
# File: WasatchInterface_MicroscopeSettings
# ------------------------------
# Author: Erick Blankenberg, based off of work from Edwin
# Date: 5/12/2018
#
# Description:
#
# These methods convert user inputs in conventional units
# to units that the microscope uses for serial interpretation.
#

#---------------------------- Constants ----------------------------------------

# Microseconds of dwelling time to fully bleach one mm long section w/ standard profile
USFORMM = 3000

# Borrowed from Edwin's code, Wasatch units seem to be roughly 2093 per mm
MIN_Y = 3492
MAX_Y = 24418
MIN_X = 5081
MAX_X = 26032
MAX_LENGTH = 9566
# Experimentaly the total reach of the beam is roughly 10mm in either direction
MM_Y = 10
MM_X = 10

# Note that actual total exposure times are determined from USFORMM, these
# are just preferences but should not effect the total amount of energy
# recieved by the sample.
PULSEPERIOD = 100 # Duration of a delay-pulse pair in microseconds
PULSESPERSWEEP = 100 # Number of pulses per sweep of the scanner
DUTY_CYCLE = 0.75 # Percentage of on time for pulses, this is the assumed duty cycle in USFORMM

# ---------------------- Function Definitions ----------------------------------

#
# Converts desired point in mm to wasatch units. Good for about 0.478 microns
# but there seems to be issues where the laser goes over etc. and is pretty
# wide?
#
# InputPoints is assumed to be a tuple of size 2 whose
# values are (x, y) mm.
#
# The function returns a tuple with the arguments converted
# to mm.
#
def WConvert_FromMM(inputPoint):
    val = float((inputPoint[0] * ((MAX_X - MIN_X) / MM_X)) + MIN_X, (inputPoint[1] * ((MAX_Y - MIN_Y) / MM_Y)) + MIN_Y)
    return val

#
# Description:
#   Returns the number of scans from the required duration
#
# Parameters:
#   'numSeconds'     (float) How long the scan should last in seconds.
#   'pulsePeriod'    (int)   Period of a single pulse in microseconds.
#   'pulsesPerSweep' (int)   Number of pulses in a primary scan.
#
# Returns:
#   Integer number of scans required.
#
def WConvert_NumScansFromSecs(numSeconds, pulsePeriod = PULSEPERIOD, pulseCount = PULSESPERSWEEP):
    return int(ceil((float(numSeconds)*(10**-6)) / (PULSEPERIOD * PULSESPERSWEEP)))

#
# Determines the number of complete scans required to achieve
# the desired exposure percentage with the given duty cycle,
# and period of the pulse.
#
# TODO Conversions: Exposure overhaul (may be bugged)
#
def WConvert_NumScans(distance, exposurePercentage, dutyCycle = DUTY_CYCLE, pulsePeriod = PULSEPERIOD, pulsesPerSweep = PULSESPERSWEEP):
    # Calculates scans for full exposure
    normalizedDutyCycle = (dutyCycle / DUTY_CYCLE)
    print(("%d") % normalizedDutyCycle)
    normalRequiredTime = (USFORMM * distance) / normalizedDutyCycle
    normalRequiredPasses = normalRequiredTime / (2 * pulsesPerSweep * pulsePeriod)
    # Applies exposure percentage
    nTimes = int(round((exposurePercentage * normalRequiredPasses)))
    return nTimes

#
# Description:
#   Calculates duration of pulse for the given duty cycle.
#
# Returns:
#   Returns the pulse length in microseconds.
#
def WConvert_PulseDuration(dutyCycle = DUTY_CYCLE):
    return int(round(dutyCycle * PULSEPERIOD))

#
# Description:
#   Calculates delay between pulses for the given duty cycle.
#
# Returns:
#   The delay between pulses in  microseconds.
#
def WConvert_PulseDelay(dutyCycle = DUTY_CYCLE):
    return int(round((1 - DUTY_CYCLE) * PULSEPERIOD))

#
# Returns the number of triggers per sweep
#
def WConvert_PulsesPerSweep():
    return PULSESPERSWEEP

#
# Returns the number of seconds required to bleach a line of the given
# length.
#
# TODO: Conversions: Exposure overhaul
#
def WConvert_BleachExposureTimeSecs(distance):
    return USFORMM * distance * 10**-6
