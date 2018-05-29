#
# File: WasatchInterface_Controller_Script
# ------------------------------
# Author: Erick Blankenberg
# Date: 5/29/2018
#
# Description:
#   Feel free to fill in whatever commands you want.
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
#GCommand_BleachLine(microscopeCommand, (1.0, 1.0), (1.0, 5.0), 0.5)

#(x,y) in mm, args are (module, center, length of mark, seperation b/ outermost pairs, exposure per line in (s), "V" is vertical, "H" is horizontal)
GCommand_BleachFiducial(microscopeCommand, (5.0, 5.0), 3.0, 1.5, 1.0, "V")

#--> Closes connection:
microscopeCommand.close()
