# TODO: basic conversions
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

USFORMM = 1
# Borrowed from Edwin's code, Wasatch units seem to be roughly 2093 per mm
MIN_Y = 3492
MAX_Y = 24418
MIN_X = 5081
MAX_X = 26032
MAX_LENGTH = 9566
# Experimentaly the total reach of the beam is roughly 10mm in either direction
MM_Y = 10 # TODO get more accurate values.
MM_X = 10

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
    string = "input is %d (x) mm and %d (y) mm" % (inputPoint[0], inputPoint[1])
    print(string)
    val = ((inputPoint[0] * ((MAX_X - MIN_X) / MM_X)) + MIN_X, (inputPoint[1] * ((MAX_Y - MIN_Y) / MM_Y)) + MIN_Y)
    return val

# TODO
# Calculates exposure time from distance for maximum bleaching
# in microseconds.
#
def WConvert_BleachExposureTime(inputDistance):
    return USFORMM * inputDistance
