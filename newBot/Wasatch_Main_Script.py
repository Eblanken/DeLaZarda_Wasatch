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
from units import *

#--------------------------- The Script ----------------------------------------

#--> Setup:
microscopeCommand = Wasatch_Serial_Interface_DirectSerial()

#--> Put your commands here:

# Note: Specify units using the pint library, ex:
# width = 10 * unitRegistry.millimeters # Value has a length of 10 mm

#lineHeight = 5.0 unitRegistry.millimeters
#lineXPosition = 0.0 unitRegistry.millimeters from center
#exposure = 1 unitRegistry.second per line
#GCommand_BleachLine(microscopeCommand, (5.0+lineXPosition, 5.0-lineHeight/2), (5.0+lineXPosition, 5.0+lineHeight/2), exposure)

#(x,y) in mm, args are (module, center, length of mark, seperation b/ outermost pairs, exposure per line in (s), "V" is vertical, "H" is horizontal)
#GCommand_BleachFiducial(microscopeCommand, (5.0, 5.0), 5.0, 0.1, 5, "V")


#This part below creates lines in different exposure times
#lineHeight = 5.0 * unitRegistry.millimeters
#exposures = [0.1, 0.2, 0.5, 1, 2, 5] * unitRegistry.second
#for i in range(len(exposures)):
#    lineXPosition = 2.0 + i*0.1 #[mm]
#    exposure = exposures[i] #[sec] per line
#    print('Current exposure :', exposure)
#    GCommand_BleachLine(microscopeCommand, (lineXPosition, 5.0-lineHeight/2), (lineXPosition, 5.0+lineHeight/2), exposure)
GCommand_TestGrid(microscopeCommand, (5000, 5000), 100, 50, 20, 40)

#--> Closes connection:
microscopeCommand.close()
