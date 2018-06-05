#
# File: WasatchInterface_Controller_Script
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/29/2018
#
# Description:
#   Executable script. Feel free to fill in whatever
#   commands you want.
#

#----------------------- Imported Libraries ------------------------------------

from Wasatch_Controller_Commands import *
from Wasatch_Serial_Interface_AutoGUI import Wasatch_Serial_Interface_AutoGUI
from Wasatch_Serial_Interface_DirectSerial import Wasatch_Serial_Interface_DirectSerial

#--------------------------- The Script ----------------------------------------

#--> Setup:
microscopeCommand = Wasatch_Serial_Interface_DirectSerial()

#--> Put your commands here:

# Note: Center of field is 5, 5 (mm)

# (x, y) in mm, time in seconds (float)
#lineHeight = 5.0 #[mm]
#lineXPosition = 0.0 #[mm] from center
#exposure = 1 #[sec] per line
#GCommand_BleachLine(microscopeCommand, (5.0+lineXPosition, 5.0-lineHeight/2), (5.0+lineXPosition, 5.0+lineHeight/2), exposure)

#(x,y) in mm, args are (module, center, length of mark, seperation b/ outermost pairs, exposure per line in (s), "V" is vertical, "H" is horizontal)
#GCommand_BleachFiducial(microscopeCommand, (5.0, 5.0), 5.0, 0.1, 5, "V")


#This part below creates lines in different exposure times
lineHeight = 5.0 #[mm]
exposures = [0.1, 0.2, 0.5, 1, 2, 5] #sec
for i in range(len(exposures)):
    lineXPosition = 2.0 + i*0.1 #[mm]
    exposure = exposures[i] #[sec] per line
    print('Current exposure :', exposure)
    GCommand_BleachLine(microscopeCommand, (lineXPosition, 5.0-lineHeight/2), (lineXPosition, 5.0+lineHeight/2), exposure)


#--> Closes connection:
microscopeCommand.close()
