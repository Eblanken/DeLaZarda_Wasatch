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

from WasatchInterface_Controller_Commands import *
from Wasatch_Serial_Interface_AutoGUI import Wasatch_Serial_Interface_AutoGUI
from Wasatch_Serial_Interface_DirectSerial import Wasatch_Serial_Interface_DirectSerial

#--------------------------- The Script ----------------------------------------

#--> Setup:
microscopeCommand = Wasatch_Serial_Interface_DirectSerial()

#--> Put your commands here:
# TODO

#--> Closes connection:
microscopeCommand.close()
